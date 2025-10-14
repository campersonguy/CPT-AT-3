import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def listUserData():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT user, pw, email FROM userData").fetchall()
    con.close()
    return data


def listPostData():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM postData").fetchall()
    con.close()
    return data


def listPostData1(id):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM postData WHERE postID = ?", (id,)).fetchone()
    con.close()
    return data


def listCommData():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM commentData;").fetchall()
    con.close()
    return data


def listLikeData():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM likeData;").fetchall()
    con.close()
    return data


def sortPostData1():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    view = cur.execute(
        "SELECT * FROM postData ORDER BY views DESC LIMIT 1000;"
    ).fetchall()
    con.close()
    return view


def sortPostData2():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    view = cur.execute(
        "SELECT * FROM postData ORDER BY likes DESC LIMIT 1000;"
    ).fetchall()
    con.close()
    return view


def insertContact(user, pw, email, creationdate):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO userData (user,pw,email,creationdate) VALUES (?,?,?,?)",
        (user, pw, email, creationdate),
    )
    con.commit()
    con.close()


def insertPost(user, title, desc, post, postTime, views, likes):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO postData (user, title, post, description, postTime, views, likes) VALUES (?,?,?,?,?,?,?)",
            (user, title, desc, post, postTime, views, likes),
        )
        con.commit()


def insertComment(postID, user, comm, time):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO commentData (postID, user, comm, time) VALUES (?,?,?,?)",
            (postID, user, comm, time),
        )
        con.commit()


def changeUser(new_user, new_pw, new_email, old_user):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute(
            "UPDATE userData SET user = ?, pw = ?, email = ? WHERE user = ?",
            (new_user, new_pw, new_email, old_user),
        )
        con.commit()


def updateView(crime):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute(
            "UPDATE postData SET views = views + 1 WHERE title = ?",
            (crime,),
        )
        con.commit()


def addLike(user, id):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO likeData (user, postID) VALUES (?,?)", (user, id))
        con.commit()


def removeLike(user, id):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM likeData WHERE user = ? AND postID = ?", (user, id))
        con.commit()


def updateLikes(count, id):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE postData SET likes = ? WHERE postID = ?", (count, id))
        con.commit()
