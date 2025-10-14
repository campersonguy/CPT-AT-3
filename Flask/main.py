from flask import Flask, redirect, url_for, session, render_template, request, jsonify
from datetime import date, datetime
import sqlite3 as sql
import database_manager as dbHandler

app = Flask(__name__)
app.secret_key = "oisfoheomhf389f89317gc68eo"


@app.route("/vsc", methods=["POST", "GET"])
def index():
    data = dbHandler.listExtension()
    return render_template("templatepgs/index.html", content=data)


@app.route("/", methods=["POST", "GET"])
def homepage():
    return render_template("partials/homepage.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        pw = request.form["pw"]
        userlist = get_user(user) or {}
        if user in userlist and userlist["pw"] == pw:
            session["user"] = user
            session["id"] = userlist[0]
            session["pw"] = pw
            session["email"] = userlist[3]
            return redirect(url_for("topcrimes"))
        else:
            return redirect(url_for("login"))
    else:
        data = dbHandler.listUserData()
        return render_template("partials/login.html", content=data)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    data = dbHandler.listUserData()
    if request.method == "POST":
        user = request.form["user"]
        pw = request.form["pw"]
        email = request.form["email"]
        creationdate = date.today()
        dbHandler.insertContact(user, pw, email, creationdate)
        session["user"] = user
        session["pw"] = pw
        session["email"] = email
        return redirect(url_for("topcrimes"))
    else:
        return render_template("partials/signup.html", content=data)


@app.route("/top_crimes")
def topcrimes():
    view1 = dbHandler.sortPostData1()
    view2 = dbHandler.sortPostData2()
    if "user" in session:
        return render_template(
            "partials/top_crimes.html", user=session["user"], view1=view1, view2=view2
        )
    else:
        return render_template(
            "partials/top_crimes.html",
            view1=view1,
            view2=view2,
            crime=session.get("crime"),
        )


@app.route("/search_crimes")
def searchcrimes():
    view = dbHandler.listPostData()
    return render_template(
        "partials/search_crimes.html", view=view, crime=session.get("crime")
    )


@app.route("/submit_crimes", methods=["POST", "GET"])
def submitcrimes():
    if request.method == "POST":
        user = request.form["user"]
        title = request.form["title"]
        desc = request.form["desc"]
        post = request.form["post"]
        postDate = datetime.now().strftime("%d/%m/%y, %I:%M %p")
        views = "0"
        likes = "0"
        dbHandler.insertPost(user, title, post, desc, postDate, views, likes)
        return redirect(url_for("topcrimes"))
    else:
        return render_template("partials/submit_crimes.html", user=session["user"])


@app.route("/leaderboard")
def leaderboard():
    return render_template("partials/leaderboard.html")


@app.route("/about_us")
def about_us():
    return render_template("partials/about_us.html")


@app.route("/profile", methods=["POST", "GET"])
def profile():
    post = dbHandler.listPostData()
    comm = dbHandler.listCommData()
    like = dbHandler.listLikeData()
    if session.get("user"):
        if request.method == "POST":
            id = request.form["id"]
            if id == "1":
                session["user"] = None
                session["pw"] = None
                session["email"] = None
                session["id"] = None
                return redirect(url_for("homepage"))
            if id == "2":
                new_user = request.form["user"]
                new_pw = request.form["pw"]
                new_email = request.form["email"]
                old_user = session["user"]
                dbHandler.changeUser(new_user, new_pw, new_email, old_user)
                session["user"] = new_user
                session["pw"] = new_pw
                return render_template(
                    "partials/profile.html",
                    user=session["user"],
                    pw=session["pw"],
                    email=session["email"],
                    post=post,
                    comm=comm,
                    like=like,
                )
        else:
            return render_template(
                "partials/profile.html",
                user=session["user"],
                pw=session["pw"],
                email=session["email"],
                post=post,
                comm=comm,
                like=like,
            )
    else:
        return render_template(
            "partials/profile2.html",
            user=session["user"],
            pw=session["pw"],
            email=session["email"],
            post=post,
            comm=comm,
            like=like,
        )


@app.route("/profile2")
def profile2():
    return render_template(
        "partials/profile2.html",
        user=session["user"],
        pw=session["pw"],
        email=session["email"],
    )


@app.route("/crime", methods=["POST", "GET"])
def crimepg():
    crime = session.get("crime")
    dbHandler.updateView(crime["c"])
    user = session.get("user")
    crime = session.get("crime")
    crime1 = crime["c"]
    id = get_id(crime1)
    liked = check_likes(user, id)
    data = dbHandler.listPostData1(id)
    comm = dbHandler.listCommData()
    liked = check_likes(user, id)
    commdata = dbHandler.listCommData()
    data = dbHandler.listPostData()
    if request.method == "POST":
        if request.form["comm"]:
            postID = request.form["postid"]
            comm = request.form["comm"]
            time = datetime.now().strftime("%d/%m/%y, %I:%M %p")
            if session.get("user"):
                user = session.get("user")
                dbHandler.insertComment(postID, user, comm, time)
            return redirect("/crime")

    else:
        return render_template(
            "partials/crime.html",
            user=session["user"],
            crime=crime,
            data=data,
            commdata=commdata,
            liked=liked,
        )


def get_user(user):
    con = sql.connect("database/data_source.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM userData WHERE user = ?", (user,))
    user = cur.fetchone()
    con.close()
    return user


@app.route("/set_session_crime", methods=["POST", "GET"])
def set_session_crime():
    data = request.get_json()
    session["crime"] = data
    return jsonify({"status": "ok", "crime": session["crime"]})


@app.route("/like", methods=["POST"])
def like():
    if request.method == "POST":
        crime = session["crime"]
        crime1 = crime["c"]
        id = get_id(crime1)
        user = session["user"]
        liked = check_likes(user, id)
        print("Liked: ", liked)
        if not liked:
            dbHandler.addLike(user, id)
            count = get_count(id)
            dbHandler.updateLikes(count, id)
            return redirect(url_for("crimepg"))
        if liked:
            dbHandler.removeLike(user, id)
            count = get_count(id)
            dbHandler.updateLikes(count, id)
            return redirect(url_for("crimepg"))


def get_id(crime):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute("SELECT postID FROM postData WHERE title = ?", (crime,))
    crime2 = cur.fetchone()
    con.close()
    if crime2:
        return crime2[0]
    else:
        return None


def get_count(id):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM likeData WHERE postID = ?", (id,))
    count = cur.fetchall()
    count1 = len(count)
    con.close()
    return count1


def check_likes(user, id):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM likeData WHERE user = ? AND postID = ?", (user, id))
    count = cur.fetchall()
    if len(count) >= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
