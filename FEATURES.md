# Cool School

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
| sales page                  | Y | N | Y (plus add a sale and edit or delete personal sales only) | N | N | N |
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

- Each page has a navbar and a footer

**Navbar**

![Navbar](documentation/features/navbar/navbar.png)

Navbar has the following links:
- home page
- button "get started", which leads to the registration page and login page
- ![Get Started button](documentation/features/navbar/get_started_button.png)
- It also has a logo of the school
- ![Logo](documentation/features/navbar/main_logo.png)

The simplistic design of the navbar is based on the decision to make the use of the webapp easy for the user.

When the user clicks on the get started button, the menu opens, and the user can choose to register or log in.

- ![Get Started menu](documentation/features/navbar/navbar_logout.png) 

When the user is logged in, the navbar looks as follows.

- ![Navbar User logged in](documentation/features/navbar/navbar_logged_in.png)

It has only one button "Menu", which opens the menu.

- ![Menu Button](documentation/features/navbar/navbar_menu.png)

If the user is a boss or a sales manager, the menu has a following links:

- ![Menu Boss or Manager View](documentation/features/navbar/menu_admin_view.png)

Menu has the following buttons:
- Profile (which leads to the user profile page)
- New applications (which leads to the new applications page)
- Sales (which leads to the sales page)
- Members (which leads to the members page)
- Students (which leads to the students page)
- Schedule (which leads to the schedule page)
- Logout (which leads to the logout page)

If the user is a teacher or a receptionist, the menu has a following look:

- ![Menu Teacher or Receptionist View](documentation/features/navbar/menu_receptionists.png)

Menu has the following buttons:
- Profile (which leads to the user profile page)
- Members (which leads to the members page)
- Students (which leads to the students page)
- Schedule (which leads to the schedule page)
- Logout (which leads to the logout page)

if the user is a parent or a potential client, the menu has a following look:

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

- School information in the middle with the school email, phone number, and address:

  ![School Information](documentation/features/footer/footer_school_data.png)

- Information about the coder is on the right side with links to the GitHub and LinkedIn, and email:

  ![Coder Information](documentation/features/footer/footer_creator_data.png)


For the mobile version of the website, the footer looks as follows:

  ![Footer Mobile](documentation/features/footer/footer_mobile.png)


**Home page**

![Home page](documentation/features/home_page/home_page.png)

The Home page has a simple welcome message and a button "get started" which leads to the registration page, from which the user can be redirected to the login page.

- ![Home page Hero section](documentation/features/home_page/home_page_logo_get_started.png)

Under the hero section, there is a section, which describes the benefits of signing up.

- ![Home page Benefits section](documentation/features/home_page/home_page_benefits.png)

This section has 3 cards, each with a title, a description, and an image.

On the mobile version, the cards are displayed in two rows.

  ![Home page Benefits section mobile](documentation/features/home_page/home_page_benefits_mobile.png)

After the cards, there are 3 subsections.

1. The first subsection has a text incentive on the left side and an image on the right side.

  ![Home page First subsection](documentation/features/home_page/home_page_incentive.png)

2. The second subsection has a text describing the school's personnel on the right side and an image on the left side.

  ![Home page Second subsection](documentation/features/home_page/home_page_personnel.png)

3. The third subsection has a text describing the school's concern about children's health on the left side and an image on the right side.

  ![Home page Third subsection](documentation/features/home_page/home_page_health.png)


After the subsections, there is an immediate contact section that has an incentive to become a school member right now and a button "get started", which leads to the registration page. The user can be redirected to the login page.

  ![Home page Contact section](documentation/features/home_page/home_page_contact_now.png)

**Registration page**

  ![Registration page](documentation/features/register_page/signup_page.png)

This page has a dark-blue container with a sign up form, which has a header and input fields for the user to fill in.

In the header of the form, there is a title "Sign up" and a subtitle "Please Fill out all information", which the seriousness of the company towards the user.

  ![Registration page header](documentation/features/register_page/signup_page_header.png)

Underneath, there is a subtitle "Already have an account?." and a button "Login", which leads to the login page.

  ![Registration page header](documentation/features/register_page/signup_page_login.png)

Under the form's header, there are the following fields:

  ![Registration page fields](documentation/features/register_page/signup_page_fields.png)

These fields are required for the user to be filled out.
- Email address (to let sales managers and bosses contact the user)
- Username (to let the user have a personal profile)
- First name (to let the user have a personal profile)
- Last name (to let the user have a personal profile)
- Phone number (to let sales managers and bosses contact the user)
- Password (to let the user log in)
- Password confirmation (to let the user log in)

If the user types the wrong email address, the email field will be highlighted.

  ![Registration page email field](documentation/features/register_page/signup_page_error_email.png)

If the user leaves an empty field, the field will be highlighted.

  ![Registration page empty field](documentation/features/register_page/signup_page_error_empty_field.png)

If the user typed a not save password or the confirmation password didn't match, the password field will be highlighted.

  ![Registration page password field](documentation/features/register_page/signup_page_error_password.png)

If the user typed a not save username, the username field will be highlighted.

  ![Registration page username field](documentation/features/register_page/signup_page_error_username.png)

**Login page**

  ![Login page](documentation/features/login_page/login_page.png)

Login Page has a dark-blue container with a login form, which has a header and input fields for the user to fill in. Plus it has a button "Sign In" and "Forgot password?", leading to the forgot password page.

  ![Login page header](documentation/features/login_page/login_page_header.png)

The header has the title "Log in" and the subtitle "If you have not created an account yet, then please sign up first."

When the user clicks on the button, he is redirected to the registration page.

  ![Login page header](documentation/features/login_page/login_page_signup_button.png)

Underneath, there are two fields which have to be filled out in order to log in:

- Username or email address
- Password

  ![Login page fields](documentation/features/login_page/login_page_fields.png)

If the user made a mistake in the username or password, the field will be highlighted.

  ![Login page error field](documentation/features/login_page/login_page_error.png)

Under the fields, there is a button "Sign in" which leads to the schedule page.

  ![Login page sign in button](documentation/features/login_page/login_page_button.png)

Under this button, there is a button "Forgot password?", which leads to the forgot password page.

  ![Login page forgot password button](documentation/features/login_page/login_page_forgot_password.png)

**Logout page**

  ![Logout page](documentation/features/logout_page/logout_page.png)

This page has a dark-blue container with a logout form with a header and a button "Logout" leading to the home page.

  ![Logout page header](documentation/features/logout_page/logout_page_box.png)

It has the title "Logout" and the subtitle "Are you sure you want to logout?"
Underneath, there is a button "Sign Out".

  ![Logout page buttons](documentation/features/logout_page/logout_page_signout_button.png)

**Forgot password page**

  ![Reset password page](documentation/features/reset_password_page/reset_password_page.png)

 It has a dark-blue container with a reset password form with a header and input fields for the user to fill in and a reset button.

  ![Reset password page header](documentation/features/reset_password_page/reset_password_page_box.png)

The header has the title "Reset Password" and a subtitle, which guides the user on what actions should be done in order to regain access to the user's account.

  ![Reset password page header](documentation/features/reset_password_page/reset_password_page_box_header.png)

Underneath, there are fields, where the user can type in his email address.

  ![Reset password page fields](documentation/features/reset_password_page/reset_password_page_field.png)

If the user types a wrong email address, the email field will be highlighted.

There is a button "Reset My Password," which leads to the home page. The user will receive an email with a link to reset his password.

  ![Reset password page button](documentation/features/reset_password_page/reset_password_page_button.png)
  
**Profile page**

  ![Profile page](documentation/features/profile_page/profile_page_admin.png)

The Profile Page has a container where the user can see his personal information.

  ![Profile page](documentation/features/profile_page/profile_page_not_admin.png)

It has 2 buttons in top right corner: "Edit" and "Password". The "Edit" button leads to the edit profile page. The "Password" button leads to the change password page.

  ![Profile page buttons](documentation/features/profile_page/edit_password_buttons.png)

If the user is the boss, there is an additional button in the top left corner, "Delete."

  ![Profile page buttons](documentation/features/profile_page/profile_page_admin.png)

The button "Delete" leads to the delete profile page.

  ![Profile page buttons](documentation/features/profile_page/profile_page_delete_button.png)

This button has a presence for all other profiles that the boss may visit; thus, only a boss can delete a profile.

  ![Profile page buttons](documentation/features/profile_page/profile_page_other_user.png)

As a comparison, the profile page of the user that the boss visited on the previous screenshot has no "Delete" button.

  ![Profile page buttons](documentation/features/profile_page/profile_page_not_admin.png)

If the user is a parent, the profile has a following look:

  ![Profile page parent](documentation/features/profile_page/profile_parent.png)

There is an additional field where the parent may assign their relation to a kid as it will be displayed for the school's members.

  ![Profile page parent relation field](documentation/features/profile_page/profile_edit_role.png)

When the user clicks on the button "Edit", the dropdown menu appears, where she or he may choose the relation to their children:

Types of the relation:

- Mother;
- Father;
- Grandmother;
- Grandfather;
- Other.

  ![Profile page edit button](documentation/features/profile_page/profile_role_choice.png)

After choosing and clicking the save button, the relation will be assigned.

  ![Profile page edit button](documentation/features/profile_page/relation_save.png)

If the user is a teacher, the profile has a following look:

  ![Profile page teacher](documentation/features/profile_page/profile_page_teacher.png)

There is additional data on the classes given to the students underneath the profile box.

  ![Profile page teacher classes](documentation/features/profile_page/profile_page_teacher_classes_box.png)

This box is only visible to the teacher and the bosses.

In this box, there are date pickers, which allow the teacher or the boss to sort classes during a particular period.

  ![Profile page teacher classes](documentation/features/profile_page/profile_page_teacher_datepicker.png)

Here the teacher or the boss will be able to pick data, and the summary of the classes will be displayed.

Needless to say, the pagination functionality has been implemented in case there are more than 20 classes.

  ![Profile page teacher classes](documentation/features/profile_page/page_navigation1.png)

The buttons for the page navigation have different appearances to guide the user on whether there are more classes or not.

  ![Profile page teacher classes](documentation/features/profile_page/page_navigation2.png):

If the user is a Sales Manager, the profile has a following look:

  ![Profile page sales manager](documentation/features/profile_page/profile_page_sales.png)

It has two addition sections: Students for which this sales manager is in charge (visible to all users) and "Sales made" (visible to the sales manager her/himself and the boss)

  ![Profile page sales manager Subsections](documentation/features/profile_page/profile_page_sales_subsections.png)

The "Students" section has a table with the students that this sales manager is in charge of.

  ![Profile page sales manager students](documentation/features/profile_page/profile_page_sales_students.png)

There the sales manager or the user can see all students. Moreover, the students whose parents should be contacted urgently have an orange label to make them more distinguishable.

  ![Profile page sales manager students](documentation/features/profile_page/profile_page_sales_urgent.png)

Underneath the "Students" section, there is a table with the "Sales made" by the sales manager.

  ![Profile page sales manager sales](documentation/features/profile_page/profile_page_sales_sales.png)

It has a header with the total amount of sales made by the sales manager and a link to the sales page, where the whole statistics are stored.

  ![Profile page sales manager sales](documentation/features/profile_page/profile_page_sales_header.png)

Under the header, there are recent sales made with limited data (the date on which the sale was made and the number of classes sold). Since the pagination functionality has been implemented, there are only 20 recent sales could be seen, and there are two buttons for the page navigation at the bottom of the table.

  ![Profile page sales manager sales](documentation/features/profile_page/page_navigation1.png)

**Edit profile page**

  ![Edit profile page](documentation/features/profile_edit_page/profile_edit_page.png)

It has a container where the user can edit:

- First Name;
- Last Name;
- Phone Number;

There are three fields with prefilled data for the user. The user could change this data if he/she wants.

  ![Edit profile page](documentation/features/profile_edit_page/profile_edit_fields.png)

Underneath the fields, there are two buttons, "Go Back" and "Save." If the user doesn't want to save changes, they can click on the "Go Back" button and will be redirected to the profile page. If the user wants to save changes, they can click on the "Save" button and will be redirected to the profile page.

  ![Edit profile page](documentation/features/profile_edit_page/cancel_save_buttons.png)

**Profile Delete Page**

  ![Profile delete page](documentation/features/profile_delete_page/profile_delete_page.png)

Only the bosses have access to this page as only they are able to delete any profile.

This page has a box with a warning message and a link to the profile page of the user that is about to be deleted:

  ![Profile delete page](documentation/features/profile_delete_page/member_delete_link.png)

There are two buttons under the warning message, there are two buttons, "Cancel" and "Delete". If the user doesn't want to delete the profile, he/she can click on the "Cancel" button and will be redirected to the profile page. If the user wants to delete the profile, he/she can click on the "Delete" button and will be redirected to the profile page, and the school member will be permanently deleted.

  ![Profile delete page](documentation/features/profile_delete_page/cancel_delete_buttons.png)

**Profile Change Password Page**

  ![Profile change password page](documentation/features/profile_change_password_page/profile_password_page.png)

It has a header with the title "Change Password" and a subtitle to guide the user on what to do next. Underneath, there are three field to be filled:

- Old Password;
- New Password;
- Confirm New Password.

  ![Profile change password page](documentation/features/profile_change_password_page/change_password_fields.png)

If there are any errors in the fields, the user will see the error message.

Under the fields, there are two buttons, "Go Back" and "Submit". If the user doesn't want to change the password, he/she can click on the "Go Back" button and will be redirected to the profile page. If the user wants to change the password, he/she can click on the "Change Password" button and will be redirected to the profile page, and the password will be changed if all conditions are met.

  ![Profile change password page](documentation/features/profile_change_password_page/cancel_delete_buttons.png)

**New Applications Page**

This page is only visible to the boss and sales manager.
  
![New applications page](documentation/features/new_applications_page/new_applications.png)

This page has a title and the number of the new applications left.

  ![New applications page](documentation/features/new_applications_page/new_applications_summary.png)

It also has a table with the new applications, where each application has a link. After clicking on the application in a table, the user will be redirected to the application detail page.

  ![New applications page](documentation/features/new_applications_page/new_applications_data.png)

Underneath the table, there are navigation buttons. If the user wants to see the next page of the application, he/she can click on the "Next" button. If the user wants to see the previous page of the applications, he/she can click on the "Previous" button.

  ![New applications page](documentation/features/new_applications_page/page_navigation1.png)
  ![New applications page](documentation/features/new_applications_page/page_navigation2.png)

**Application Detail Page**

This page is accessible to the boss and sales manager.
For the boss, the page has the following look:

  ![Application detail page. Boss View](documentation/features/application_detail_page/application_detail_admin_view.png)

It has two boxes. The first box consists of the information about the applicant, including the name, the email, and the phone number.

  ![Application detail page. Applicant Data Box](documentation/features/application_detail_page/application_detail_data.png)

It also has a "Delete" button in the top right corner of the page. If the boss wants to delete the application, he/she can click on the "Delete" button and will be redirected to the delete application page.

  ![Application detail page. Delete Button](documentation/features/application_detail_page/application_detail_delete_button.png)

The second box provides the boss with the assigning role functionality, which will give access to the applicant to the application according to the role the boss assigns.

  ![Application detail page. Role Assignment Box](documentation/features/application_detail_page/application_detail_role.png)

When the boss clicks on the dropdown menu, the following choices will be shown:

  ![Application detail page. Role Choices](documentation/features/application_detail_page/application_detail_role_choice.png)

After choosing the role the boss wants to assign, he/she can click on the "Save" button.

  ![Application detail page. Save Role Button](documentation/features/application_detail_page/application_detail_save_role_button.png)

When the boss clicks on "Save" button, the role will be assigned to the applicant. However, it will not redirect the boss to any page in order to prevent the boss from accidentally assigning the wrong role to an applicant.

To go back to the applications page, the boss may click on the link underneath the boxes "Go to other applications". And the user will be redirected to the applications page.

  ![Application detail page. Go back to applications](documentation/features/application_detail_page/application_detail_back.png)

For the sales manager, the page has the following look:

  ![Application detail page. Sales Manager View](documentation/features/application_detail_page/application_detail_sale_view.png)

The page has no "Delete" button as it is not accessible to the sales manager. Moreover, the page has no box with the assigning role to the new applicant as it is accessible only to the boss.

**Application Delete Page**

  ![Application delete page](documentation/features/application_delete_page/application_delete_page.png)

This page is only accessible to the boss. Thus, only the boss is empowered to delete any applications.
It has a warning message with the applicant's name.

  ![Application delete page](documentation/features/application_delete_page/application_delete_warning.png)

It also has 2 buttons, "Go Back" and "Delete". If the boss doesn't want to delete the application, he/she can click on "Go Back" button and will be redirected to the application detail page. If the boss wants to delete the application, he/she can click on "Delete" button. He / she will be redirected to the new applications page, and the application will be permanently deleted.

  ![Application delete page](documentation/features/application_delete_page/cancel_delete_buttons.png)

**Limited Access Page**

  ![Limited access page](documentation/features/limited_access_page/limited_access_page.png)

This page applies to the users that are not allowed to access the page that they want to enter manually in the address bar. it has a box with a friendly message pointing out that the user has no access to a particular page. It also has a link to the user's profile page.


  ![Limited access page. Link to Personal Profile](documentation/features/limited_access_page/limit_access_link.png)

**Sales Page**

This page is accessible only by the sales manager and the boss. However, the look of the page is different for the boss and the sales manager as the boss has no access to add, edit or delete salez.

For the sales managers, the sales page looks as follows:

  ![Sales page. Sales Manager View](documentation/features/sales_page/sales_page_sales_view.png)

It has a button "Add new sale" in the top right corner of the page. If the sales manager wants to add a new sale, he/she can click on the "Add new sale" button and will be redirected to the add new sale page.

  ![Sales page. Add New Sale Button](documentation/features/sales_page/sales_page_add_sale_button.png)

It has the title "Sales", datepicker sorting bar, and a table with the sales.

The sorting bar has 2 datepickers, one for the start date and one for the end date. The sales are sorted by the start date. There is a button "Search" on the right side of the sorting bar. after picking dates and clicking on the "Search" button, the sales will be filtered by the dates.

  ![Sales page. Sorting Bar](documentation/features/sales_page/datepicker_menu.png)

Under the sorting bar, there is the summary of sales found:

  ![Sales page. Summary](documentation/features/sales_page/sales_page_summary.png)

The table has the following columns:

- ID of the sale;
- Date of the sale;
- Total amount of classes sold;
- Manager, who conducted the sale (with the link to the personal profile);
- Client, who bought the classes (with the link to the personal profile);
- Student for whom the classes were bought (with the link to the personal profile);
- Edit, which will redirect the sales manager to the edit sale page;
- Delete, which will redirect the sales manager to the delete sale page.

  ![Sales page. Table](documentation/features/sales_page/sales_page_edit_delete_limitations.png)

As it is shown in the picture, only the sales manager, who conducted the sale, is able to edit or delete the sale. The user in the picture is Annie Green, and only she is able to edit or delete the sale which she conducted. She has no access to render or delete the sales made by another Sales Manager, Kate Peterson.

Under the table, there is a navigation bar for the table. It has a "Previous" button and a "Next" button. The "Previous" button will redirect the sales manager to the previous page of the table. The "Next" button will redirect the sales manager to the next page of the table.

  ![Sales page. Navigation1](documentation/features/sales_page/page_navigation1.png)
  ![Sales page. Navigation2](documentation/features/sales_page/page_navigation2.png)

On the mobile screens, the table has only the following columns:

- ID of the sale;
- Date of the sale;
- Total amount of classes sold;
- Edit, which will redirect the sales manager to the edit sale page;
- Delete, redirecting the sales manager to the delete sale page.

  ![Sales page. Mobile Table](documentation/features/sales_page/sales_page_mobile.png)

It also has a friendly message, which will suggest that the user open the sales on the page to view the complete data on sales on the broader devices.

Additionally, the sales page has a different look for the boss. It has no "Add new sale" button in the top right corner of the page. It has "Edit" and "Delete" columns as only sales managers can edit or delete their sales.

  ![Sales page. Boss View](documentation/features/sales_page/sales_page_admin_view.png)

**Add New Sale Page**

This page is accessible only by the sales manager.

  ![Add new sale page.](documentation/features/add_sale_page/add_sale_page.png)

 It has the title "Add New Sale" and a form with the following fields:

  ![Add new sale page. Fields](documentation/features/add_sale_page/add_sale_page_fields.png) 

- Client Name (with dropdown menu, where all clients are listed);
- Amount (for the number of classes that the client is buying);
- Student (with dropdown menu, where all students are listed);

When a Sales Manager clicks on the "Client Name" dropdown menu, it will show all the clients with an option to type a name for a search:

  ![Add new sale page. Dropdown Functionality](documentation/features/add_sale_page/add_sale_dropdown.png)

When a Sales Manager clicks on the "Student" dropdown menu, it will show all the students with an option to type a name for a search:

  ![Add new sale page. Dropdown](documentation/features/add_sale_page/add_sale_page_dropdown_students.png)

Underneath the form, there is a button "Save" and a button "Cancel". If the sales manager clicks on the "Save" button, the form will be validated, and if it is valid, the sale will be added to the database. If the form is not valid, the user will be redirected to the same page, and the form will be filled with the data that was entered before. If the sales manager clicks on the "Cancel" button, he/she will be redirected to the sales page.

  ![Add new sale page. Form Buttons](documentation/features/add_sale_page/cancel_back_buttons.png)

**Edit Sale Page**

This page is accessible only by the sales manager.

  ![Edit sale page.](documentation/features/edit_sale_page/edit_sale_page.png)

 It has the title "Edit Sale" and a form with the following fields with pre-filled data:

  ![Edit sale page. Fields](documentation/features/edit_sale_page/edit_sale_page_fields.png)

The dropdown menus are pre-filled with the data from the sale that is being edited, and the previously chosen client is highlighted with the orange background. The same comes to the dropdown menus for the students.

  ![Edit sale page. Dropdown](documentation/features/edit_sale_page/edit_sale_page_dropdown.png)

Under the fields, there are two buttons: "Save" and "Cancel." If the sales manager clicks on the "Save" button, the form will be validated, and if it is valid, the sale will be updated in the database. If the form is not valid, the user will be redirected to the same page, and the form will be filled with the data that was entered before. If the sales manager clicks on the "Cancel" button, he/she will be redirected to the sales page.

  ![Edit sale page. Form Buttons](documentation/features/edit_sale_page/cancel_back_buttons.png)

**Delete Sale Page**

This page is accessible only by the sales manager.

  ![Delete sale page.](documentation/features/delete_sale_page/delete_sale_page.png)

 It has the title "Delete Sale" and a warning message with info og the sale that is about to be deleted.

  ![Delete sale page. Warning Message](documentation/features/delete_sale_page/delete_sale_page_warning.png)

Under the warning message there are 2 buttons: "Delete" and "Cancel". If the sales manager clicks on the "Delete" button, the sale will be deleted from the database. If the sales manager clicks on the "Cancel" button, he/she will be redirected to the sales page.

  ![Delete sale page. Form Buttons](documentation/features/delete_sale_page/cancel_delete_buttons.png)

**MembersPage**

This page is accessible only by the school personnel (bosses, teachers, sales managers, receptionists).

  ![Members page.](documentation/features/members_page/members_page.png)

  It has the title "Members" and a sorting bar. The sorting bar has the following choices:

- All Members;
- Parents;
- Teachers;
- Sales Managers;
- Receptionists;

  ![Members page. Sorting bar](documentation/features/members_page/members_page_sorting_bar.png)

When the user clicks on the "All Members" button, the table will be sorted by the name of the member. When the user clicks on the "Parents" button, the table will be sorted by the name of the parent. When the user clicks on the "Teachers" button, the table will be sorted by the name of the teacher. When the user clicks on the "Sales Managers" button, the table will be sorted by the name of the sales manager. When the user clicks on the "Receptionists" button, the table will be sorted by the name of the receptionist.

It also displays the amount of the sorting results:

  ![Members page. Sorting bar](documentation/features/members_page/members_page_summary.png)

There is also a search bar with the instructions:

  ![Members page. Search bar](documentation/features/members_page/members_page_search_input_results.png)

When the user inputs the name of the member, the search bar will show the amount of the results.
  
  ![Members page. Search bar](documentation/features/members_page/members_page_search_input.png)

In the table results, the user will see only members which match the input:

  ![Members page. Search bar Results](documentation/features/members_page/members_page_search_input_results.png)

  
Then the redo button will be displayed. When the user clicks on the redo button, the search bar will be cleared, and the table will be sorted by the name of the member.

  ![Members page. Search bar. Undo Button](documentation/features/members_page/undo_button.png)


Underneath, there is a table of the results. It has links to the pages of each member.

Under the table, there is a navigation bar for the table. It has a "Previous" button and a "Next" button. The "Previous" button will redirect the sales manager to the previous page of the table. The "Next" button will redirect the sales manager to the next page of the table.

  ![Sales page. Navigation1](documentation/features/members_page/page_navigation1.png)
  ![Sales page. Navigation2](documentation/features/members_page/page_navigation2.png)


**Student Page**

This page is accessible only by the school personnel (bosses, teachers, sales managers, receptionists).

  ![Student Page](documentation/features/students_page/students_page_admin_view.png)

There is a button "add new student," which is visible only to sales managers and bosses as only they are empowered to add any students.

  ![Student Page. Add New Student Button](documentation/features/students_page/add_student_button.png)

When the sales manager or a boss clicks on this button, he/she will be redirected to add a new student page.

At the top of the age, there is a title "All Students", and under this title, there is a search bar with instructions underneath this input bar.

  ![Student Page. Search Input](documentation/features/students_page/students_page_search_input.png)

Here the user may type the name in order to find a particular student. As the user starts typing, the undo button appears in the search bar.

  ![Student Page. Undo Button](documentation/features/students_page/undo_button.png)

When the user clicks on the undo button or deletes the input manually, the undo button disappears.

Under the search bar, there is a sorting bar where the user may sort students according to the urgent call needs. It has two options: All students sort and Urgent Class Sort. Plus, there is a search button on the right side. There are also the instructions under the sorting bar.

  ![Student Page. Sorting Bar](documentation/features/students_page/students_page_sort.png)

If a student has fewer than ten classes left, this student will have an urgent label on the right side of their name.

  ![Student Page. Urgent Label](documentation/features/students_page/students_student_urgent_call.png)

After all, there is sorting results summary:

  ![Student Page. Sort Summary](documentation/features/students_page/students_page_summary.png)

The following image will display how the urgent sort works:

  ![Student Page. Urgent Sort](documentation/features/students_page/students_sort_urgent_results.png)

The central part of this page is devoted to the student's table, where all students are displayed. The users can see students' names, urgent call labels, and the link to students' profiles. If the user clicks on the student, he/she will be redirected to this student's profile.

  ![Student Page. Students Table](documentation/features/students_page/students_page_table.png)

  Under the table, there is page navigation. 

Under the table, there is a navigation bar for the table. It has a "Previous" button and a "Next" button. The "Previous" button will redirect the sales manager to the previous page of the table. The "Next" button will redirect the sales manager to the next page of the table.

  ![Student page. Navigation1](documentation/features/students_page/page_navigation1.png)
  ![Student page. Navigation2](documentation/features/students_page/page_navigation2.png)

The Students Page looks differently for teachers and receptionists as there is no "add new student" button in the top right corner:

  ![Student Page. Teachers and Receptionists View](documentation/features/students_page/students_page.png)

**Add student Page**

This page is accessible only by the sales manager and the boss.

  ![Add Student Page.](documentation/features/add_student_page/add_student_page.png)

 It has the title "Add Student" and a form with the following fields:

  ![Add Student Page. Fields](documentation/features/add_student_page/add_student_fields.png) 

- First Name (student's first name);
- Last Name (student's last name);
- Parents (with the list of all clients);

*The user may search by name*

  ![Add Student Page. Parent Field](documentation/features/add_student_page/add_student_page_parents_field.png)

*The user may also assign several relatives to a student*

  ![Add Student Page. Parent Field. Chosen](documentation/features/add_student_page/add_student_page_parents_field_several.png)

- Birthday (with a date picker functionality);

  ![Add Student Page. Birthday Field](documentation/features/add_student_page/add_student_page_birthday_field.png)

- Address (to store student's address in case of urgent situations);
- Classes Left (if the parents purchased any special offers packages);
- Sales Manager (to assign the sales manager in charge of the student, who will be responsible for keeping close attention to a student's attendance)

  ![Add Student Page. Sales Field](documentation/features/add_student_page/add_student_page_sales_field.png)

- Notes (in case, if a student has any preferences or allergies)

Underneath the form, there is a button "Save" and a button "Cancel". If the sales manager or a boss clicks on the "Save" button, the form will be validated and if it is valid, the sale will be added to the database. If the form is not valid, the user will be redirected to the same page, and the form will be filled with the data that was entered before. If the sales manager or a boss clicks on the "Cancel" button, he/she will be redirected to the student's page.

  ![Add Student Page. Form Buttons](documentation/features/add_student_page/cancel_save_buttons.png)

**Edit Student Page**

This page is accessible only by the sales manager or the boss.

  ![Edit Student Page.](documentation/features/edit_student_page/edit_students_page.png)

 It has the title "Edit Student's Data" and a form with the following fields with pre-filled data:

  ![Edit Student Page. Fields](documentation/features/edit_student_page/edit_students_page_fields.png)

The fields are pre-filled with the data from the data on the previously selected student. The boss or the sales manager is able to render this data by selecting a particular field and changing data. 

Under the fields, there 2 buttons: "Save" and "Cancel". If the sales manager or the boss clicks on the "Save" button, the form will be validated, and if it is valid, the sale will be updated in the database, and he/she will be redirected to the Student's Detail page. If the form is not valid, the user will be redirected to the same page, and the form will be filled with the data that was entered before. If the sales manager clicks on the "Cancel" button, he/she will be redirected to the Student's Detail page.

  ![Edit Student Page. Form Buttons](documentation/features/edit_student_page/cancel_save_buttons.png)

**Delete Student Page**

This page is accessible only by the sales manager or the boss.

  ![Delete Student Page.](documentation/features/delete_student_page/delete_student_page.png)

 It has the title "Delete Student's data" and a warning message with the name of the student.

  ![Delete Student Page. Warning Message](documentation/features/delete_student_page/delete_student_warning.png)

The student's name has a link to his/her profile. Thus if the sales manager or a boss wants to open the student's profile, they may directly go to the student's profile.

  ![Delete Student Page. Link to student's profile](documentation/features/delete_student_page/delete_student_page_link.png)

Under the warning message there 2 buttons: "Delete" and "Cancel". If the sales manager clicks on the "Delete" button, the sale will be deleted from the database. If the sales manager clicks on the "Cancel" button, he/she will be redirected to the sales page.

  ![Delete Student Page. Form Buttons](documentation/features/delete_student_page/cancel_delete_buttons.png)

**Student Detail Page**

This page is accessible to everyone except potential clients. However, parents can see only their own children's profiles. If they try to enter other students' profiles, they will be redirected to the Access Limitation page.

The page has a following look for the bosses and sales managers:

  ![Student Detail Page](documentation/features/student_detail_page/student_detail_page_admin_view.png)

It has additional editing and deletion functionality for the bosses and sales managers. If the user clicks on the "Delete" button, he/she will be redirected to the Student Delete Page. If the user clicks on the "Edit" button, he/she will be redirected to Student Edit Page.

  ![Student Detail Page. Buttons](documentation/features/student_detail_page/edit_delete_buttons.png)

For the rest of the users, this page looks as follows:

  ![Student Detail Page. Others users view](documentation/features/student_detail_page/student_detail_page_others_view.png)

It has a student data box with a student's name as a title and a role underneath the name (Student). If a parent opens his/her child's profile, there will be an additional line pointing that this student is related to the user 

  ![Student Detail Page. Relation to the parent](documentation/features/student_detail_page/students_detail_relation.png)

Then the user may see the student's data:

  ![Student Detail Page. Data Box](documentation/features/student_detail_page/student_detail_page_data_box.png)

- Full Name;
- Birthday;
- Address;
- Parents;

  ![Student Detail Page. Parents](documentation/features/student_detail_page/student_detail_page_parents.png)

  *If the school wants to contact student's relatives, they simply need to click on the parents' link, and they will be redirected to parents' profiles, where they will see their emails and phone numbers data*

- Notes;
- Classes left;
- Sales Manager;

  ![Student Detail Page. Sales Manager](documentation/features/student_detail_page/student_detail_page_sales_manager.png)

- Enrolled date;

Underneath the data box, the user will find the information on the student's attendance.

  ![Student Detail Page. Attendance](documentation/features/student_detail_page/student_detail_attendance.png)

There is sorting by date bar and a search button on the right side of the bar. The sorting bar has 2 datepickers, one for the start date and one for the end date. The sales are sorted by the start date. There is a button "Search" on the right side of the sorting bar. after picking dates and clicking on the "Search" button, the classes will be filtered by the dates. Then the user may see the summary of the results found.

  ![Student Detail Page. Attendance Summary](documentation/features/student_detail_page/student_detail_summary.png)

Each class in the attendance section has a date, the name of the subject, and a link to view the class's details. If the user clicks on the class, he/she will be redirected to the class details page.

  ![Student Detail Page. Attendance Classes](documentation/features/student_detail_page/student_detail_page_classes.png)

Under the table, there is a navigation bar for the table. It has a "Previous" button and a "Next" button. The "Previous" button will redirect the user to the previous page of the table. The "Next" button will redirect the user to the next page of the table.

  ![Student page. Navigation1](documentation/features/student_detail_page/page_navigation1.png)
  ![Student page. Navigation2](documentation/features/student_detail_page/page_navigation2.png)

**Schedule Page**

This page is accessible to everyone. 

  ![Schedule Page](documentation/features/schedule_page/schedule_page_others_view.png)

But it has a different look for teachers:

  ![Schedule Page. Teachers' view](documentation/features/schedule_page/schedule_page_teacher_view.png)

It has a "My Schedule Button". If the teacher clicks this button, he/she will be redirected to the personal schedule page.

  ![Schedule Page. My Schedule Button](documentation/features/schedule_page/my_schedule_button.png)


And for the receptionists it will have an additional feature:

  ![Schedule Page. Receptionists' view](documentation/features/schedule_page/schedule_page_receptionist.png)

  It has the button "add lesson". Only receptionists are allowed to make any changes to the schedule.

  ![Schedule Page. Add Lesson Button](documentation/features/schedule_page/add_lesson_button.png)

The page has the title "Schedule" and the Line: "Today is ..." for the user to see which day is today. 

  ![Schedule Page. Today](documentation/features/schedule_page/schedule_today_data.png)

There is a datepicker for the user to choose a day that the user wants to look into. The calendar is set automatically on today's schedule.
If the user wants to change the day, he/she may click on the date picker, and the calendar will appear.

  ![Schedule Page. Calendar](documentation/features/schedule_page/schedule_calendar.png)

Underneath, there is a schedule table where the time period is on the left side and the classes which were scheduled on the right side. If the user clicks on the class, he/she will be redirected to the lesson detail page.

  ![Schedule Page. Schedule table](documentation/features/schedule_page/schedule_page_box.png)

When the user enters the schedule page, it displays the schedule for today's classes.

  ![Schedule Page. Schedule table for today](documentation/features/schedule_page/schedule_today.png)

When the user chooses another day, the schedule table will display classes only for that particular day that has been chosen.

  ![Schedule Page. Schedule table for another day](documentation/features/schedule_page/schedule_other_day.png)

**Teacher's Personal Schedule Page**

This page is available only to teachers.

  ![Teacher Schedule Page](documentation/features/teacher_schedule_page/teacher_schedule_page.png)

It has a button in the right top corner - "Back" - to go back to the common schedule page.

  ![Teacher Schedule Page. Back Button](documentation/features/teacher_schedule_page/back_button.png)

This schedule will display only the classes of the teacher, which account was entered.

In comparison, here is the common schedule:

  ![Common Schedule Page.](documentation/features/teacher_schedule_page/schedule_look_compare.png)

Here is the teacher's personal schedule:

  ![Teacher Schedule Page.](documentation/features/teacher_schedule_page/schedule_look_compare2.png)

**Add Lesson Page**

This page is accessible only by receptionists as only they have the rights to make any changes in the schedule.

  ![Add Lesson Page](documentation/features/add_lesson_page/add_lesson_page.png)

It has the title "Adding lesson" and the following fields:

  ![Add Lesson Page. Form fields.](documentation/features/add_lesson_page/add_lesson_fields.png)

- Date (to pick a day on which the class will be given);

  ![Add Lesson Page. Form fields. Date](documentation/features/add_lesson_page/add_lesson_date_field.png)

  *The datepicker functionality was implemented to ease choosing of the day*

- Time Period;

  ![Add Lesson Page. Form fields. Time Period](documentation/features/add_lesson_page/add_lesson_time_field.png)

*The dropdown menu was implemented to make it easy for the user to choose from available time periods*

- Subject;

  ![Add Lesson Page. Form fields. Subjects](documentation/features/add_lesson_page/add_lesson_subject.png)

*The dropdown menu was implemented to make it easy for the user to choose from available subjects*

- Teachers:

  ![Add Lesson Page. Form fields. Teachers](documentation/features/add_lesson_page/add_lesson_teachers_field.png)

*The dropdown menu was implemented to make it easy for the user to choose from a list of teachers*

- Students;

  ![Add Lesson Page. Form fields. Teachers](documentation/features/add_lesson_page/add_lesson_students_field.png)

*The dropdown menu was implemented to make it easy for the user to choose from a list of students*

The field form looks as following:

  ![Add Lesson Page. Filled Form](documentation/features/add_lesson_page/add_lesson_filled.png)

Under the fields there are 2 buttons: "Save" and "Cancel". If the receptionist clicks on the "Save" button, the sale will be added to the database. If the sales manager clicks on the "Cancel" button, he/she will be redirected to the schedule page.

  ![Delete Student Page. Form Buttons](documentation/features/delete_student_page/cancel_delete_buttons.png)

**Edit Lesson Page**

This page is accessible only by receptionists as only they have the rights to make any changes in the schedule.

  ![Edit Lesson Page](documentation/features/edit_lesson_page/edit_lesson_page.png)

 It has the title "Edit Lesson" and a form with the following fields with pre-filled data:

  ![Edit Lesson Page. Fields](documentation/features/edit_lesson_page/edit_page_fields.png)

The fields are pre-filled with the data from the data on the lesson that had been previously added. The receptionist is able to render this data by selecting a particular field and changing data. 

Under the fields there 2 buttons: "Save" and "Cancel". If the receptionist clicks on the "Save" button, the form will be validated, and if it is valid, the lesson will be updated in the database, and he/she will be redirected to the Lesson's Detail page. If the form is not valid, the user will be redirected to the same page, and the form will be filled with the data that was entered before. If the receptionist clicks on the "Cancel" button, he/she will be redirected to the Lesson's Detail page.

  ![Edit Lesson Page. Form Buttons](documentation/features/edit_lesson_page/cancel_save_buttons.png)


**Delete Lesson Page**

This page is accessible only by receptionists as only they have the rights to make changes in the schedule.

  ![Delete Lesson Page](documentation/features/delete_lesson_page/delete_lesson_page.png)

This page has the title "Lesson Deletion" and a warning message about the permanent deletion of the lesson.

  ![Delete Lesson Page. Warning](documentation/features/delete_lesson_page/delete_lesson_page_warning.png)

Inside this warning message is the link to the lesson that is about to be deleted, so the the receptionist may double check which class he/she wants to delete:

  ![Delete Lesson Page. Lesson Link](documentation/features/delete_lesson_page/delete_lesson_page_link.png)

Under the warning message, there are 2 buttons "Cancel" and "Delete". If the receptionist doesn't want to delete the lesson, he/she can click on "Cancel" button and will be redirected to the lesson detail page. If the receptionist wants to delete the lesson, he/she can click on "Delete" button, and will be redirected to the schedule page and this lesson will be permanently deleted.

  ![Profile delete page](documentation/features/delete_lesson_page/cancel_delete_buttons.png)


**Lesson Detail Page**

This page is accessible by each member of the school.

  ![Lesson Detail Page](documentation/features/lesson_detail_page/lesson_detail_page.png)

The lesson table has a different look for the users. 

School personnel except receptionists looks as follows:

  ![Lesson Detail Page. Personnel View](documentation/features/lesson_detail_page/lesson_detail_personnel.png)

It has the name of the subject as a title:

  ![Lesson Detail Page. Subject](documentation/features/lesson_detail_page/lesson_subject.png)

Under the name of the subject, there is a table with the data on the lesson:

  ![Lesson Detail Page. Personnel View](documentation/features/lesson_detail_page/lesson_data.png)

This table allows users to learn which subject is given, on which day, and in which period of time. This will be beneficial to the users plan their personal schedules.
Moreover, it has a row which shows who is teaching this subject and a row on the students which will attend the class.

However, when it comes to the users, who are parents of potential clients, the table looks a bit differently:

  ![Lesson Detail Page. Parent View](documentation/features/lesson_detail_page/lesson_detail_parent.png)

As it may be noticed, a parent may access only their own children's profiles. The rest of the students have no link to this parent.

  ![Lesson Detail Page. Parent View. Students' Links](documentation/features/lesson_detail_page/lesson_detail_parent_links.png)

When it comes to the receptionists, they have additional functionality available, and thus, the lesson table looks differently:

  ![Lesson Detail Page. Receptionist View](documentation/features/lesson_detail_page/lesson_detail_receptionist.png)

It has 2 button in the top right corner of the table: "edit" and "delete".

  ![Lesson Detail Page. Receptionist View. Buttons](documentation/features/lesson_detail_page/lesson_edit_delete_buttons.png)

If the receptionist clicks on the "Delete" button, he/she will be redirected to the Lesson Delete Page. If the user receptionist on the "Edit" button, he/she will be redirected to Lesson Edit Page.

**Error Pages**

There are also 2 additional error pages:

  ![Error Page. 404](documentation/features/error_page/404_error_page.png)

  it has a box with the header "Page 404", an image and a short message about the error ("Something went wrong as this page is not found").

  If the user is logged in and tries to access a page that doesn't exist, he/she will find a button with the link to his/her profile page.

  ![Error Page. 404. Link to user profile](documentation/features/error_page/404_error_page2.png)

  If the user is logged out and tries to access a page that doesn't exist, he/she will find a button with the link to the home page

  ![Error Page. 404. Link to home page](documentation/features/error_page/404_error_page1.png)

  Page 505 is the same as 404 page, but it has a different header ("Page 500") and message ("Something went wrong as there is an internal sever error!").

  ![Error Page. 500](documentation/features/error_page/500_error_page.png)

**Favicon**

  ![Favicon](documentation/features/favicon/favicon.png)

  The favicon is a small image that is displayed in the browser's address bar. It is used to identify the website among others and help the user to find it when he/she is searching for it.

[Back to contents](#contents)

---