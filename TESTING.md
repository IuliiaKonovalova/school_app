# Testing

## Automated testing

### Django unit testing

As there 4 main apps in the project, we can test them separately.
I knew at the very beginning that I had to implement automated testing. As was highly concentrated on the developing all functionality first, so I left testing to the end. While testing my work I found several bugs related to the access limitation to a particular pages and functionality for different roles. In the future, I plan to implement testing and code simultaneously in order to increase my productivity.

**Lessons App**

![Lessons Testing Coverage](documentation/test_reports/lessons_report_testing.png)

**Profiles App**

![Profiles Testing Coverage](documentation/test_reports/profiles_report_testing.png)

**Sales App**

![Sales Testing Coverage](documentation/test_reports/sale_report_testing.png)

**Students App**

![Students Testing Coverage](documentation/test_reports/students_report_testing.png)

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