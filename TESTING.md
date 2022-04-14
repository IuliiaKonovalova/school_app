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