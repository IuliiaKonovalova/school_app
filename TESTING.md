# Testing

## Manual Testing

Testing was done throughout site development, for each feature before it was merged into the master file.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.


|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up     |                        |                  |      |             |
| 1           | Click on the Get started button | Dropdown menu with 2 options: Login/SignUp | Y |          |
| 2           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 3           | Click Get Started button in the hero section | Redirection to Sign Up page | Y |          |
| 4           | Click on the Login link in the form | Redirection to Login page | Y |          |
| 5           | Enter valid email | Field will only accept email address format | Y |          |
| 6           | Enter valid username | Field will only accept no more than 50 characters | Y |          |
| 7           | Enter valid First Name | Field will only accept no more than 30 characters | Y |          |
| 8           | Enter valid Last Name | Field will only accept no more than 30 characters | Y |          |
| 9           | Enter valid phone number | Field will only accept no more than 30 characters | Y |          |
| 10          | Enter valid password | Field will only accept secure passwords | Y |          |
| 11          | Enter valid password confirmation | Field will only accept the same password from the previous field | Y |          |
| 12          | Click on the Sign Up button | Takes user to confirm email page Sends address a confirmation request email | Y |          |
| 13          | Confirm email | Redirects user to blank Sign In page | Y |          |
| 14          | Sign In with the same email/username and password | Takes user to schedule page with pop-up confirming successful sign in. Get started button now missing in main nav, replaced by Menu | Y |          |
| 15          | Click "Menu", choose "Logout" | Takes user to log out page to confirm logout | Y |          |
| 16          | Click "Logout" button  in the center of the page| Redirects user to home page | Y |          |
| 17          | Click browser back button | You are still logged out | Y |          |
| Log In      |                        |                  |      |             |
| 1           | Click on the Get started button | Dropdown menu with 2 options: Login/SignUp | Y |          |
| 2           | Click on Login button | Redirection to Login page | Y |          |
| 3           | Click on the SignUp link in the form | Redirection to SignUp page | Y |          |
| 4           | Enter valid email or username | Field will only accept email address format | Y |          |
| 5           | Enter valid password | Field will only accept secure passwords | Y |          |
| 6           | Click on the Sign In button | Takes user to schedule page with pop-up confirming successful sign in. Get started button now missing in main nav, replaced by Menu | Y |          |
| 7           | Clicks "Forgot Password" instead of "Sign In" | Redirects user to forgot password page | Y |          |
| 8           | Click "Menu", choose "Logout" | Takes user to log out page to confirm logout | Y |          |
| 9           | Click "Logout" button  in the center of the page| Redirects user to home page | Y |          |
| 10          | Click browser back button | You are still logged out | Y |          |
| Menu        |                        |                  |      |             |
| 1           | Click on the "Menu" button | Dropdown menu with 2-7 options depending on the user's role | Y | Available to everyone |
| 2           | Click on "Profile" | Redirection to My Profile page | Y | Available to everyone |
| 3           | Click on "New Applications" | Redirection to New Applications page | Y | Available only to bosses and sales managers |
| 4           | Click on "Sales" | Redirection to Sales page | Y | Available only to bosses and sales managers |
| 5           | Click on "Members" | Redirection to Members page | Y | Available only to school personnel |
| 6           | Click on "Students" | Redirection to Students page | Y |  Available only to school personnel |
| 7           | Click on "Schedule" | Redirection to Schedule page | Y | Available to everyone |
| 2           | Click on "Logout" button in the center of the page | Takes user to log out page to confirm logout | Y | Available to everyone |
| Profile     |            |                  |      |             |
| 1           |  Click "delete" button | Redirect to delete profile page | Y | Available only to bosses  |
| 2           |  Click "edit" button | Redirect to edit profile page | Y |  Available only when the user opens his/her own profile  |
| 3           |  Click "password" button | Takes user to change password page to confirm logout | Y |  Available only when the user opens his/her own profile |
| 4           |  Click "child's name" button | Takes user to change email page to confirm logout | Y | Available only to the parents whose kids are saved in the school system |
| 5           |  Click "edit" button in the relation section | Opens dropdown menu with options: mother, father, grandmother, grandfather, other | Y | Available only to the parents whose kids are saved in the school system |
| 6           |  Click on the particular relation | dropdown menu closes and only chosen relation is seen | Y | Available only to the parents whose kids are saved in the school system |
| 7           |  Click "save" button in the relation section | relation is updated | Y | Available only to the parents whose kids are saved in the school system |
| 8           |  Click "from date calendar" input classes section | calendar picker appear | Y | Available only to the teacher in his/her own profile and the bosses, when the boss enters teacher's profile |
| 9           |  Click "to date calendar" input classes section | calendar picker appear | Y | Available only to the teacher in his/her own profile and the bosses, when the boss enters teacher's profile |
| 10          |  Click "search" button in the classes section when the dates are set | classes are selected | Y | Available only to the teacher in his/her own profile and the bosses, when the boss enters teacher's profile |
| 11          |  Click "class" button in the classes section | redirected to the lesson detail page | Y | Available only to the teacher in his/her own profile and the bosses, when the boss enters teacher's profile |
| 12          |  Click "from date calendar" input sales section | calendar picker appear | Y | Available only to the sales managers in his/her own profile and the bosses, when the boss enters sale mangers's profile |
| 13          |  Click "to date calendar" input sales section | calendar picker appear | Y | Available only to the sales managers in his/her own profile and the bosses, when the boss enters sale mangers's profile |
| 14          |  Click "search" button in the sales section when the dates are set | sales are selected | Y | Available only to the sales managers in his/her own profile and the bosses, when the boss enters sale mangers's profile |
| 15          |  Click "sales" button in the sales section | redirected to the sales detail page | Y | Available only to the sales managers in his/her own profile and the bosses, when the boss enters sale mangers's profile |
| 16          |  Click "student name" button | redirect to the student's profile | Y | Available only to everyone in sales manager profile but parents/potential clients may enter only their own children's profiles|
 17           | Click page navigation buttons | additional sales/classes results will be uploaded | Y | For classes accessible only by the school personnel | 
|Delete Profile |            |                  |      |             |
| 1           |  Click "user name" link | Redirect to the user profile that is about to be deleted | Y | Available only to bosses  |
| 2           |  Click "cancel" button | Redirect back to user profile | Y | Available only to bosses  |
| 3           |  Click "delete" button | Redirect to members page+the user will be deleted from the database | Y | Available only to bosses  |
| Edit Profile |            |                  |      |             |
| 1           |  Change the form data for the first name, last name, or phone number | Date in the form will be updated | Y | Available only when the user opens his/her own profile  |
| 2           |  Click "cancel" button | Redirect back to user profile | Y |  Available only when the user opens his/her own profile |
| 3           |  Click "save" button | Redirect back to user profile+data will be updated in the database | Y |  Available only when the user opens his/her own profile |
| Change Password |            |                  |      |             |
|1                | Enter valid current password | Field will only accept secure passwords | Y |  Available only when the user opens his/her own profile |
|2                | Enter valid new password | Field will only accept secure passwords | Y |  Available only when the user opens his/her own profile |
|3                | Enter valid new password confirmation | Field will only accept the same password from the previous field | Y |  Available only when the user opens his/her own profile |
|4                | Click "cancel" button | Redirect back to user profile | Y |  Available only when the user opens his/her own profile |
|5                | Click "save" button | Redirect back to user profile+password will be updated | Y |  Available only when the user opens his/her own profile |
| New Applications |     |      |     |    |
| 1                | click on a new application button | Redirect to the application detail page | Y | Available only to bosses and sales managers |
| 2                | page navigation "next" | Redirect to the next page of applications | Y | Available only to bosses and sales managers |
| 3                | page navigation "previous" | Redirect to the previous page of applications | Y | Available only to bosses and sales managers |
| Application Detail |     |      |     |    |
| 1                | click on "delete" button | Redirect to the application detail page+application will be accepted | Y | Available only to bosses |
| 2                | click dropdown menu "potential user" | dropdown menu with user's roles appear | Y | Available only to bosses |
| 3                | click on the particular role | dropdown menu closes and only chosen role is seen | Y | Available only to bosses |
| 4                | click on "accept" button | Redirect to the application detail page+application will be accepted and role will be assigned | Y | Available save to bosses |
| 5                | click on "Go to other application" button | Redirect to the new applications | Y | Available only to bosses and sales managers |
| Sales            |     |      |     |    |
| 1                | click on an "add new sale" button | Redirect to the sales detail page | Y | Available only to sales managers |
| 2                | click on the "from date calendar" input | calendar picker appear | Y | Available only to sales managers and bosses|
| 3                | click on the "to date calendar" input | calendar picker appear | Y | Available only to sales managers and bosses|
| 4                | click on the "search" button | sales are selected | Y | Available only to sales managers and bosses|
| 5                | click on the "sales manager name" button | redirect to the sales manager's profile | Y | Available only to sales managers and bosses|
| 6                | click on the "client name" button | redirect to the client's profile | Y | Available only to sales managers and bosses|
| 7                | click on the "student name" button | redirect to the student's profile | Y | Available only to sales managers and bosses|
| 8                | click on the "edit" button | redirect to the edit sale page | Y | Available only to sales managers, who conducted this sale |
| 9                | click on the "cancel" button | redirect to the sales detail page | Y | Available only to sales managers, who conducted this sale |
| Add Sale         |     |      |     |    |
| 1                | click on the "Client Name" input | dropdown menu with clients appear | Y | Available only to sales managers |
| 2                | click on the "Amount" input | number of classes is available for the input | Y | Available only to sales managers |
| 3                | click on the "Student" input | dropdown menu with students appear | Y | Available only to sales managers |
| 4                | click on the "Cancel" button | redirect to the sales page | Y | Available only to sales managers |
| 5                | click on the "Save" button | redirect to the sales page+sale will be added to the database | Y | Available only to sales managers |
| Edit Sale        |     |      |     |    |
| 1                | click on the "Client Name" input | dropdown menu with clients appear | Y | Available only to sales managers, who conducted this sale |
| 2                | click on the "Amount" input | number of classes is available for the input | Y | Available only to sales managers, who conducted this sale |
| 3                | click on the "Student" input | dropdown menu with students appear | Y | Available only to sales managers, who conducted this sale |
| 4                | click on the "Cancel" button | redirect to the sales page | Y | Available only to sales managers, who conducted this sale |
| 5                | click on the "Save" button | redirect to the sales page+sale will be updated in the database | Y | Available only to sales managers, who conducted this sale |
| Delete Sale      |     |      |     |    |
| 1                | click on the "cancel" button | redirect to the sales page | Y | Available only to sales managers, who conducted this sale |
| 2                | click on the "delete" button | redirect to the sales page+sale will be deleted from the database | Y | Available only to sales managers, who conducted this sale |
| Members          |     |      |     |    |
| 1                | click on the "All members" button + "search" button | all members are displayed | Y | Available only to school staff |
| 2                | click on the "Parents" button + "search" button | only parents are displayed | Y | Available only to school staff |
| 3                | click on the "Teachers" button + "search" button | only teachers are displayed | Y | Available only to school staff |
| 4                | click on the "Sales Managers" button + "search" button | only sales managers are displayed | Y | Available only to school staff |
| 5                | click on the "Receptionists" button + "search" button | only Receptionists are displayed | Y | Available only to school staff |
| 6                | type name in the "search" input | only members with the name are displayed+undo button will appear in the search input | Y | Available only to school staff |
| 7                | click on the "undo" button | all members are displayed | Y | Available only to school staff |
| 8                | click on the "member" box | redirect to member's profile | Y | Available only to school staff |
| 9                | click on the "next" navigation button | redirect to the next page of members | Y | Available only to school staff |
| 10               | click on the "previous" navigation button | redirect to the previous page of members | Y | Available only to school staff |
| Students         |     |      |     |    |
| 1                | type name in the "search" input | only students with the name are displayed+undo button will appear in the search input | Y | Available only to school staff |
| 2                | click on the "undo" button | all students are displayed | Y | Available only to school staff |
| 3                | click on the "All students" button + "search" button | all students are displayed | Y | Available only to school staff |
| 4                | click on the "Urgent Call" button + "search" button | only urgent call students are displayed | Y | Available only to school staff |
| 5                | click on the "student" box | redirect to student's profile | Y | Available only to school staff |
| 6                | click on the "next" navigation button | redirect to the next page of students | Y | Available only to school staff |
| 7                | click on the "previous" navigation button | redirect to the previous page of students | Y | Available only to school staff |
| Add Student      |     |      |     |    |
| 1                | type student's first name in the "first name" input | student's first name is available for the input | Y | Available only to sales managers and bosses |
| 2                | type student's last name in the "last name" input | student's last name is available for the input | Y | Available only to sales managers and bosses |
| 3                | click on the "parents" dropdown menu | dropdown menu with parents' names appear | Y | Available only to sales managers and bosses |
| 4                | click on the parent's name in the "parents" dropdown menu | parent's name is selected | Y | Available only to sales managers and bosses |
| 5                | click on the birthday calendar input | calendar picker appear | Y | Available only to sales managers and bosses |
| 6                | type student's address in the "address" input | student's address is available for the input | Y | Available only to sales managers and bosses |
| 7                | change the number of classes in the "number of classes" input | number of classes is available for the input | Y | Available only to sales managers and bosses |
| 8                | click on the "sales manager" dropdown menu | dropdown menu with sales managers' names appear | Y | Available only to sales managers and bosses |
| 9                | type notes in the "notes" input | notes are available for the input | Y | Available only to sales managers and bosses |
| 10               | click on the "cancel" button | redirect to the students page | Y | Available only to sales managers and bosses |
| 11               | click on the "save" button | redirect to the students page+student will be added to the database | Y | Available only to sales managers and bosses |
| Edit Student     |     |      |     |    |
| 1                | render student's first name in the "first name" input | student's first name is available for the input | Y | Available only to sales managers and bosses, who conducted this sale |
| 2                | render student's last name in the "last name" input | student's last name is available for the input | Y | Available only to sales managers and bosses, who conducted this sale |
| 3                | render the "parents" dropdown menu | dropdown menu with parents' names appear | Y | Available only to sales managers and bosses, who conducted this sale |
| 4                | render the parent's name in the "parents" dropdown menu | parent's name is selected | Y | Available only to sales managers and bosses, who conducted this sale |
| 5                | render the birthday calendar input | calendar picker appear | Y | Available only to sales managers and bosses, who conducted this sale |
| 6                | render student's address in the "address" input | student's address is available for the input | Y | Available only to sales managers and bosses, who conducted this sale |
| 7                | render the number of classes in the "number of classes" input | number of classes is available for the input | Y | Available only to sales managers and bosses, who conducted this sale |
| 8                | render the "sales manager" dropdown menu | dropdown menu with sales managers' names appear | Y | Available only to sales managers and bosses, who conducted this sale |
| 9                | render notes in the "notes" input | notes are available for the input | Y | Available only to sales managers and bosses, who conducted this sale |
| 10               | click on the "cancel" button | redirect to the student detail page | Y | Available only to sales managers and bosses, who conducted this sale |
| 11               | click on the "save" button | redirect to the student detail page+student will be updated in the database | Y | Available only to sales managers and bosses, who conducted this sale |
| Delete Student   |     |      |     |    |
| 1                | click on the "student's name" box | redirect to student's profile | Y | Available only to sales managers and bosses, who conducted this sale |
| 2                | click on the "cancel" button | redirect to the student detail page | Y | Available only to sales managers and bosses, who conducted this sale |
| 3                | click on the "delete" button | redirect to the students page+student will be deleted from the database | Y | Available only to sales managers and bosses, who conducted this sale |
| Student detail   |     |      |     |    |
| 1                | click on the "edit" button | redirect to the edit student page | Y | Available only to sales managers and bosses |
| 2                | click on the "delete" button | redirect to the students page+student will be deleted from the database | Y | Available only to sales managers and bosses |
| 3                | click on the "parent name" button | redirect to the parent's profile | Y | Available only to sales managers and bosses |
| 4                | click on the "sales manager name" button | redirect to the sales manager's profile | Y | Available only to sales managers and bosses |
| 5                | click on "from" calendar input | calendar picker appear | Y | Available only to sales managers and bosses |
| 6                | click on "to" calendar input | calendar picker appear | Y | Available only to sales managers and bosses |
| 7                | click on the "Search" button when the search input is filled | only classes with the subject's names and dates are displayed | Y | Available only to school staff and child's parents |
| 8                | click on the "class" box | redirect to class's profile | Y | Available only to school staff and child's parents |
| 9                | click on the "next" navigation button | redirect to the next page of classes | Y | Available only to school staff and child's parents |
| 10               | click on the "previous" navigation button | redirect to the previous page of classes | Y | Available only to school staff and child's parents |
| Schedule         |     |      |     |    |
| 1                | click on the "add lesson" button | redirect to the add class page | Y | Available only to receptionists |
| 2                | click on the "my schedule" button | redirect to the schedule page for a teacher , which in the session | Y | Available only to teachers |
| 3                | click on the "date" box | calendar picker appear | Y | Available only to teachers |
| 4                | click on the "subject" box | redirect to lesson's detail | Y | Available only to teachers |
| Teacher Schedule    |     |      |     |    |
| 1                | click on the "back" button | redirect to the schedule page | Y | Available only to teacher, who is in session |
| 2                | click on the "subject" box | redirect to lesson's detail | Y | Available only to teachers |
| Lesson detail    |     |      |     |    |
| 1                | click on the "edit" button | redirect to the edit lesson page | Y | Available only to receptionists |
| 2                | click on the "delete" button | redirect to the schedule page+lesson will be deleted from the database | Y | Available only to receptionists |
| 3                | click on the "teacher" button | redirect to the teacher's profile | Y | Available only to everyone |
| 4                | click on the "student" button | redirect to the student's profile | Y | Available only to school staff and parents whose child is |
| Add Lesson       |     |      |     |    |
| 1                | click on the "Date" box | calendar picker appear | Y | Available only to receptionists |
| 2                | click on the "Time Period" dropdown menu | dropdown menu with time periods appear | Y | Available only to receptionists |
| 3               | click on the time in the dropdown menu | time is selected | Y | Available only to receptionists |
| 4                | click on the "Subject" dropdown menu | dropdown menu with subjects appear | Y | Available only to receptionists |
| 5                | click on the subject in the dropdown menu | subject is selected | Y | Available only to receptionists |
| 6                | click on the "Teacher" dropdown menu | dropdown menu with teachers appear | Y | Available only to receptionists |
| 7                | click on the teacher in the dropdown menu | teacher is selected | Y | Available only to receptionists |
| 8                | click on the "Students" dropdown menu | dropdown menu with students appear | Y | Available only to receptionists |
| 9                | click on the student in the dropdown menu | student is selected | Y | Available only to receptionists |
| 10               | click on the "save" button | redirect to the schedule page+lesson will be added to the database | Y | Available only to receptionists |
| 11               | click on the "cancel" button | redirect to the schedule page | Y | Available only to receptionists |
| Edit Lesson      |     |      |     |    |
| 1                | render the "Date" box | calendar picker appear | Y | Available only to receptionists |
| 2                | render the "Time Period" dropdown menu | dropdown menu with time periods appear | Y | Available only to receptionists |
| 3               | render the time in the dropdown menu | time is selected | Y | Available only to receptionists |
| 4                | render the "Subject" dropdown menu | dropdown menu with subjects appear | Y | Available only to receptionists |
| 5                | render the subject in the dropdown menu | subject is selected | Y | Available only to receptionists |
| 6                | render the "Teacher" dropdown menu | dropdown menu with teachers appear | Y | Available only to receptionists |
| 7                | render the teacher in the dropdown menu | teacher is selected | Y | Available only to receptionists |
| 8                | render the "Students" dropdown menu | dropdown menu with students appear | Y | Available only to receptionists |
| 9                | render the student in the dropdown menu | student is selected | Y | Available only to receptionists |
| 10               | click on the "save" button | redirect to the schedule page+lesson will be updated in the database | Y | Available only to receptionists |
| 11               | click on the "cancel" button | redirect to the schedule page | Y | Available only to receptionists |
| Delete Lesson    |     |      |     |    |
| 1                | click on the "Lesson" box | redirect to lesson's detail | Y | Available only to receptionists |
| 2                | click on the "delete" button | redirect to the schedule page+lesson will be deleted from the database | Y | Available only to receptionists |
| 3                | click on the "cancel" button | redirect to the schedule page | Y | Available only to receptionists |

##  Testing User Story

| First Time Visitor Goals | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a First Time Visitor, I want to be able to easily understand the main purpose of the app, so that I can learn more about this app. | Welcome text on the top of the homepage explaining the main purpose of the website and describing the the services offered | ![Home page](documentation/features/home_page/home_page.png) |
| As a First Time Visitor, I want to be able to easily navigate through the app, so that I can find the content. | The website for the fist time visitors made out of one page. The user can read all benefits of the school and learn briefly about its services. The page has also several buttons, which lead to the registration page. At the end of the page, the user may find additional contact information and location of the school. | ![Menu](documentation/features/navbar/menu_admin_view.png) |
| As a First Time Visitor, I want to be able to register my account, so that I can learn the benefits of the app as a user. | Top navigation GET STARTED button + GET STARTED button in the hero section | ![Navbar Logout](documentation/features/navbar/navbar_logout.png) |
| As a First Time Visitor, I want to be able to find the app useful, so that I can use it according to my needs. | The website cover benefits of becoming a member and engages new visitors to become a member of a school | go to features section in the [README.md](README.md) |


| Frequent Visitor Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Frequent User, I want to be able to log in to my account, so that I can have a personal account. | Log in from the top right navigation | ![Get Started Button](documentation/features/navbar/get_started_button.png) |
| As a Frequent User, I want to be able to easily log in and log out, so that I can access my personal account information. | Logout button in the main menu in the top of navbar | ![Navbar limited access](documentation/features/navbar/navbar_limited_access.png) |
| As a Frequent User, I want to be able to easily recover my password in case I forget it, so that I can recover access to my account. | Available on login page | ![Login](documentation/features/login_page/login_page.png) |
| As a Frequent User, I can be able to change my password, so that I can be sure that nobody else can access my account. | Available in user’s profile | ![Profile. Admin view](documentation/features/profile_page/profile_page_admin_box.png) |

| Potential Client Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Potential client, I want to be contacted by sales managers, so that I can make a prudent decision about being a member. | Sales Manager will be able to get contact information from a potential client in new application page in order to contact new user | ![New Application. Data](documentation/features/application_detail_page/application_detail_data.png) |

| Bosses' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Boss, I want to be able to view new applications, so that I can control the flow of potential clients. | Available in new application page | ![New Applications. Data](documentation/features/new_applications_page/new_applications_data.png) |
| As a Boss, I want to be able to delete or approve membership, assign a role to a new member, so that I can keep data up to date. | Available in new application detail page | ![Assigning role to new application](documentation/features/application_detail_page/application_detail_role.png) |
| As a Boss, I want to be able to add, edit data on a kid, so that I can have a profile for each student. | Add student button is available on students page, students personal info is seen after clicking on a particular student. Edit button is located in student’s profile page. | ![Student Detail. Admin View](documentation/features/student_detail_page/student_detail_page_admin_view.png) |
| As a Boss, I want to be able to delete a member, so that I can control the access to the application. | Available in user’s profile only for bosses | ![Profile View. Deletion](documentation/features/profile_page/profile_page_other_user.png) |
| As a Boss I can see the info about kids provided by the company: name, contact info, classes visited, how many classes left, so that refresh the information about a client. | Available on students page, students personal info is seen after clicking on a particular student | ![Data about a student](documentation/features/student_detail_page/student_detail_page_admin_view.png) |
| As a Boss, I want to be able to search for a particular member, so that I can easily access information on this member. | Available in members page | ![Members search](documentation/features/members_page/members_page_search_input_results.png) |
| As a Boss, I want to be able to sort members according to a role, so that I can easily access particular group of members. | Available in members page | ![Members sorting bar](documentation/features/members_page/members_page_sorting_bar.png) |
| As a Boss, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Students. Search input](documentation/features/students_page/students_page_search_input.png) |
| As a Boss, I want to be able to sort students by the urgent sale, so that I can control the sales in the company and preserve clients. | Available in students page | ![Students. Sort Bar](documentation/features/students_page/students_page_sort.png) |
| As a Boss, I want to be able to see lessons schedule, so that I can schedule time to talk to a teacher or a parent. | Available in schedule page | ![Schedule table](documentation/features/schedule_page/schedule_page_box.png) |
| As a Boss, I want to see see information on students for each lesson, so that I can control students’ attendance, learn clients preferences. | Available in schedule page, after clicking on a lesson | ![Lesson detail](documentation/features/lesson_detail_page/lesson_detail_personnel.png) |
| As a Boss, I want to be able to see sales' details, so that I can check which sales manager and which parent was involved in a deal. | Available in sales page | ![Menu](documentation/features/sales_page/sales_table_admin_view.png) |
| As a Boss, I want to be able to delete students from the application, so that I can control the flow of the present students. | Available on students page, student delete button is seen after clicking on a particular student. | ![Student deletion](documentation/features/student_detail_page/student_detail_page_data_box.png) |

| Teachers' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Teacher, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Students. Search Input](documentation/features/students_page/students_page_search_input.png) |
| As a Teacher, I want to be able to see personal information on a kid, so that I can know student’s personal data. |  students personal info is seen after clicking on a particular student. | ![Student. Data](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Teacher, I want to be able to see lessons schedule, so that I can manage my time. | Available in schedule page | ![Schedule](documentation/features/teacher_schedule_page/schedule_look_compare2.png) |
| As a Teacher, I want to be able to see information on students for each lesson, so that I can be prepared for each student. | Available in schedule page, after clicking on a lesson | ![Lesson detail](documentation/features/lesson_detail_page/lesson_detail_personnel.png) |

| Receptionists' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Receptionist, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Student. Search input](documentation/features/students_page/students_page_search_input.png) |
| As a Receptionist, I want to be able to see personal information on a kid, so that I can know student’s personal data. |  students personal info is seen after clicking on a particular student. | ![Menu](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Receptionist, I want to be able to see lessons schedule and student attending lessons, so that I can arrange the flow of the students. | Available in schedule page | ![Schedule](documentation/features/schedule_page/schedule_page_box.png) |
| As a Receptionist, I want to be able to create lessons for a day (day, time, subject, teachers, students), so that I can provide a precise schedule for school members. | Add lesson button is available in schedule page | ![Add lesson button](documentation/features/schedule_page/add_lesson_button.png) |
| As a Receptionist, I want to be able to render lessons for a day (day, time, subject, teachers, students), so that I can provide up to date schedule. | Edit and delete lesson buttons are available after clicking on a lesson in schedule page | ![Lesson Detail. Editing and Deletion](documentation/features/lesson_detail_page/lesson_detail_receptionist.png) |

| Sales Managers' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Sales Manager, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Student. Search Input](documentation/features/students_page/students_page_search_input.png) |
| As a Sales Manager, I want to be able to see personal information on a kid, so that I can know student’s personal data. |  students personal info is seen after clicking on a particular student. | ![Menu](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Sales Manager, I want to be able to sort students by the urgent sale, so that I can control the sales in the company and preserve clients. | Available in students page | ![Student. Search Input](documentation/features/students_page/students_page_sort.png) |
| As a Sales Manager, I want to be able to view new applications, so that I can contact a potential client and make profits for a company. | Available in the new applications page | ![New Application Data](documentation/features/new_applications_page/new_applications_data.png) |
| As a Sales Manager, I want to be able to add personal notes on each student that I’m in charge of, so that I can increase the company’s sales. | Available in the students page | ![Add student Page](documentation/features/add_student_page/add_student_page.png) |
| As a Sales Manager, I want to be able to add or edit information on students, so that I can keep up to date students’ profiles. | Available in the students page | ![Student Detail. Data](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Sales Manager, I want to be able to review my sales, so that I can control my performance. | Available in the sales manager personal profile | ![Sales for sales manager in Profile](documentation/features/profile_page/profile_page_sales_sales.png) |
| As a Sales Manager, I want to be able to add new classes to a child when parents buy classes, so that I can maintain relationships with clients. | Available in the sales page | ![Add sale button](documentation/features/sales_page/sales_page_add_sale_button.png) |
| As a Sales Manager, I want to be able to delete students from the application, so that I can control the flow of the present students. | Available on students page, student delete button is seen after clicking on a particular student. | ![Student Detail. Data](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Sales Manager I can edit information on about a sale so that change the data on a sale if a mistake was made or a parent changed his or her mind. | Available on sales page | ![Sales deletion and edition](documentation/features/sales_page/sales_page_edit_delete_limitations.png) |
| As a Sales Manager I can delete information on about a sale so that render sales data if a mistake was made or a parent changed his or her mind. | Available on sales page | ![Delete sale page](documentation/features/delete_sale_page/delete_sale_page.png) |

| Parents' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Parent, I want to be able to see personal information on my child/children, so that I can check the personal data. | Available in student detail page | ![Student Detail. Other members view](documentation/features/student_detail_page/student_detail_page_others_view.png) |
| As a Parent, I want to be able to see my child’s attendance (subject, teacher, date), so that I can control my child’s education and my spending. | Available in student detail page | ![Menu](documentation/features/student_detail_page/student_detail_attendance.png) |
| As a Parent, I want to be able to see lessons schedule, so that I can manage my time and control child’s attendance. | Available in schedule page | ![Schedule](documentation/features/schedule_page/schedule_page_box.png) |
| As a Parent, I want to be able to see information on students for each lesson, so that I can prepare my child for a lesson. | Available in schedule page, after clicking on a lesson | ![Lesson detail for parents](documentation/features/lesson_detail_page/lesson_detail_parent.png) |
| As a Parent, I want to be able to see names of teachers for each lesson, so that I can know who is/are teaching a lesson. | Available in schedule page, after clicking on a lesson | ![Lesson Detail Parent](documentation/features/lesson_detail_page/lesson_detail_parent.png) |

---


## Bugs

### Known bugs:

When the parent, who has 2 or more children, assigns a relation to a child, the relation could be assign only to one child.

![Lessons Testing Coverage](documentation/bugs/roles_bug1.png)
![Lessons Testing Coverage](documentation/bugs/roles_bug2.png)

However, when the user refreshes the page all children are shown with the correct relation.

![Lessons Testing Coverage](documentation/bugs/roles_bug4.png)

### Solved bugs:

There were plenty of bugs during the development process since this project was a learning platform for me and allowed me to improve my skills and knowledge significantly.

However, I tried to solve the majority of them. And one of the bugs that I remember perfectly was related to the extension of the allauth sign up form. I was able to solve it by customizing the allauth sign up form. Moreover, I encountered the problem of making the form work as the migrations were not working. What I have done to migrate the changes is to migrate the profile app first and then perform the rest of the migrations.

Another bug that took me a lot of time to solve was avoiding circular import when I was developing a sales app, as I needed to get not only the client data but also the children's data to add or delete classes from students' profiles. The solution to this problem was to implement the student_id field that will be used to get the children's data and store it in the sales table.
## Automated testing

### Django unit testing

As there are four main apps in the project, we can test them separately.
I knew at the very beginning that I had to implement automated testing. As I was highly concentrated on developing all functionality first, so I left testing to the end. While testing my work, I found several bugs related to the access limited to particular pages and functionality for different roles. In the future, I plan to implement testing and code simultaneously in order to increase my productivity.

**Lessons App**

![Lessons Testing Coverage](documentation/test_reports/lessons_report_testing.png)

**Profiles App**

![Profiles Testing Coverage](documentation/test_reports/profiles_report_testing.png)

**Sales App**

![Sales Testing Coverage](documentation/test_reports/sale_report_testing.png)

**Students App**

![Students Testing Coverage](documentation/test_reports/students_report_testing.png)

To run testing, the database must be set to sqlite3.

![Testing Database](documentation/test_reports/testing_preparation.png)

Thus, you need to comment out the PostgreSQL database settings in the settings.py file and uncomment the sqlite3 database settings.

I set tests folder for each app separately. I also deleted the test.py files from the apps.

![Testing Folders](documentation/test_reports/tests_folder.png)

While developing tests I was running the following command:

```
python manage.py test <name of the app>
```

To create the coverage report, I ran the following command:

```
coverage run --source=<name of the app> manage.py test
```
```
coverage report
```
To see the html version of the report, I ran the following command:

```
coverage html
```
```
    python3 -m http.server
```
The link to the server will appear. Click the link to see the report and find out which parts of code has not been covered in testing.

### Jest unit testing

I wasn't able to run proper test for the javascript files. I was able to run the tests for the files in the js folder. However, as I was using modern js and target events in my code, jest was not able to run the tests. 

![Testing Javascript](documentation/test_reports/jest_error.png)

To perform the tests, I created a separate folder outside of the project, where I changed the code to suit the jest standards:

```JavaScript
  if (studentSearchInput) {
    studentSearchInput.addEventListener("keyup", searchStudent);
  }
  if (memberSearchInput) {
    memberSearchInput.addEventListener("keyup", searchMembers);
  }
```

After these changes I was able to run the tests and see the coverage report.

To run the jest tests, I ran the following command:

```
npm init
```
skipped all fields except for the "test command"

```
test: command: jest
```
and confirmed the package.json file.

after that, I run the following command to install jest:


```
npm install --save-dev jest
```
To run test, simply type the following command:

```
npm test
```

![Testing Javascript](documentation/test_reports/jest_error_solved.png)


## Validation:
### HTML Validation:

- [Full HTML Validation](documentation/validation/html_validation.pdf)

- No errors or warnings were found when passing through the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying view page source code (Ctrl+U) and pasting it into the validator.

### CSS Validation:

- [Full CSS Validation](documentation/validation/css_validation.png)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator except the warnings about the use of css root variables and webkits for the box-shadow. However, css code works perfectly on various devices. 

### JS Validation:

- [Full JS Validation](documentation/validation/js_validation.png)

- No errors or warning messages were found when passing through the official [JSHint](https://www.jshint.com/) validator. However, the validator has pointed that module variable is not used, but this variable is needed for the automated testing. Needless to say, that as the modern js syntax was used (the Optional Chaining method - `?.`) `/* jshint esversion: 11 */` was added to the top of the file.

### Python Validation:

- [Full Python Validation](documentation/validation/python_validation.pdf)

- No errors were found when the code was passed through Valentin Bryukhanov's [online validation tool](http://pep8online.com/). According to the reports the code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code and pasting it into the validator.

## Lighthouse Report

### Home Page

![Lighthouse Report. Home Page](documentation/lighthouse_reports/lighthouse_home.png)

### Login Page

![Lighthouse Report. Login Page](documentation/lighthouse_reports/lighthouse_signin.png)

### Logout Page

![Lighthouse Report. Logout Page](documentation/lighthouse_reports/lighthouse_logout.png)

### Forgot Password Page

![Lighthouse Report. Forgot Password Page](documentation/lighthouse_reports/lighthouse_forgot_password.png)

### Access Limited Page

![Lighthouse Report. Access Limited Page](documentation/lighthouse_reports/access_limited.png)

### New Applications Page

![Lighthouse Report. New Applications Page](documentation/lighthouse_reports/lighthouse_new_applications.png)

### New Application Detail Page

![Lighthouse Report. New Application Detail Page](documentation/lighthouse_reports/lighthouse_application_detail.png)

### Application Detail Page

![Lighthouse Report. Application Detail Page](documentation/lighthouse_reports/lighthouse_application_detail.png)

### Members Page

![Lighthouse Report. Members Page](documentation/lighthouse_reports/lighthouse_members.png)

### Profile Page

![Lighthouse Report. Profile Page](documentation/lighthouse_reports/lighthouse_profile.png)

### Profile Edit Page

![Lighthouse Report. Profile Edit Page](documentation/lighthouse_reports/lighthouse_profile_edit.png)

### Profile Edit Password Page

![Lighthouse Report. Profile Edit Password Page](documentation/lighthouse_reports/lighthouse_profile_password.png)

### Profile Delete Page

![Lighthouse Report. Profile Delete Page](documentation/lighthouse_reports/lighthouse_profile_delete.png)

