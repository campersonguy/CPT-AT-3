# Cameron Guglielmino - CPT AT 3 Documentation

## **Week 1 - Project Definition and Requirements** ##
I want to create a platform for users to be able to read crime stories. To accomplish this, users will sign up to the platform, and they will be able to read stories published by other users. Users will be able to like other crime stories, and the most popular/liked stories will appear on the front page. Users can also post their own crime stories.

Users will also be able to customise their profile with a username, profile picture and about me. They can also follow other users, and they will receive notifications when that user publishes a story. Users can also set their password to secure their account and prevent others from logging into it.

I will use the design created on Figma last year as a template for a new design for the website and improve upon some aspects of the original that were not as strong (e.g colour palette, typography, user interactions). I also want to remove the 'crime chat' sections of the original design to encourage wider use of the platform without promoting organised crime.

### **Functional Requirements**

- Users should be able to sign up to the site and log in with the same account at a later date.
- Users should be able to customise their profile (e.g profile picture, username, password)
- Users should be able to view and follow other users.
- Users should be able to post stories onto the platform.

### **Non-Functional Requirements**

- The app should be able to load webpages in under 2 seconds.
- The app should be easy to navigate for new users.
- The system should be able to support at least 1000 different users.
- The system should be able to store info of each different user (e.g username, password, id)

### **Client Feedback**

- Need to add a fourth functional requirement (has been added)
- Need to add more detail onto some of the functional/non-functional requirements

## **Week 2 - Basic Design of UI, Hierachy and Interactive Elements**

### **Design Table**:

| Aspect of Design | Description |
| ---------------- | ----------- |
| Landing Page | The landing page should display the logo, and give the user the option to either log in or sign out. When signing up or logging in, the user has the option to enable 'Keep Me Signed In', where this page is skipped and the user is automatically logged in. This option will automatically disable if the user does not log in for 14 days or logs out manually. |
| Navigation Bar | This bar will display in every page except for the landing page. The bar will have options to take users directly to the Top Crimes, Search Crimes, Submit Crimes and Leaderboard pages, as well as an option to edit their account and settings through a dropdown menu attached to an icon in the top-right corner displaying the user's profile picture. |
| Top Crimes Page | This is the page the user will be directed to upon being logged in.  On the left, there will be a display of the most liked crime posted in the last week (titled 'This Week's Top Crime'). On the right, there will be a display of 'The Latest Crimes', where the user can sort the crimes by most recent, most liked, and most viewed. This display will show the first 100 crimes ordered by the user's preference, and disply the number of likes, favourites and views on each one. The user should be able to scroll through them. Clicking on one of them will take the user to an individual page so they can read the crime. |
| Individual Crime Page | This is the page where the user will be able to read an individual crime. On the left will be a display of the name of the crime, the user(s) who posted it, and an option to favourite/like/dislike/share the crime, which will also display the number of each as well as the number of views. Underneath that, there will be a comment section where users can read and post comments about the crime, sorted by number of likes and displaying the username of the commenter as well as the date and time of when it was posted. On the right will be the posted crime, with the option to scroll through it if the crime is long enough. |
| Profile Settings Page | This is the page where the user can edit their profile. On the left will be a sidebar allowing the user to view different pages of their settings (Account Details/Settings) and allow them to log out of their account. On the Account Details page, the user can change their username, password and email, however changing the password and email will require the user to input their password and the email will send the new email address a verification code. The user will also be able to see how many crimes they've submitted/liked, how many followers they have, and how many other users they're following. Hovering over the following stat will show a small list of the profile pictures of people they're following. |
| Colour Palette | Primary: Gray, Secondary: White, Accent: Navy Blue. The accent colour will likely be used on buttons to add contrast. |
| Other Pages | Search Crimes, Submit Crimes, Leaderboard, Settings, Login/Signup Page (not included in prototype sketch) |

### **Images of Sketch**

**Landing Page**

![landingpage](drawing1.jpeg)

**Individual Crime Page**

![individualcrime](drawing2.jpeg)

**Top Crimes Page**

![topcrimes](drawing3.jpeg)

**Profile Settings Page**

![profilesettings](drawing4.jpeg)

### **Client Feedback**

- Landing page is very empty with a lot of blank space, needs more interactions or text as the only features on there are login/signup buttons
- Annotations are not very detailed, more detail has been added to the Design Table
- No colour scheme or typography design choices present, need to add those more visually in the Alternative Design as it is difficult to visualise typography/colours on a drawing


## **Week 3 - Alternative Design - Playing with Possibilities**

### **Design Table**:

| Aspect of Design | Description |
| ---------------- | ----------- |
| Landing Page | The landing page is similar to the original design. I wanted to add some text to prevent it looking very empty, as before it only had a large image of the logo, but functionality-wise it is the same. The page still feels lacking in terms of interactions for the user, so for the actual project I want to add more features to this page. |
| Navigation Bar | The navigation bar has been moved from the top to the left side of the screen. I believe the navigation bar is more fitting on the top rather than the side as there is much more blank space when it is on the side, leading to it looking more empty. To fill some of the empty space, I added an image of the confessions.com logo. |
| Top Crimes Page | This page is the most similar to previous designs. The main difference is the navigation bar being moved and the colours/typography, so the main functions of the page are the same as before. The 'click to view more' button uses the accent colour to make it stand out. |
| Submit Crimes Page | The submit crimes page needed to have a lot of features to add to one story so the entire page wouldn't be taken up by a box to type in. The page has options to write a story, add a list of names, add the date, write a description, attach images and set to different modes of viewing (Public, Private). It also has an option to save your progress and finish later, so the longer stories don't have to be written in one go. |
| Colour Palette | Primary: Blue, Secondary: Dark Indigo, Accent: Dark Blue. Since the last prototype of this website used a mainly grey and black colour scheme, I wanted to change the colour so the website wasn't only monochrome colours. The background colour of each page is a blue gradient. This palette has a less serious feel to it compared to the grey and black from before, so for the actual project this is the palette I would use, or have a toggleable dark theme with the original grey/black colour scheme. |
| Typography | The font used for majority of the text is Cooper Hewitt. I didn't have a specific font design in mind for this, so I used a less serious font than before since the colour scheme for this design isn't as intense (mainly blue compared to mainly grey and black). For the actual project, I want to choose a more serious-looking font. |

### **Images of Design (Canva)**

**Landing Page**

![landingpage](ss_1.png)

**Top Crimes Page**

![topcrimes](ss_2.png)

**Submit Crimes Page**

![submitcrimes](ss_3.png)

### **Client Feedback**

- No annotations present on design images (will be added onto the design table instead)
- Landing page is less empty than in the previous iteration of design, but could still use more detail in final project
- Designs are overall very similar to the previous iteration from last week, with some minor design changes and improvements such as the navigation bar moved to the side


## **Week 4 - Designing algorithms - Functional Steps for User Focused Design**

### **Basic Algorithm - Creating an Account - Pseudocode**

```
1. Declare variables: username, password, confirmpassword, email, verificationcode, 
matchverificationcode
2. Prompt user to enter a username, password and email
3. Get username, password and email
4. Display username, password and email
5. IF username is taken, THEN
    5.1. DO
        5.1.1. Display error message "Username is taken"
        5.1.2. Prompt user to enter new username
        5.1.3. Get new username
    5.2. WHILE username is taken
6. IF password is less than 8 characters, THEN
    6.1. DO
        6.1.1. Display error message "Password is less than 8 characters"
        6.1.2. Prompt user to enter new password
        6.1.3. Get new password
    6.2. WHILE password is less than 8 characters
7. IF password does not contain a number
    7.1. DO
        7.1.1. Display error message "Password does not contain a number"
        7.1.2. Prompt user to enter new password
        7.1.3. Get new password
    7.2. WHILE password does not contain a number
8. IF password does not contain a capital letter
    8.1. DO
        8.1.1. Display error message "Password does not contain a capital letter"
        8.1.2. Prompt user to enter new password
        8.1.3. Get new password
    8.2. WHILE password does not contain a capital letter
9. ENDIF
10. Prompt user to enter a confirmpassword
11. Get confirmpassword
12. Display confirmpassword
13. IF confirmpassword does not match password, THEN
    13.1. DO
        13.1.1. Display error message "Passwords do not match"
        13.1.2. Prompt user to enter new confirmpassword
        13.1.3. Get confirmpassword
    13.2. WHILE confirmpassword does not equal password
13. ENDIF
14. Set verificationcode to random 6-digit integer
15. Send verificationcode to email
16. Prompt user to input matchverificationcode
17. IF matchverificationcode does not match verificationcode, THEN
    17.1. DO
        17.1.1. Display error message "Verification codes do not match"
        17.1.2. Prompt user to re-enter verificationcode
        17.1.3. Get verificationcode
    17.2. WHILE matchverificationcode does not match verificationcode
18. Create account with username, password and email data
19. Log in user to platform
```

### **Flowchart Image**

![flowchart](flowchart.png)

### **Test Cases**

**Test Case ID:** AD-001

**Test Case Name:** Creating an account

**Preconditions:** User is not logged into an account

**Test Steps:**
1. User will enter a username and password.
2. User will click the 'Sign Up' button.
3. System will check for if the username matches with another existing account. If so, the user will be prompted to change their username until it is valid.
4. System will check for if the username meets some conditions (at least 8 characters, must have a number, must have a capital letter). If not, the user will be prompted to change their password until it is valid.
5. System will prompt the user to retype their password in 'Confirm password'.
6. System will check for if the confirm password matches the original. If not, the user will be prompted to retype it until they match.
7. System will send a randomly generated 6-digit verification code to the inputted email.
8. System will prompt the user to input the same 6-digit code.
9. System will check the verification codes match. If not, the user will be prompted to retype it until they match.
10. System will create the account with the correct username, password and email data.
11. User will be logged into the account.

**Expected Result:** Account is created with correct data and user is logged in with the account.

**Priority:** Very High


**Test Case ID:** AD-002

**Test Case Name:** Resetting account password

**Preconditions:** User already has an account

**Test Steps:**
1. User will click the 'Reset password' button.
2. User will input their current username and email address.
3. System will send a randomly generated 6-digit verification code to the inputted email.
4. System will prompt the user to input the same 6-digit code.
5. System will check the verification codes match. If not, the user will be prompted to retype it until they match.
6. User will be prompted to enter a new password.
7. System will update the password through the account data.
8. User will be logged into the account.

**Expected Result:** Account data is correctly updated and user is logged in with the account.

**Priority:** High

### **Client Feedback**

- Need to fix up flowchart - inaccurate to pseudocode (will be changed), also there is a singular missing arrow that NEEDS fixing
- No usage of variables within test cases such as `username`, `password` etc


## **Week 5 - Setting Up for Development and Database Work (SQL)**

**20/8/25 - Initial Backend Setup**

- I first managed to install all the necessary dependencies for Python, VSCode, Flask, SQLite and Git-Bash. I progressed through the tutorial well at first, but I did get stuck on the `pip install flask` step as, when trying to put the command into Git-bash, it would respond with `Command not found`. Yi Ping assisted me in getting Flask to work.
- I set up the required file directory with folders for `static`, `templates`, `working_documents` and `database`, plus `database_manager.py` and `main.py`. Within the `database` folder I set up the SQLite Database with a few different files - one for the actual data (which will contain tables that can be imported with Excel) and a Query Editor which will contain the SQL queries. I managed to add the initial table from the `SETUP` docs, however I didn't yet understand how the tables worked.

**21/8/25 - Setting Up Database Tables**

- For this lesson, I aimed to figure out how the SQL tables worked and start adding the queries. I went through the SQL tutorial website and looked through the SQL course on Grok to revise the basic functions of SQL (since it had been a while since I'd done the course). After a bit, I remembered how SQL queries are structured with `SELECT * FROM`, `WHERE` and `ORDER BY`. I used SQL's `CREATE TABLE` and `INSERT INTO` functions to create a basic layout for two tables - `UserData` and `PostData` - however I realised I could generate the data using Mockaroo, which I would do tomorrow.

**22/8/25 - Populating Tables and Sorting Data with SQL**

- Using Mockaroo, I was able to add two tables of mock data with 1000 rows each, for both user and posts on the website. For `userData`, there are columns for `userID` (which is the primary key), `username`, `password`, `email` and `creationdate`. For `postData`, there are columns for `postID`, `username` (of whoever posted it), `post` (for the actual text), `postTime`, `public` (bool), `views` and `likes`. There were some columns that I forgot to add such as `postTitle`, `followers`, `following` and `description`, which will be added later.
- I added some queries for posts with over 2000 `likes` and over 90,000 `views`, which are both very basic for now. Later, I improved them and added some more queries so that there were five in total.
    - UserData: Select data from a specific user, sort by most recently created users.
    - PostData: Sort by the top 50 most liked/viewed posts, sort by posts within the last (timeframe).

## **Weeks 6, 7 and 8 - Creating and Styling Webpages (HTML/CSS)**

**25/8/25 - Setting up the Frontend**
- I started the lesson by finishing up the meetings from the last period. Then, I started to go through the second setup document and copied the code into the appropriate files. However, when I got up to rendering the website, I couldn't get it to load and got hit with a Jinga2 error. Instead of fixing it, I went through the rest of the docs just in case it would work when I finished (it didn't). I couldn't figure out how to get it to render the page, so instead I left it as is and waited for the double CPT on Thursday to get it fixed.

**28/8/25 - Fixing the Rendering and Designing a Page**
- I managed to deduce that it was an issue with trying to load the page, as it stated that the error was `Template not found:` with an incorrect pathing to `index.html`. By fixing the pathing to fit the file directory I had, I managed to get `index.html` loaded onto the page by using the link in the terminal after running `python main.py` once I ran `cd Flask` first so the command can access `main.py`. Afterwards, I linked up `style.css` and `favicon.png` so the page would display with a logo and render the stylesheet properly (except for the first image that has an incorrect link and can't render), and redirected one of the links on the navigation bar to a page that I had created, `homepage.html`, to be able to show the original page had loaded as well as being able to display any new pages I would create.
- I aimed to recreate the first page that had been initially designed on Canva, and then to link a signup and login page. Before starting, I went through the HTML/CSS and JavaScript courses on Grok to refresh myself, and then I started designing the page. I only managed to add a gradient background, an image, some text and two buttons onto the page before the lesson ended.

```
body {
    background: linear-gradient(to right, rgb(0, 0, 172), rgb(31, 31, 74));
    text-align: center;
}

img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 350px;
}
```

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="..\static\css\homepage_style.css"/>
    <link rel="icon" type="image/x-icon" href="..\static\images\favicon.png"/>
    <title>confessions.com</title>
  </head>
  <body>
    <img src="..\..\static\images\logo.png" alt="logo">
    <h1 id="a">The only place where you can see the latest crimes. It's the details the news 
    doesn't tell you.</h1>
    <p class="button login" id="login">Log In</p>
    <p class="button signup" id="signup">Sign Up</p>
  </body>
</html>
```

**29/8/25 - Fixing the first page**
- I aimed to fix up the first page of my website by adding some JavaScript to make the buttons work. I started by going back through some of the Grok source on JavaScript to recall how it works, and I started by getting the text to change when the buttons were clicked. I was able to do this with the folowing script:

```
<body>
  <img src="..\..\static\images\logo.png" alt="logo">
  <h1 id="title">The only place where you can see the latest crimes. It's the details the news 
  doesn't tell you.</h1>
  <a href="login" class="button login" id="login">Login</a>
  <a href="signup" class="button signup">Sign Up</a>
  <p class="copyright">© Cameron Guglielmino Productions 2025 Pty Ltd.</p>
  <script>
    function Login() {
        title.textContent = 'login';
    }
    login.onclick = Login;
  </script>
</body>
```

**1/9/25 & 2/9/25 - Adding new pages**
- For these lessons, I wanted to start on adding more pages to my website, and add some details to them so they weren't completely empty.
- In order to add more pages, `main.py` has to be able to load them. So, to get the new pages to load (`login.html` and `top_crimes.html`), more code has to be added to `main.py`. The initial code for `index.html` looks like this:

```
@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def homepage():
    data = dbHandler.listExtension()
    return render_template("index.html", content=data)
```

- The first `@app.route` line determines what the URL for the page will be. In this case, it can be either set to `/index.html` or `/` because, in HTML, `index.html` is used as the first page so it interprets `/index.html` as nothing, so the front page loads first. The `data` line is used to pass data to the frontend, so it isn't useful yet and doesn't need to be included. At the time, I didn't know what the second `@app.route` line was used for, so I didn't include it either. The `return` line is used to link the appropriate HTML file, and `content=data` is only for passing data so it doesn't need to be included. For `login.html`, the new code looks like this: (and `top_crimes.html` is essentially the same with a different link)

```
@app.route("/login")
def login():
    return render_template("partials/login.html")
```

- To add detail to the pages, I linked `login.html` and `top_crimes.html` with their own stylesheets and copied over the gradient I used on the front page. Under `login.html`, I learned how to add input boxes, so the user can input their username/email and password when the login page was fully working, and then added an Enter button below it. The code for it looked like this: (mind that the signup link doesn't work yet)

```
<body>
    <img src="..\..\static\images\logo.png" alt="logo">
    <p>Username or Email</p> <br>
    <input id="username" placeholder="Enter username..."><br>
    <p>Password</p><br>
    <input id="password" placeholder="Enter password..."><br>
    <p>Don't have an account? <a href="signup"><u>Sign Up</u></a></p><br>
    <p class="incorrect" id="inc"></p><br>
    <button id="enter">Enter</button>
</body>
```

- For `top_crimes.html`, I aimed to add a navigation bar on the left side of the page. I started with a simple list that contained each page that I planned to add as an option to switch to through the navigation bar. To replicate the original navigation bar design from earlier in the project, the links would be listed vertically and there would be a logo at the bottom of the bar. To do this, i first set `list-style-type` to `none` to remove the bullet points that were visible, set `text-decoration` to `none` to remove the underlines and added `border-bottom: 2px solid black` to each `li` to give them a visible separation, plus `padding-top: 20px` and `padding-bottom: 20px` to space them out more. Under `nav ul li:last-child`, I added `padding-bottom: 450px` to ensure that the navigation bar extends far enough to make it the entire page. For the logo, I added `margin-top: 260px` to position it at the bottom of the bar (and yes I am aware this is not the most efficient way to do that, but it's good enough for now). For final details, I removed the `a` from the Top Crimes link to make it unusable and styled it grey to show the user that they can't go to the page they're already on. For the rest of the links, I used `nav ul li:hover` to change the background color slightly when the links are hovered over and used `nav ul li a:hover` to make the text bold when hovered over.

```
<head>
    <link rel="stylesheet" href="..\static\css\top_crimes_style.css" />
    <link rel="icon" type="image/x-icon" href="..\static\images\favicon.png" />
    <title>confessions.com - Top Crimes</title>
    <nav>
        <ul>
            <li class="selected">Top Crimes</li>
            <li><a href="search_crimes">Search Crimes</a></li>
            <li><a href="submit_crimes">Submit Crimes</a></li>
            <li><a href="leaderboard">Leaderboard</a></li>
            <li><a><img src="..\static\images\logo.png" alt="logo" width="128" height="60" 
            class="logo"></a></li>
        </ul>
    </nav>
</head>
```

```
nav {
    position: fixed;
    top: 0;
    left: 0;
    border-right: 2px solid black;
}

nav ul {
    text-align: center;
    list-style-type: none;
    justify-content: flex-start;
    margin: 0;
    padding: 0;
}

nav ul li {
    background-color: rgb(47, 47, 134);
    padding-top: 20px;
    padding-bottom: 20px;
    font-family: 'Titillium Web';
    border-bottom: 2px solid black;
}

nav ul li:last-child {
    padding-bottom: 450px;
}

nav ul li a {
    text-decoration: none;
    color: white;
    font-family: 'Titillium Web';
    padding: 30px;
}

nav ul li a:hover {
    font-weight: bold;
}

nav ul li:hover {
    background-color: rgb(31, 31, 130);
}

nav ul li.selected {
    color: gray;
    background-color: rgb(20, 20, 104);
}

nav ul li:last-child {
    background-color: rgb(47, 47, 134);
}

.logo {
    margin-top: 260px;
    padding: 0px;
}
```

**3/9/25 & 4/9/25 - Passing Data to the Frontend**
- This is where the fun begins: passing data to the frontend before Mr Clark teaches you how to. To figure this out, I first tried googling how to pass data, but ended up giving up because I couldn't get a clear answer. Instead, I attempted to look through the example code to figure out how the extension table is used in the example page.

- The first thing I noticed in the `index.html` page was this line from `main.py`:

```
@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def homepage():
    data = dbHandler.listExtension()
    return render_template("index.html", content=data)
```

- The second thing I noticed was in `index.html` which used a lot of lines such as `{{ % for row in content %}}`, `{{ % endfor %}}`, `"Product image for the {{ row[1] }} VSCode extension."`, etc.

```
{% extends 'layout.html' %} {% block content %}
<div class="container">
  {% for row in content %}
<div class="card">
  <img
    class="card-image"
    src="{{ row[4] }}"
    alt="Product image for the {{ row[1] }} VSCode extension."
  />
  <h1 class="card-name">{{ row[1] }}</h1>
  <p class="card-about">{{ row[3] }}</p>
  <a class="card-link" href="{{ row[2] }}"
    ><button class="btn">Read More</button></a
  >
</div>
{% endfor %}
</div>
{% endblock %}
```

- I deduced that the passed data is translated through the `{{ % (whatever) % }}` formatting that has been used in the example pages. Specifically, the line `{{ % for row in content}}` is structured similarly to a for loop used in other coding languages such as JavaScript and C#, and the last line from the `main.py` extract says `content=data` after `data = dbHandler.listExtension()`. `data = dbHandler.listExtension()` is used to access `database_manager.py` to run `listExtension()`, which looks like this:

```
def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data
```

- I figured out that `def` functions from `database_manager.py` are what is used to translate data from the SQL tables to the frontend webpages. To access them on other pages, I added a separate function on `database_manager.py` and ported the data to whatever pages I wanted through `main.py`. For example, to get data from posts to the Top Crimes page:

```
def listPostData():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT user, post, views, likes FROM postData").fetchall()
    con.close()
    return data


def sortPostData1():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    view = cur.execute(
        "SELECT * FROM postData ORDER BY views DESC LIMIT 100;"
    ).fetchall()
    con.close()
    return view


def sortPostData2():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    view = cur.execute(
        "SELECT * FROM postData ORDER BY likes DESC LIMIT 100;"
    ).fetchall()
    con.close()
    return view
```
```
@app.route("/top_crimes")
def topcrimes():
    data = dbHandler.listPostData()
    view1 = dbHandler.sortPostData1()
    view2 = dbHandler.sortPostData2()
    return render_template(
        "partials/top_crimes.html", content=data, view1=view1, view2=view2
    )
```

- From the Top Crimes page, I can then access the data using `{{ % view1[0][1] % }}`, where the first digit represents what row of data to use and the second represents what column. Using this method, I entered `SELECT user, pw, email FROM userData` and ported it to the Login page to attempt to set up a functional Login page that compares entered login credentials to existing details from the database.

```
<script>
    const data = {{ content | tojson | safe }};
    function Enter() {
        if (username.value == "" || password.value == "") {
            inc.textContent = "Missing username or password";
        } else {
            for (let i = 0; i <= data.length - 1; i++) {
                if (username.value.trim() != data[i][0] && username.value.trim() != data[i][2]) {
                    inc.textContent = "Incorrect username or password";
                } else {
                    const outerIndex = data.findIndex(inner => inner.includes(username.value));
                    if (password.value != data[outerIndex][1]) {
                        inc.textContent = "Incorrect username or password";
                    } else {
                        inc.textContent = "";
                        window.location.href = "top_crimes";
                    }
                }
            }
        }
    }
    enter.onclick = Enter;
</script>
```

**4/9/25 - Styling Pages**
- For these lessons, I wanted to style some of the pages to make them look better, mainly `top_crimes`, `login` and `signup`. Styling `login` and `signup` was very easy, as I just made sure to align the input fields properly and added a description to `login` since the page was very bland and had nothing on it outside of the actual login fields. For `signup`, I also added a box on the right side, next to the input fields, displaying the conditions an account must meet, such as the password must have at least 8 characters and must have a number in it. To make these conditions work, I added some javascript code to detect what was in the fields and update the conditions box dynamically:

```
    <script>
        const uchar = document.getElementById("uchar");
        const uspa = document.getElementById("uspa");
        const pchar = document.getElementById("pchar");
        const num = document.getElementById("num");
        const cap = document.getElementById("cap");
        const match = document.getElementById("match");
        const signupForm = document.getElementById('signup');
        let numtest = /\d/;
        let captest = /[A-Z]/;
        let spatest = / /;
        let atest = /@/;

        function updateData() {
            if (username.value.length <= 16 && username.value.length >= 3) {
                uchar.style.color = "lime";
            } else {
                uchar.style.color = "red";
            }
            uchar1.textContent = " (" + username.value.length + ")";

            if (!spatest.test(username.value) && username.value.length >= 1) {
                uspa.style.color = "lime";
            } else {
                uspa.style.color = "red";
            }

            if (password.value.length >= 8) {
                pchar.style.color = "lime";
            } else {
                pchar.style.color = "red";
            }
            pchar1.textContent = " (" + password.value.length + ")";

            if (numtest.test(password.value)) {
                num.style.color = "lime";
            } else {
                num.style.color = "red";
            }

            if (captest.test(password.value)) {
                cap.style.color = "lime";
            } else {
                cap.style.color = "red";
            }

            if (password.value === cpassword.value && password.value !== "") {
                match.style.color = "lime";
            } else {
                match.style.color = "red";
            }
        }
        const intervalId = setInterval(updateData, 1);
    </script>
```
- This code would update the colors of each condition as well as displaying exactly how many characters the username and passowrd has, as shown in this screenshot:

![signup](signup.png)

**8/9/25 - 11/9/25 - Sorting Data in Real Time**
- For these lessons, I aimed to generate data in real time on the `top_crimes` page based on the selected option under a dropdown menu. To do this, I originally wrote code to take the first line of data from `postData` and display it:

```
<p><strong>#{{ view1[0][0] }} - {{ view1[0][2]}}, by: {{ view1[0][1] }}</strong><br>👁&nbsp;
{{ view1[0][6] }}&nbsp;👍&nbsp;{{ view1[0][7] }}<br><br>{{ view1[0][3] }}</p>
```

- However, this code only generates a single line from the database, and I would have to copypaste that line over a thousand times to generate all the data. Plus, it wouldn't be able to update when the dropdown menu was changed. Therefore, I had to write a script that not only generates all the lines of data, but also updates it. In JavaScript, I wrote this code to generate all the `li` elements:

```
for (let i = 0; i < 50; i++) {
    const li = document.createElement("li");
    li.classList.add("crime");
    ol.appendChild(li);
    const br = document.createElement("br");
    const br2 = document.createElement("br");
    ol.appendChild(br);
    ol.appendChild(br2);
}
```

- This would generate 50 elements that could then be set to the correct text elements. However, to change the text of the elements in JS, you can't use `<strong>` and {{ view1[x][y] }} properly without it breaking. Instead of `.textcontent`, you can use `.innerHTML` (provided you change {{ view1[x][y] }} to ${view1[x][y]}):

```
list[i].innerHTML = `<strong>#` + (i + 1) + ` - ${sort2[i][2]} - ${sort2[i][1]}</strong><br>👁
&nbsp;${sort2[i][6]}&nbsp;👍&nbsp;${sort2[i][7]}<br><br>${sort2[i][3]}`;
```

- After getting the website to generate text properly, I added a dropdown menu that would let the user sort by either views or likes. The way I managed to do this was first generating the 50 list elements, then nesting the above code into a `for` loop that ran infinitely, so it would automatically update.

- As well as sorting the data, I wanted to style the page, since I currently just had it list them on the page with no styling whatsoever. To do this, I seperated each list entry into a box to make the list feel more orderly, then used `<br>` in the code to seperate the title, the view/like count, and the actual story. In the end, it looked like this:

![topcrimes](topcrimes.png)

**17/9/25 - 19/9/25 - Adding Data to the Backend & Lighthouse Testing**

- Next, I needed to learn how to add data to the backend through the `signup` page. At the time, the `signup` page would only detect if your inputs met the conditions, but wouldn't actually add the data to the backend. To add data, I needed to nest the `signup` inputs inside a `<form>`, as the following:

```
    <form id="signup" action="/signup" method="POST">
        <p class="sg">Username</p>
        <input id="username" placeholder="Enter username..." class="sg" name="user">
        <p class="sg">Email</p>
        <input id="email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2, 4}$" placeholder="Enter
        email..." class="sg" name="email">
        <p class="sg">Password</p>
        <input id="password" type="password" placeholder="Enter password..." class="sg"
        name="pw">
        <p class="sg">Confirm Password</p>
        <input id="cpassword" type="password" placeholder="Enter password..." class="sg">
        <p class="sg">Already have an account? <a href="login"><u>Log In</u></a></p>
        <p class="incorrect" id="inc"></p><br>
        <button id="enter" class="sg">Enter</button>
    </form>
```

The `action` and `method` of the form would directly correspond to the code in `main.py`. I updated the code for the `signup` page to be able to add to the database, connecting it to a function in `database_manager.py`:

```
@app.route("/signup", methods=["POST", "GET"])
def signup():
    data = dbHandler.listUserData()
    if request.method == "POST":
        user = request.form["user"]
        pw = request.form["pw"]
        email = request.form["email"]
        creationdate = date.today()
        dbHandler.insertContact(user, pw, email, creationdate)
        return redirect(url_for("topcrimes"))
    else:
        return render_template("partials/signup.html", content=data)
```

```
def insertContact(user, pw, email, creationdate):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO userData (user,pw,email,creationdate) VALUES (?,?,?,?)",
        (user, pw, email, creationdate),
    )
    con.commit()
    con.close()
```

- This code will add data from the form into the database through the `insertContact` function. Each of the fields in `signup` corresponds to `user`, `pw`, and `email`.

- As well as adding functionality to the `signup` page, I also ran Lighthouse tests on some of my other webpages to try and detect any flaws within my existing pages. All of the pages scored at least 90, except `top_crimes` with a massive outlier, a score of 44. This was clearly a problem, and it scored so low because my code was running every frame, slowing the website down. To fix this, I instead made the code update only when the dropdown menu was updated, through nesting the code under the function `handleDropdownChange`, activated by the dropdown menu.

```
<select class="sort" id="sort" name="sort" onchange="handleDropdownChange()">
    <option value="views">Views</option>
    <option value="likes">Likes</option>
</select>
```

**22/9/25 - 25/9/25 - Adding the Last Pages**

- The last few pages I needed to add were `search_crimes`, `submit_crimes`, `about_us` and `leaderboard`[^1].

[^1]: Leaderboard didn't really fit the design of the website, since it was designed around how many crimes someone posted which could easily be cheesed by spamming. This was a page I ended up scrapping, mainly because it didn't fit and I didn't have time to add it.

- Starting with `search_crimes`, the main thing I needed to implement was a 'searching' function, as other than that it was very similar to `top_crimes`. The best way to do this is to only generate values from the database that contain the search input. Both values are attached to `.toLowerCase()` to prevent capitalisation affecting the values.

```
if (view1[i][2].toLowerCase().includes(search.value.toLowerCase())) {
```

- This if statement checks if the search value is included in the title/username of each post. This means only posts that contain the search value can appear, which makes it work properly. Adding the if statement to the existing data generation code in `top_crimes` looks like this:

```
    function generateData() {
        let i1 = 0;
        ol.innerHTML = '';
        for (let i = 0; i < view1.length; i++) {
            if (dropdown.value === 'title') {
                if (view1[i][2].toLowerCase().includes(search.value.toLowerCase())) {
                    const li = document.createElement("li");
                    li.classList.add("crime");
                    ol.appendChild(li);
                    const br = document.createElement("br");
                    const br2 = document.createElement("br");
                    ol.appendChild(br);
                    ol.appendChild(br2);
                    li.innerHTML = `<strong>` + `${view1[i][2]} - ${view1[i][1]}</strong>
                    <br>👁&nbsp;${view1[i][6]}&nbsp;👍&nbsp;${view1[i][7]}<br><br>
                    ${view1[i][3]}`;
                    i1 += 1;
                }
            } else {
                if (view1[i][1].toLowerCase().includes(search.value.toLowerCase())) {
                    const li = document.createElement("li");
                    li.classList.add("crime");
                    ol.appendChild(li);
                    const br = document.createElement("br");
                    const br2 = document.createElement("br");
                    ol.appendChild(br);
                    ol.appendChild(br2);
                    li.innerHTML = `<strong>` + `${view1[i][2]} - ${view1[i][1]}</strong>
                    <br>👁&nbsp;${view1[i][6]}&nbsp;👍&nbsp;${view1[i][7]}<br><br>
                    ${view1[i][3]}`;
                    i1 += 1;
                }
            }
        }
    }
```

- For `submit_crimes`, it is very similar to `signup` in that it mainly utilises a form and input fields to function. The following form takes the user's name (as an input since I hadn't done user login sessions yet), their title, their story and the publicity of the crime.

```
    <form id="signup" action="/submit_crimes" method="POST">
        <label style="margin-left: 200px;">
            Name:
            <input style="text-align: left;" placeholder="Your name here..." name="user">
        </label>
        <label style="margin: 50px;">
            Title:
            <input style="text-align: left;" placeholder="Name your crime..." name="title">
        </label><br><br>
        <label>
            Your Story Here: <br><br>
            <textarea size="180" style="height: 300px; width: 700px; margin-left: 140px;
            text-align: left;"
                placeholder="Write here..." name="post"></textarea>
        </label><br><br>
        <label>
            <input size="60" type="checkbox" name="public">
            Public?
        </label><br><br>
        <button id="enter">Enter</button>
    </form>
```

- In `main.py`, I added code to add form data into the database:

```
@app.route("/submit_crimes", methods=["POST", "GET"])
def submitcrimes():
    if request.method == "POST":
        user = request.form["user"]
        title = request.form["title"]
        post = request.form["post"]
        postDate = date.today()
        public = request.form["public"]
        views = "0"
        likes = "0"
        if public == "on":
            public = "true"
        else:
            public = "false"
        dbHandler.insertPost(user, title, post, postDate, public, views, likes)
        return redirect(url_for("topcrimes"))
    else:
        return render_template("partials/submit_crimes.html")
```

```
def insertPost(user, title, post, postTime, public, views, likes):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO postData (user, title, post, postTime, public, views, likes)
            VALUES (?,?,?,?,?,?,?)",
            (user, title, post, postTime, public, views, likes),
        )
        con.commit()
```

- This code takes all the inputs from `submit_crimes` and puts them into the database using the appropriate `database_manager.py` function.

- For `about_me`, I added a short description of the website's history (yapping about how confessions.com started from the New Social Media Presentation from the end of Year 9), since that page didn't need too much interactivity since it was just a text description of the website.

**27/9/25 - 13/9/25 - Final Additions**

- Firstly, I needed to rework my login system so that it would use sessions that would better suit how the website was setup. The previous design I used would check in JavaScript for the correct logins, but in order to transmit that data to other pages I would need to use session IDs. To fix this, I would have to use a form (similarly to `submit_crimes`) to compare the inputted data with the existing logins in the database.

```
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
```

- This code compares the user and password with ones from the database, which either reloads the page if it's wrong or redirects to `top_crimes` if it's valid. It also sets the session variables properly if they need to be used within other pages.

- The next thing I wanted to fix were the crimes. I wanted each crime to have its own page so you could comment, view and like them, and for that I reworked crimes to have a description that would show up and you could click to read the full story. For this, I attached this script to my `top_crimes` page:

```
ol.addEventListener("click", async (event) => {
    if (event.target !== ol && event.target.dataset.crime !== undefined) {
        const crime = "{{ crime }}"
        const c = event.target.dataset.crime;
        await fetch("/set_session_crime", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ c })
        });
        window.location.href = "crime";
    }
});
```

- This detects when an element of the crime list is clicked and redirects you to a separate page for it. The `/set_session_crime` line sets some important session variables and the JS redirects you, so that the page can load with correct information. The `crime` code in `main.py` looks like this:

```
@app.route("/crime", methods=["POST", "GET"])
def crimepg():
    if "user" in session:
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
    else:
        return redirect(url_for("profile2"))
```

- This code sends lots of information to the page based on the crime selected previously, as well as some user-based variables for adding the comments. The page then uses this info to load the correct crime, with the right user, time of post (which was also added around this time), description, story and comments. The like icon changes depending on whether or not the user has liked the post (which was added later).

- The comment form also works with this code, and adds the comment into the database. When loading the page, the frontend checks for comments with the same `postID` as the one being viewed and only displays those ones. Using `window.location.reload()`, the page can reload instantly and display the comment without the user having to automatically reload.

- The code for the crime page can be seen here:

```
document.addEventListener("DOMContentLoaded", () => {
    for (let i = 0; i < data.length; i++) {
        if (data[i][2] === crime.c) {
            c1.innerHTML = `<strong> ${data[i][2]} - ${data[i][1]} - (${data[i][5].replace
            ('\n', '<br>')})</strong><br>👁&nbsp;${data[i][6]}&nbsp;`;
            if (liked === false) {
                c2.innerHTML = `👍🏻`;
            } else {
                c2.innerHTML = `👍`;
            }
            c3.innerHTML = `&nbsp;${data[i][7]}`;
            p2.innerHTML = `${data[i][3].replace('\n', '<br>')}`;
            i1.value = data[i][0];
            for (let i1 = 0; i1 < comm.length; i1++) {
                if (comm[i1][1] === data[i][0]) {
                    const br = document.createElement("br");
                    div.appendChild(br);
                    const p = document.createElement("p");
                    div.appendChild(p);
                    p.classList.add("crime");
                    p.innerHTML = `<strong>${comm[i1][2]} (${comm[i1][4]})</strong><br>
                    ${comm[i1][3].replace('\n', '<br>')}`;
                }
            }
        }
    }
});
```

- I also added a profile page for the user to change their profile settings and display statistics. This page contained a form that would save the changes made, however it didn't account for bypassing initial restrictions on usernames and passwords. There was also a separate form for logging out the user, so I used hidden ID values for each form to differentiate them in `main.py`.

```
@app.route("/profile", methods=["POST", "GET"])
def profile():
    post = dbHandler.listPostData()
    comm = dbHandler.listCommData()
    like = dbHandler.listLikeData()
    if "user" in session:
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
        )
```

- The last thing I wanted to add was to make the views and like counts work. The views were relatively easy, as I just made it increment by one when the page was loaded.

```
def updateView(crime):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute(
            "UPDATE postData SET views = views + 1 WHERE title = ?",
            (crime,),
        )
        con.commit()
```
- However, making likes work properly is very, very painful. In order for it to work, the system needs ot detect if the user has already liked the post (in which case it should be removed) or add a like if the user has not liked it. Visibility-wise, the like icon would change depending on if the post was liked.

```
c2.addEventListener("click", async (event) => {
    if (c2.innerHTML = `👍`) {
        c2.innerHTML = `👍🏻`;
    } else {
        c2.innerHTML = `👍`;
    }
    fetch("/like", {
        method: "POST"
    });
    window.location.reload();
});
```

- In `main.py`, I wrote some scripts to add or remove the like. I created a new SQL table to store the like data, in which each would have a postID that it would be attached to.

```
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
```

```
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
```

- While this updates correctly in the backend, the only issue is that the frontend doesn't always update dynamically. This was the main issue with the final product that I had, as I wasn't able to fix it.

- The last thing I did was get ChatGPT to generate some crimes that I could manually add to the database to replace the mock data that was entirely in Latin. I generated around 60 crimes to add, however I was able to make it generate them to be added as an SQL command.

**15/10/25 - Client Testing**

- For the client testing, I had Zac test my website for bugs. The only issues he found was the aforementioned like bug, as well as bypassing the username and password restrictions through the profile page. However, everything else worked as expected and he was able to comment, view, search for and create crimes effectively.

- The only remaining issues were:

1. The like button would sometimes not update visually when it was clicked. it would add to the database properly, but wouldn't update on the frontend sometimes unless the page was reloaded.
2. The profile stats would break if you changed your username, as it counted based on how many likes/posts/comments were under a certain username rather than the user's ID.
3. You can bypass the initial naming restrictions on usrenames and passwords in the profile menu.
4. Some of the positioning of elements breaks when a different screen size is used, as many elements use margins to be positioned. The website is mainly designed around the screen size that I use.

- However, most of them are minimal and don't break the website if used.

**Lighthouse Testing Final Scores**

- Homepage: 100
- Login: 94
- Signup: 98
- Top Crimes: 88
- Search Crimes: 98
- Submit Crimes: 98
- Your Profile: 99
- Crime page: 92

**Final Product**

![home](homepage.png)
![login](login.png)
![signup](signup.png)
![topcrimes](topcrimes.png)
![searchcrimes](search_crimes.png)
![submitcrimes](submit_crimes.png)
![profile](profile.png)
![crimepage](crimepage.png)