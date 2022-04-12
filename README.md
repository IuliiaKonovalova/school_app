# Cool School

## **Contents**

* [About](#About)
* [User Experience Design](#User-Experience-Design)
  * [Strategy](#Strategy)
  * [Target Audience](#Target-Audience)
  * [User Stories](#User-Stories)
    * [First Time Visitor Goals](#First-Time-Visitor-Goals)
    * [Frequent Visitor Goals](#Frequent-Visitor-Goals)
    * [Potential Client Goals](#Potential-Client-Goals)
    * [Boss Goals](#Boss-Goals)
    * [Teachers' Goals](#Teachers-Goals)
    * [Receptionists' Goals](#Receptionists-Goals)
    * [Sales Managers' Goals](#Sales-Managers-Goals)
    * [Parents' Goals](#Parents-Goals)
* [Technologies used](#Technologies-used)
* [Features](#Features)
* [Design](#Design)
  * [Colour Scheme](#Colour-Scheme)
  * [Typography](#Typography)
  * [Imagery](#Imagery)
  * [Wireframes](#Wireframes)
* [Flowcharts](#Flowcharts)
* [Information Architecture](#Information-Architecture)
  * [Database](#Database)
  * [Entity-Relationship Diagram](#Entity-Relationship-Diagram)
  * [Data Modeling](#Data-Modeling)
* [Testing](#Testing)

* [Deployment](#Deployment)
  * [Local deployment](#Local-deployment)
  * [Heroku Deployment](#Heroku-Deployment)

* [Credits](#Credits)

* [Acknowledgments](#Acknowledgments)

## About

This is [Cool School app](https://school-application-konovalova.herokuapp.com/), which is a school management application. The main goal Ff this app is to help the school to manage the students, teachers, classes, subjects, etc. Moreover, the app is aimed at increasing the efficiency of the school management. The app is developed by [Iuliia Konovalova](https://github.com/IuliiaKonovalova).
Repository: [GitHub Repo](https://github.com/IuliiaKonovalova/school_app)

[Back to contents](#contents)

## User Experience Design

### Strategy

Developed for a real early childhood school, the app is designed to be easy to use and intuitive. The main goal of the app is to help the school to manage the students, teachers, classes, subjects, etc. This is achieved by the use of a simple and intuitive interface. As a final goal, the app is aimed at increasing the efficiency of the school management.

### Target Audience

The app was developed for all members of the early childhood school. 
  * Bosses: to control the flow of the school, to manage the students, teachers, classes, subjects, sales, etc.;
  * Parents: to control their children attendance, to manage their children's payments, to manage their children's schedules, etc.;
  * Teachers: to control their classes, to manage their classes' schedules, to access students' personal information on time, to manage their classes' attendance, etc.;
  * Sales Managers: to control sales, to manage the sales, to manage the payments, to manage the schedules, to access students' personal information on time, to manage the attendance, etc.;
  * Receptionists: to control the schedule of the school, to manage the schedule, to access students' personal information on time, to manage the attendance, etc.;

### User Stories

#### **First Time Visitor Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/IuliiaKonovalova/school_app/issues/1)| As a First Time Visitor, I want to be able to easily understand the main purpose of the app, so that I can learn more about this app. |
|[#2](https://github.com/IuliiaKonovalova/school_app/issues/2)|As a First Time Visitor, I want to be able to easily navigate through the app, so that I can find the content.|
|[#3](https://github.com/IuliiaKonovalova/school_app/issues/3)|As a First Time Visitor, I want to be able to register my account, so that I can learn the benefits of the app as a user.|
|[#4](https://github.com/IuliiaKonovalova/school_app/issues/4)|As a First Time Visitor, I want to be able to find the app useful, so that I can use it according to my needs.|

#### **Frequent Visitor Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#5](https://github.com/IuliiaKonovalova/school_app/issues/5)|As a Frequent User, I want to be able to log in to my account, so that I can have a personal account.|
|[#6](https://github.com/IuliiaKonovalova/school_app/issues/6)|As a Frequent User, I want to be able to easily log in and log out, so that I can access my personal account information.|
|[#7](https://github.com/IuliiaKonovalova/school_app/issues/7)|As a Frequent User, I want to be able to easily recover my password in case I forget it, so that I can recover access to my account.|
|[#8](https://github.com/IuliiaKonovalova/school_app/issues/8)|As a Frequent User, I can be able to change my password, so that I can be sure that nobody else can access my account.|

#### **Potential Client Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#9](https://github.com/IuliiaKonovalova/school_app/issues/9)|As a Potential client, I want to be contacted by sales managers, so that I can make a prudent decision about being a member.|

#### **Boss Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#11](https://github.com/IuliiaKonovalova/school_app/issues/11)|As a Boss, I want to be able to view new applications, so that I can control the flow of potential clients.|
|[#13](https://github.com/IuliiaKonovalova/school_app/issues/13)|As a Boss, I want to be able to delete or approve membership, assign a role to a new member, so that I can keep data up to date.|
|[#14](https://github.com/IuliiaKonovalova/school_app/issues/14)|As a Boss, I want to be able to add, edit data on a kid, so that I can have a profile for each student.|
|[#15](https://github.com/IuliiaKonovalova/school_app/issues/15)|As a Boss, I want to be able to delete a member, so that I can control the access to the application.|
|[#16](https://github.com/IuliiaKonovalova/school_app/issues/16)|As a Boss I can see the info about kids provided by the company: name, contact info, classes visited, how many classes left, so that refresh the information about a client.|
|[#17](https://github.com/IuliiaKonovalova/school_app/issues/17)|As a Boss, I want to be able to search for a particular member, so that I can easily access information on this member.|
|[#18](https://github.com/IuliiaKonovalova/school_app/issues/18)|As a Boss, I want to be able to sort members according to a role, so that I can easily access particular group of members.|
|[#19](https://github.com/IuliiaKonovalova/school_app/issues/19)|As a Boss, I want to be able to search for a particular student, so that I can easily access information on this student.|
|[#21](https://github.com/IuliiaKonovalova/school_app/issues/21)|As a Boss, I want to be able to sort students by the urgent sale, so that I can control the sales in the company and preserve clients.|
|[#22](https://github.com/IuliiaKonovalova/school_app/issues/22)|As a Boss, I want to be able to see lessons schedule, so that I can schedule time to talk to a teacher or a parent.|
|[#23](https://github.com/IuliiaKonovalova/school_app/issues/23)|As a Boss, I want to see see information on students for each lesson, so that I can control students’ attendance, learn clients preferences.|
|[#24](https://github.com/IuliiaKonovalova/school_app/issues/24)|As a Boss, I want to be able to see sales' details, so that I can check which sales manager and which parent was involved in a deal.|
|[#51](https://github.com/IuliiaKonovalova/school_app/issues/51)|As a Boss, I want to be able to delete students from the application, so that I can control the flow of the present students.|

#### **Teachers' Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#25](https://github.com/IuliiaKonovalova/school_app/issues/25)|As a Teacher, I want to be able to search for a particular student, so that I can easily access information on this student.|
|[#26](https://github.com/IuliiaKonovalova/school_app/issues/26)|As a Teacher, I want to be able to see personal information on a kid, so that I can know student’s personal data.|
|[#28](https://github.com/IuliiaKonovalova/school_app/issues/28)|As a Teacher, I want to be able to see lessons schedule, so that I can manage my time.|
|[#29](https://github.com/IuliiaKonovalova/school_app/issues/29)|As a Teacher, I want to be able to see information on students for each lesson, so that I can be prepared for each student.|

#### **Receptionists' Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#30](https://github.com/IuliiaKonovalova/school_app/issues/30)|As a Receptionist, I want to be able to search for a particular student, so that I can easily access information on this student.|
|[#31](https://github.com/IuliiaKonovalova/school_app/issues/31)|As a Receptionist, I want to be able to see personal information on a kid, so that I can know student’s personal data.|
|[#33](https://github.com/IuliiaKonovalova/school_app/issues/33)|As a Receptionist, I want to be able to see lessons schedule and student attending lessons, so that I can arrange the flow of the students.|
|[#34](https://github.com/IuliiaKonovalova/school_app/issues/34)|As a Receptionist, I want to be able to create lessons for a day (day, time, subject, teachers, students), so that I can provide a precise schedule for school members.|
|[#35](https://github.com/IuliiaKonovalova/school_app/issues/35)|As a Receptionist, I want to be able to render lessons for a day (day, time, subject, teachers, students), so that I can provide up to date schedule.|


#### **Sales Managers' Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#36](https://github.com/IuliiaKonovalova/school_app/issues/36)|As a Sales Manager, I want to be able to search for a particular student, so that I can easily access information on this student.|
|[#37](https://github.com/IuliiaKonovalova/school_app/issues/37)|As a Sales Manager, I want to be able to see personal information on a kid, so that I can know student’s personal data.|
|[#38](https://github.com/IuliiaKonovalova/school_app/issues/38)|As a Sales Manager, I want to be able to sort students by the urgent sale, so that I can control the sales in the company and preserve clients.|
|[#40](https://github.com/IuliiaKonovalova/school_app/issues/40)|As a Sales Manager, I want to be able to view new applications, so that I can contact a potential client and make profits for a company.|
|[#42](https://github.com/IuliiaKonovalova/school_app/issues/42)|As a Sales Manager, I want to be able to add personal notes on each student that I’m in charge of, so that I can increase the company’s sales.|
|[#43](https://github.com/IuliiaKonovalova/school_app/issues/43)|As a Sales Manager, I want to be able to add or edit information on students, so that I can keep up to date students’ profiles.|
|[#44](https://github.com/IuliiaKonovalova/school_app/issues/44)|As a Sales Manager, I want to be able to review my sales, so that I can control my performance.|
|[#45](https://github.com/IuliiaKonovalova/school_app/issues/45)|As a Sales Manager, I want to be able to add new classes to a child when parents buy classes, so that I can maintain relationships with clients.|
|[#52](https://github.com/IuliiaKonovalova/school_app/issues/52)|As a Sales Manager, I want to be able to delete students from the application, so that I can control the flow of the present students.|
|[#53](https://github.com/IuliiaKonovalova/school_app/issues/53)|As a Sales Manager I can edit information on about a sale so that change the data on a sale if a mistake was made or a parent changed his or her mind.|
|[#54](https://github.com/IuliiaKonovalova/school_app/issues/54)|As a Sales Manager I can delete information on about a sale so that render sales data if a mistake was made or a parent changed his or her mind.|
|[#61](https://github.com/IuliiaKonovalova/school_app/issues/61)|As a Sales Manager I want to control my own sales so that nobody else can edit or delete my sales.|
#### **Parents' Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#46](https://github.com/IuliiaKonovalova/school_app/issues/46)|As a Parent, I want to be able to see personal information on my child/children, so that I can check the personal data.|
|[#47](https://github.com/IuliiaKonovalova/school_app/issues/47)|As a Parent, I want to be able to see my child’s attendance (subject, teacher, date), so that I can control my child’s education and my spending.|
|[#48](https://github.com/IuliiaKonovalova/school_app/issues/48)|As a Parent, I want to be able to see lessons schedule, so that I can manage my time and control child’s attendance.|
|[#49](https://github.com/IuliiaKonovalova/school_app/issues/49)|As a Parent, I want to be able to see information on students for each lesson, so that I can prepare my child for a lesson.|
|[#50](https://github.com/IuliiaKonovalova/school_app/issues/50)|As a Parent, I want to be able to see names of teachers for each lesson, so that I can know who is/are teaching a lesson.|

[Back to contents](#contents)

---

## Technologies used

- ### Languages:
    
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): the main language used to develop the server side of the website.
    + [JS](https://www.javascript.com/): the main language used to develop the client side of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [jQuery](https://jquery.com/): was used to control click events and sending AJAX requests.
    + [jQuery User Interface](https://jqueryui.com/) was used to create interactive elements.

- ### Databases:

    + [SQLite](https://www.sqlite.org/): was used as a development database.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Gunicorn](https://gunicorn.org/): the web server used to run the website.
    + [Spycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
    + [GitHub](https://github.com/): used to host the source code of the website.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [Draw.io](https://www.lucidchart.com/) was used to make a flowchart for the README file.
    + [Coolors](https://coolors.co/202a3c-1c2431-181f2a-0b1523-65e2d9-925cef-6b28e0-ffffff-eeeeee) was used to make a color palette for the website.
    + [BGJar](https://www.bgjar.com/): was used to make a background images for the website.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.

[Back to contents](#contents)

---

## Features

Web application has the following pages:
- home page
- login page
- registration page
- logout page
- profile page
- edit profile page
- change password page
- delete member page
- members page
- new applications page
- application detail page
- delete application page
- sales page
- add sale page
- edit sale page
- delete sale page
- students page
- student detail page
- add student page
- edit student page
- delete student page
- schedule page
- lesson page
- add lesson page
- edit lesson page
- delete lesson page
- teacher's personal schedule page

### Access to pages according to the user role:

| Page Name     | Boss  | Teacher    | Sales Manager | Receptionist | Parent | Potential Client |
| ------------- | ------------- | ------------- | ---------- | ------------- | ------------- | ------------- |
| home page                   | Y | Y | Y | Y | Y | Y |
| login page                  | Y | Y | Y | Y | Y | Y |
| registration page           | Y | Y | Y | Y | Y | Y |
| logout page                 | Y | Y | Y | Y | Y | Y |
| user's profile page         | Y | Y | Y | Y | Y | Y |
| other user's profile page   | Y (all data + delete member functionality) | Y (all data except sales made by a sales manager and other teachers' classes) | Y (all data except teachers' classes and other sales managers' sales ) | Y (all data except teachers's classes and sales of the sales managers) | Y (only name, phone number and email) | Y (only name, phone number and email) |
| edit profile page           | Y | Y | Y | Y | Y | Y |
| delete member         | Y | N | N | N | N | N |
| change password page        | Y | Y | Y | Y | Y | Y |
| members page                | Y | Y | Y | Y | N | N |
| new applications page       | Y | N | Y | N | N | N |
| application detail page     | Y (plus assign role and delete application) | N | Y | N | N | N |
| delete application page     | Y | N | N | N | N | N |
| sales page                  | Y | N | Y (plus add sale and edit or delete personal sales only) | N | N | N |
| add sale page               | N | N | Y | N | N | N |
| edit sale page              | N | N | Y | N | N | N |
| delete sale page            | N | N | Y | N | N | N |
| students page               | Y (plus add student button) | Y | Y (plus add student button) | Y | N | N |
| student detail page         | Y (plus delete and edit functionality) | Y | Y (plus delete and edit functionality) | Y | Y (only their own children) | N |
| add student page            | Y | N | Y | N | N | N |
| edit student page           | Y | N | Y | N | N | N |
| delete student page         | Y | N | Y | N | N | N |
| schedule page               | Y | Y (plus view personal schedule functionality) | Y | Y (plus add lesson functionality) | Y | Y |
| lesson page                 | Y | Y | Y | Y | Y (except view other students' profiles) | Y (except view students' profiles functionality) |
| add lesson page             | N | N | N | Y | N | N |
| edit lesson page            | N | N | N | Y | N | N |
| delete lesson page          | N | N | N | Y | N | N |
| teacher's personal schedule page | N | Y | N | N | N | N |

- Each page has a navbar and footer

**Navbar**

![Navbar](documentation/features/navbar/navbar.png)

Navbar has the following links:
- home page
- button "get started", which leads to the registration page and login page
- ![Get Started button](documentation/features/navbar/get_started_button.png)
- It also has a logo of the school
- ![Logo](documentation/features/navbar/main_logo.png)

The simplistic design of the navbar is based on the decision to make the use of the webapp easy for the user.

When the user clicks on the get started button, the menu opens and the user can choose to register or login.

- ![Get Started menu](documentation/features/navbar/navbar_logout.png) 

When the user is logged in, the navbar looks as following.

- ![Navbar User logged in](documentation/features/navbar/navbar_logged_in.png)

It has only one button "Menu", which opens the menu.

- ![Menu Button](documentation/features/navbar/navbar_menu.png)

If the user is a boss or a sales manager, the menu has the following links:

- ![Menu Boss or Manager View](documentation/features/navbar/menu_admin_view.png)

Menu has the following buttons:
- Profile (which leads to the user profile page)
- New applications (which leads to the new applications page)
- Sales (which leads to the sales page)
- Members (which leads to the members page)
- Students (which leads to the students page)
- Schedule (which leads to the schedule page)
- Logout (which leads to the logout page)

If the user is a teacher or receptionist, the menu has the following look:

- ![Menu Teacher or Receptionist View](documentation/features/navbar/menu_receptionists.png)

Menu has the following buttons:
- Profile (which leads to the user profile page)
- Members (which leads to the members page)
- Students (which leads to the students page)
- Schedule (which leads to the schedule page)
- Logout (which leads to the logout page)

if the user is a parent or a potential client, the menu has the following look:

- ![Menu Parent or Potential Client View](documentation/features/navbar/navbar_limited_access.png)

Menu has the following buttons:
- Profile (which leads to the user profile page)
- Schedule (which leads to the schedule page)
- Logout (which leads to the logout page)

**Footer**

![Footer](documentation/features/footer/footer.png)

Footer has the following sections:

- Logo in the top left corner:

  ![Logo](documentation/features/footer/footer_logo.png)

- School information in the middle with the school email, phone number and address:

  ![School Information](documentation/features/footer/footer_school_data.png)

- Information about the coder in the right side with links to the github and linkedin and email:

  ![Coder Information](documentation/features/footer/footer_creator_data.png)


For the mobile version of the website, the footer looks as following:

  ![Footer Mobile](documentation/features/footer/footer_mobile.png)


**Home page**

![Home page](documentation/features/home_page/home_page.png)

Home page has a simple welcome message and a button "get started", which leads to the registration page, from which the user can be redirected to the login page.

- ![Home page Hero section](documentation/features/home_page/home_page_logo_get_started.png)

Under the hero section, there is a section, which describes the benefits of signing up.

- ![Home page Benefits section](documentation/features/home_page/home_page_benefits.png)

This section has 3 cards, each with a title, a description and an image.

On the mobile version, the cards are displayed in two rows.

  ![Home page Benefits section mobile](documentation/features/home_page/home_page_benefits_mobile.png)

After the cards, there are 3 subsections.

1. The first subsection has a text-incentive on the left side and an image on the right side.

  ![Home page First subsection](documentation/features/home_page/home_page_incentive.png)

2. The second subsection has a text describing the schools personnel on the right side and an image on the left side.

  ![Home page Second subsection](documentation/features/home_page/home_page_personnel.png)

3. The third subsection has a text describing the school concern about children health on the left side and an image on the right side.

  ![Home page Third subsection](documentation/features/home_page/home_page_health.png)


After the subsections, there is an immediate contact section, which has an incentive to become a school member right now and a button "get started", which leads to the registration page, from which the user can be redirected to the login page.

  ![Home page Contact section](documentation/features/home_page/home_page_contact_now.png)

**Registration page**

  ![Registration page](documentation/features/register_page/signup_page.png)

This page has a dark-blue container with a sign up form which has a header and input fields for the user to fill in.

In the header of the form, there is a title "Sign up" and a subtitle "Please Fill out all information", which the seriousness of the company towards the user.

  ![Registration page header](documentation/features/register_page/signup_page_header.png)

Underneath, there is a subtitle "Already have an account?." and a button "Login", which leads to the login page.

  ![Registration page header](documentation/features/register_page/signup_page_login.png)

Under the forms's header, there are the following fields:

  ![Registration page fields](documentation/features/register_page/signup_page_fields.png)

These fields are are required for the user to be filled out.
- Email address (to let sales managers and bosses contact the user)
- Username (to let the user have a personal profile)
- First name (to let the user have a personal profile)
- Last name (to let the user have a personal profile)
- Phone number (to let sales managers and bosses contact the user)
- Password (to let the user login)
- Password confirmation (to let the user login)

If the user typed a wrong email address, the email field will be highlighted.

  ![Registration page email field](documentation/features/register_page/signup_page_error_email.png)

If the user left an empty field, the field will be highlighted.

  ![Registration page empty field](documentation/features/register_page/signup_page_error_empty_field.png)

If the user typed a not save password or the confirmation password didn't match, the password field will be highlighted.

  ![Registration page password field](documentation/features/register_page/signup_page_error_password.png)

If the user typed a not save username, the username field will be highlighted.

  ![Registration page username field](documentation/features/register_page/signup_page_error_username.png)

**Login page**

  ![Login page](documentation/features/login_page/login_page.png)

Login Page has a dark-blue container with a login form which has a header and input fields for the user to fill in. Plus it has a button "Sign In" and "Forgot password?", which leads to the forgot password page.

  ![Login page header](documentation/features/login_page/login_page_header.png)

The header has a title "Log in" and a subtitle "If you have not created an account yet, then please sign up first."

When the user clicks on the button, he is redirected to the registration page.

  ![Login page header](documentation/features/login_page/login_page_signup_button.png)

Underneath, there are two fields, which have to be filled out in order to log in:

- Username or email address
- Password

  ![Login page fields](documentation/features/login_page/login_page_fields.png)

If the user made a mistake in the username or password, the field will be highlighted.

  ![Login page error field](documentation/features/login_page/login_page_error.png)

Under the fields, there is a button "Sign in", which leads to the schedule page.

  ![Login page sign in button](documentation/features/login_page/login_page_button.png)

Under this button there is a button "Forgot password?", which leads to the forgot password page.

  ![Login page forgot password button](documentation/features/login_page/login_page_forgot_password.png)

**Logout page**

  ![Logout page](documentation/features/logout_page/logout_page.png)

This page has a dark-blue container with a logout form which has a header and a button "Logout", which leads to the home page.

  ![Logout page header](documentation/features/logout_page/logout_page_box.png)

It has a title "Logout" and a subtitle "Are you sure you want to logout?"
Underneath, there is a button "Sign Out".

  ![Logout page buttons](documentation/features/logout_page/logout_page_signout_button.png)

**Forgot password page**

  ![Reset password page](documentation/features/reset_password_page/reset_password_page.png)

  It has a dark-blue container with a reset password form which has a header and input fields for the user to fill in and a reset button.

  ![Reset password page header](documentation/features/reset_password_page/reset_password_page_box.png)

  The header has a title "Reset Password" and a subtitle, which guide the user what actions should be done in order to regain the access to the user's account.

  ![Reset password page header](documentation/features/reset_password_page/reset_password_page_box_header.png)

  Underneath, there is a fields, where the user can type in his email address.

  ![Reset password page fields](documentation/features/reset_password_page/reset_password_page_field.png)

  If the user typed a wrong email address, the email field will be highlighted.

  Underneath, there is a button "Reset My Password", which leads to the home page. The user will receive an email with a link to reset his password.

  ![Reset password page button](documentation/features/reset_password_page/reset_password_page_button.png)
  
**Profile page**

  ![Profile page](documentation/features/profile_page/profile_page_admin.png)

The Profile Page has a container where the user can see his personal information.

  ![Profile page](documentation/features/profile_page/profile_page_not_admin.png)

It has 2 buttons in top right corner: "Edit" and "Password". The "Edit" button leads to the edit profile page. The "Password" button leads to the change password page.

  ![Profile page buttons](documentation/features/profile_page/edit_password_buttons.png)

If the user is the boss, there is an additional button in the top left corner "Delete".

  ![Profile page buttons](documentation/features/profile_page/profile_page_admin.png)

The button "Delete" leads to the delete profile page.

  ![Profile page buttons](documentation/features/profile_page/profile_page_delete_button.png)

This button has presence for all other profiles that the boss may visit; thus only a boss can delete a profile.

  ![Profile page buttons](documentation/features/profile_page/profile_page_other_user.png)

As a comparison, the profile page of the user that the boss visited on the previous screenshot has no "Delete" button.

  ![Profile page buttons](documentation/features/profile_page/profile_page_not_admin.png)

If the user is a parent, the profile has the following look:

  ![Profile page parent](documentation/features/profile_page/profile_parent.png)

There is an addition field where the parent may assign their relation to a kid as it will be displayed for the school's members.

  ![Profile page parent relation field](documentation/features/profile_page/profile_edit_role.png)

When the user clicks on the button "Edit", the dropdown menu appears, where she or he may choose the relation to their children:

Types of the relation:

- Mother;
- Father;
- Grandmother;
- Grandfather;
- Other.

  ![Profile page edit button](documentation/features/profile_page/profile_role_choice.png)

  After making a choice and clicking save button, the relation will be assigned.

  ![Profile page edit button](documentation/features/profile_page/relation_save.png)

If the user is a teacher, the profile has the following look:

  ![Profile page teacher](documentation/features/profile_page/profile_page_teacher.png)

Underneath the profile box, there is additional data of the classes given to the students.

  ![Profile page teacher classes](documentation/features/profile_page/profile_page_teacher_classes_box.png)

This box is only visible for the teacher and the bosses.

In this box there are datepickers, which allows the teacher or the boss to sort classes during the particular time period.

  ![Profile page teacher classes](documentation/features/profile_page/profile_page_teacher_datepicker.png)

Here the teacher or the boss will be able to pick a data and the summery of the classes will be displayed.


Needless to say, that the pagination functionality has been implemented in case that there are more than 20 classes.

  ![Profile page teacher classes](documentation/features/profile_page/page_navigation1.png)

The buttons for the page navigation have different appearances to guide the user whether there are more classes or not.

  ![Profile page teacher classes](documentation/features/profile_page/page_navigation2.png):

If the user is a Sales Manager, the profile has the following look:

  ![Profile page sales manager](documentation/features/profile_page/profile_page_sales.png)

It has 2 addition sections: Students for which this sales manager is in charge of (visible to all users) and "Sales made" (visible to the sales manager her/himself and the boss)

  ![Profile page sales manager Subsections](documentation/features/profile_page/profile_page_sales_subsections.png)

The "Students" section has a table with the students that this sales manager is in charge of.

  ![Profile page sales manager students](documentation/features/profile_page/profile_page_sales_students.png)

There the Sales manager or the user can see all students. Moreover, the students whose parents should be contacted urgently has an orange label to make them more distinguishable.

  ![Profile page sales manager students](documentation/features/profile_page/profile_page_sales_urgent.png)

Underneath the "Students" section, there is a table with the "Sales made" by the sales manager.

  ![Profile page sales manager sales](documentation/features/profile_page/profile_page_sales_sales.png)

It has a header with the total amount of sales made by the sales manager and a link to the sales page, where the whole statistics stored.

  ![Profile page sales manager sales](documentation/features/profile_page/profile_page_sales_header.png)

Under the header there are recent sales made with limited data (date on which the sale was made and an amount of classes sold). Since the pagination functionality has been implemented, there are only 20 recent sales could be seen and there are 2 buttons for the page navigation at the bottom of the table.

  ![Profile page sales manager sales](documentation/features/profile_page/page_navigation1.png)

**Edit profile page**

  ![Edit profile page](documentation/features/profile_edit_page/profile_edit.png)

It has a container where the user can edit:

- First Name;
- Last Name;
- Phone Number;

There are 3 fields with prefilled data for the user. This data could be changed by the user if he/she wants.

  ![Edit profile page](documentation/features/profile_edit_page/profile_edit_fields.png)

Underneath the fields there are to buttons "Go Back" and "Save". If user doesn't want to save changes, he/she can click on "Go Back" button and will be redirected to the profile page. If user wants to save changes, he/she can click on "Save" button and will be redirected to the profile page.

  ![Edit profile page](documentation/features/profile_edit_page/back_submit_buttons.png)

**Profile Delete Page**

  ![Profile delete page](documentation/features/profile_delete_page/profile_delete.png)

Only the bosses have access to this page as only they are able to delete any profile.

This page has a box with warning message and a link to the profile page of the user that is about to be deleted:
  
  ![Profile delete page](documentation/features/profile_delete_page/member_delete_link.png)

Under the warning message there are 2 buttons "Go Back" and "Delete". If the user doesn't want to delete the profile, he/she can click on "Go Back" button and will be redirected to the profile page. If the user wants to delete the profile, he/she can click on "Delete" button and will be redirected to the profile page and the school member will be permanently deleted.

  ![Profile delete page](documentation/features/profile_delete_page/back_delete_buttons.png)

**Profile Change Password Page**

  ![Profile change password page](documentation/features/profile_change_password_page/profile_password.png)

It has a header with the title "Change Password" and a subtitle to guide the user what to do next. Underneath, there are 3 fieldto be field:

- Old Password;
- New Password;
- Confirm New Password.

  ![Profile change password page](documentation/features/profile_change_password_page/change_password_fields.png)

If there any errors in the fields, the user will see the error message.

Under the fields there are 2 buttons "Go Back" and "Submit". If the user doesn't want to change the password, he/she can click on "Go Back" button and will be redirected to the profile page. If the user wants to change the password, he/she can click on "Change Password" button and will be redirected to the profile page and the password will be change if all conditions were met.

  ![Profile change password page](documentation/features/profile_change_password_page/back_submit_buttons.png)

**New Applications Page**

This page is only visible to the boss and sales manager.
  
![New applications page](documentation/features/new_applications_page/new_applications.png)

This page has a title and the number of the new applications left.

  ![New applications page](documentation/features/new_applications_page/new_applications_summary.png)

It also has a table with the new applications, where each application has a link. After clicking on the application in a table, the user will be redirected to the application detail page.

  ![New applications page](documentation/features/new_applications_page/new_applications_data.png)

Underneath the table, there is navigation buttons. If the user wants to see the next page of the applications, he/she can click on the "Next" button. If the user wants to see the previous page of the applications, he/she can click on the "Previous" button.

  ![New applications page](documentation/features/new_applications_page/page_navigation1.png)
  ![New applications page](documentation/features/new_applications_page/page_navigation2.png)

**Application Detail Page**

This page is accessible to the boss and sales manager.
For the boss, the page has a following look:

  ![Application detail page. Boss View](documentation/features/application_detail_page/application_detail_admin_view.png)

It has 2 boxes. The first box consist the information about the applicant including the name, the email, the phone number.

  ![Application detail page. Applicant Data Box](documentation/features/application_detail_page/application_detail_data.png)

It also has a "Delete" button in the top right corner of the page. If the boss wants to delete the application, he/she can click on the "Delete" button and will be redirected to the delete application page.

  ![Application detail page. Delete Button](documentation/features/application_detail_page/application_detail_delete_button.png)

The second box provides the boss with the assigning role functionality, which will give an access to the applicant to the application according to the role the boss assigns.

  ![Application detail page. Role Assignment Box](documentation/features/application_detail_page/application_detail_role.png)

When the boss click on the dropdown menu, the following choices will be shown:

  ![Application detail page. Role Choices](documentation/features/application_detail_page/application_detail_role_choice.png)

After choosing the role the boss wants to assign, he/she can click on the "Save" button.

  ![Application detail page. Save Role Button](documentation/features/application_detail_page/application_detail_save_role_button.png)

When the boss clicks on "save" button, the role will be assigned to the applicant. However, it will not redirect the boss to any page, in order to prevent the boss from accidentally assigning wrong role to an applicant.

To go back to the applications page, the boss may click on the link underneath the boxes "Go to other applications". And the user will be redirected to the applications page.

  ![Application detail page. Go back to applications](documentation/features/application_detail_page/application_detail_back.png)

For the sales manager, the page has a following look:

  ![Application detail page. Sales Manager View](documentation/features/application_detail_page/application_detail_sale_view.png)

The page has no "Delete" button as it is not accessible to the sales manager. Moreover, the page has no  box with the assigning role to the new applicant as it is accessible only to the boss.

**Application Delete Page**

  ![Application delete page](documentation/features/application_delete_page/application_delete_page.png)

This page is only accessible to the boss. Thus, only boss is empowered to delete any applications.
It has a warning message with the applicant's name.

  ![Application delete page](documentation/features/application_delete_page/application_delete_warning.png)

It also has 2 buttons "Go Back" and "Delete". If the boss doesn't want to delete the application, he/she can click on "Go Back" button and will be redirected to the application detail page. If the boss wants to delete the application, he/she can click on "Delete" button and will be redirected to the new applications page page and the application will be permanently deleted.

  ![Application delete page](documentation/features/application_delete_page/back_delete_buttons.png)

**Limited Access Page**

  ![Limited access page](documentation/features/limited_access_page/limited_access_page.png)

  This page is applicable to the users that are not allowed to access the page that they want to enter manually in the address bar. it has a box with a friendly message, pointing that the user has no access to a particular page. It also has a link to the user's profile page.

  ![Limited access page. Link to Personal Profile](documentation/features/limited_access_page/limit_access_link.png)

**Sales Page**

This page is accessible only by the sales manager and the boss. However, the look of the page is different for the boss and the sales manager as the boss has no access to add, edit or delete sale.

For the sales managers the sales page looks as following:

  ![Sales page](documentation/features/sales_page/sales_page_sales_view.png)

It has a button "Add new sale" in the top right corner of the page. If the sales manager wants to add a new sale, he/she can click on the "Add new sale" button and will be redirected to the add new sale page.

  ![Sales page](documentation/features/sales_page/sales_page_add_sale_button.png)

It has a title "Sales", datepicker sorting bar and a table with the sales.

The sorting bar has 2 datepickers, one for the start date and one for the end date. The sales are sorted by the start date. There is a button "Search" on the right side of the sorting bar. after picking dates and clicking on the "Search" button, the sales will be filtered by the dates.

  ![Sales page](documentation/features/sales_page/datepicker_menu.png)

Under the sorting bar, there is the summary of sales found:

  ![Sales page](documentation/features/sales_page/sales_page_summary.png)

The table has the following columns:

- ID of the sale;
- Date of the sale;
- Total amount of classes sold;
- Manager, who conducted the sale (with the link to the personal profile);
- Client, who bought the classes (with the link to the personal profile);
- Student, for whom the classes were bought (with the link to the personal profile);
- Edit, which will redirect the sales manager to the edit sale page;
- Delete, which will redirect the sales manager to the delete sale page.

  ![Sales page](documentation/features/sales_page/sales_page_edit_delete_limitations.png)

As it is shown in the picture, only the sales manager, who conducted the sale, is able to edit or delete the sale. The user in the picture is Annie Green, and only she is able to edit or delete the sale, which she conducted. She has no access to render or delete the sales made by another Sales Manager, Kate Peterson.

Under the table there is a navigation bar for the table. It has a "Previous" button and a "Next" button. The "Previous" button will redirect the sales manager to the previous page of the table. The "Next" button will redirect the sales manager to the next page of the table.

  ![Sales page](documentation/features/sales_page/page_navigation1.png)
  ![Sales page](documentation/features/sales_page/page_navigation2.png)









[Back to contents](#contents)

---
## Design






### Wireframes

- [Desktop Wireframes](documentation/wireframes/pp4_desktop.pdf)
- [Tablet Wireframes](documentation/wireframes/pp4_tablet.pdf)
- [Mobile Wireframes](documentation/wireframes/pp4_mobile.pdf)

[Back to contents](#contents)

---

## Flowcharts

This application is aimed at users with different roles to fulfill there expectations and provide all functionality.

The following flowcharts were created to help to understand the application and its functionality.

The flowcharts were created using [Draw.io](https://www.lucidchart.com/).

- [Flowchart for Bosses](documentation/flowcharts/flowchart_boss.pdf)
- [Flowchart for Sales Managers](documentation/flowcharts/flowchart_sales.pdf)
- [Flowchart for Parents](documentation/flowcharts/flowchart_parent.pdf)
- [Flowchart for Teachers](documentation/flowcharts/flowchart_teachers.pdf)
- [Flowchart for Receptionist](documentation/flowcharts/flowchart_receptionist.pdf)

[Back to contents](#contents)

---

## Information Architecture

### Database

* During the earliest stages of the project, the database was created using SQLite.
* The database was then migrated to PostgreSQL.

### Entity-Relationship Diagram

* The ERD was created using [Draw.io](https://www.lucidchart.com/).

- [Database Scheme](documentation/diagrams/db_final.pdf)

### Data Modeling

1. **CustomUser**

Extends Allauth's User model.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| UserName      | username      | CharField     |  max_length=50, blank=False, null=True, unique=True    |
| Email         | email         | EmailField    | max_length=50, unique=True, blank=False, null=False    |
| First Name    | first_name    | CharField     | max_length=30, blank=False, null=False    |
| Last Name     | last_name     | CharField     | max_length=30, blank=False, null=False    |
| Phone Number  | email         | CharField     | max_length=30, blank=False, null=False    |
| Role          | phone         | IntegerField  | choices=ROLES, default=5    |


```Python
    # Roles to assign to users
    ROLES = (
        (0, 'boss'),
        (1, 'teacher'),
        (2, 'sales'),
        (3, 'receptionist'),
        (4, 'parent'),
        (5, 'potential user'),
    )
```

2. **Teacher**

Was created in order to provide more room for manipulation of the database and provide opportunities for the future developments. Users with the role of teacher will be automatically assigned to this table.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Teacher       | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |

3. **Receptionist**

Was created in order to provide more room for manipulation of the database and provide opportunities for the future developments.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Receptionist  | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |

4. **SalesManager**

Was created in order to provide more room for manipulation of the database and provide opportunities for the future developments. Users with the role of sales manager will be automatically assigned to this table.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Sales Manager | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |
| Sales Total   | total_sold    | IntegerField  |  default=0, blank=True, null=True  |

5. **Parent**

Was created in order to provide more room for manipulation of the database and provide opportunities for the future developments. Users with the role of parent will be automatically assigned to this table.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Sales Manager | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |
| Relation to a student  | relation      | IntegerField  |  choices=GUARDIAN_RELATION, default=5  |

```Python
    # Guardian's relation to the student
    GUARDIAN_RELATION = (
        (1, 'father'),
        (2, 'mother'),
        (3, 'grandfather'),
        (4, 'grandmother'),
        (5, 'other'),
    )
```
6. **Student**

This table does not inherit from the CustomUser model. This is because the students are not users. Instead, they are the main table of the application.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| First Name         | first_name    | CharField       | max_length=50, blank=False, null=False    |
| Last Name          | last_name     | CharField       | max_length=50, blank=False, null=False    |
| Parents            | parent        | ManyToManyField | Parent, related_name='child'  |
| Birthday           | birthday      | DateField       |          |
| Address            | address       | CharField       | max_length=100, blank=True, null=True |
| Date of enrollment | enrolled      | DateTimeField   | auto_now_add=True    |
| Classes left       | classes_left  | IntegerField    | default=0, blank=True, null=True    |
| Sales Manager      | sales_manager | ManyToManyField | SalesManager, related_name='student'    |
| Notes              | notes         | TextField       | blank=True    |

7. **Sales**

This table is needed to conduct sales operations. It controls the sales of the products. It is also adds classes to a particular student and adds total classes sold to a sales manager. Separate field "student_id" was added in order to prevent a circular import but allow sales to be in control of classes added to a particular student or reduced (For example, when parents asks for a refund).

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Sales Manager | sold_by       | ForeignKey    | SalesManager, on_delete=models.CASCADE, related_name='sold'   |
| Client(Parent)| sold_to       | ForeignKey    | Parent, on_delete=models.CASCADE, related_name='bought'   |
| Classes Number| amount        | IntegerField  |            |
| Date of Sale  | date          | DateTimeField | auto_now_add=True    |
| Student       | amount        | IntegerField  |  default=0          |

8. **Lesson**

This table is necessary to control the lessons and provide data for schedule.

| Name          | Database Key  | Field Type     | Validation |
| ------------- | ------------- | -------------- | ---------- |
| Class's Date  | date          | DateField      |            |
| Class's Time  | time          | IntegerField   | choices=TIME_PERIODS, default=0 |
| Subject       | subject       | IntegerField   | choices=SUBJECTS, default=1     |
| Teachers      | teachers      | ManyToManyField| Teacher, related_name='lessons' |
| Students      | students      | ManyToManyField| Student, related_name='lessons' |


```Python
    # Time periods variations
    TIME_PERIODS = (
        (0, '9:00-9:45'),
        (1, '10:00-10:45'),
        (2, '11:00-11:45'),
        (3, '14:00-14:45'),
        (4, '15:00-15:45'),
        (5, '16:00-16:45'),
        (6, '17:00-17:45'),
        (7, '18:00-18:45'),
    )

    # Subject variations
    SUBJECTS = (
        (1, 'art'),
        (2, 'math'),
        (3, 'casa'),
        (4, 'chinese'),
        (5, 'toddlers'),
        (6, 'music'),
        (7, 'english'),
        (8, 'sport'),
        (9, 'cooking'),
        (10, 'infants'),
    )
```


[Back to contents](#contents)

---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test related documentation.

[Back to contents](#contents)

---

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://issue-tracker-by-konovalovs.herokuapp.com/)
### Local deployment

*Note:*
  - This project requires install all the requirements:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/IuliiaKonovalova/issue_tracker).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/issue_tracker.git`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/IuliiaKonovalova/issue_tracker)

---

1. Install the dependencies:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`

1. Create a .gitignore file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

1. Create a .env file. This will contain the following environment variables:

    ```python
    import os

      os.environ("SECRET_KEY", "Add a secret key")
      os.environ("DATABASE_URL", "will be used to connect to the database")
    ```

1. Run following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.


### Heroku Deployment

1. Set up a local workspace on your computer for Heroku:
    - Create a list of requirements that the project needs to run:
      - type in this in the terminal: `pip3 freeze > requirements.txt`
    - Commit and push the changes to GitHub
    
1. Go to [www.heroku.com](www.heroku.com) 
1. Login or create a Heroku account.
1. Create a new app with any unique name <name app>.
1. Create a Procfile in your local workplace, which will contain the following:
    ```python
        web: gunicorn <name app>.wsgi:application
    ```
    - Commit and push the changes to GitHub.

1. Go to resources in Heroku and search for postgresql. Select Hobby dev - Free and click on the provision button to add it to the project.

1. Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars and add the following config variables:

| Key      | Value          |
|-------------|-------------|
| DATABASE_URL | ... | 
| DISABLE_COLLECTSTATIC | 1 |
| EMAIL_HOST_PASS | ... |
| EMAIL_HOST_USER | ... |
| HEROKU_HOSTNAME | ... |
| SECRET_KEY | ... |


1. Copy the value of DATABASE_URL and input it into the .env file.
1. Create EMAIL_HOST_PASS and EMAIL_HOST_USER with gmail account and add values to these keys.
1. Migrate changes.
1. Set debug to False in settings.py
1. Commit and push the changes to GitHub.


[Back to contents](#contents)

---



