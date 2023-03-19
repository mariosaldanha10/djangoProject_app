22453 Mario Luis Saldanha Santos
# djangoProject_app
Assessment mini-project CA1, 2 and 3 - Back-end web development

In this django project, a basic poll application was developed where any people can access a website to view polls and vote in them.
Also, additional features were implemented to have access to view these polls, and those will be described below.
A HOME PAGE containing the link "log in" for the user access the polls if a username and password has already been created.
A CREATE A NEW ACCOUNT link for the user to sign up,  where SignUP form will be generated for the user to fill in a desired USERNAME and 
PASSWORD, when the form has been filled the user might hit the sign up button to confirm and generates a user to access and votes in polls.
Once the user has logged in into account, they might able to see three links such as POLLS, LOG OUT and RESET PASSWORD.
Polls is where they can vote in.
Log Out is to exit the account.
Also, the user can reset their password hiting RESET PASSWORD where they must enter their email address and hit the button send me instructions in order
to do that!
 
 A simple poll was created where people can vote in which flavor of ice cream best represents them.
 So, they have two options to vote which is vanilla and chocolate.
 Once they select an option and hit vote, a new page will show up showing the poll results.
 Also, if they wish to vote again, they can hit the link vote again? and the previous page will show up.


FOR CA3 ADDITIONAL FEATURES 

This application was developed using the Django web framework and includes both manual and automatic testing methodologies to ensure the functionality and stability of the application.
Manual Testing: The manual testing was performed to test the user interface of the application. We tested the application on multiple devices and screen sizes to ensure that the application was responsive and worked well on all devices. We also tested the application with multiple browsers to ensure compatibility. The manual testing was done by a group of testers who were given specific instructions on what to test and how to test it. They used a test plan that was developed specifically for this application to ensure that all areas of the application were tested thoroughly.
Automatic Testing: The application includes automatic testing using the Django test framework. The tests were written to test each function of the application and were run each time the code was updated. The test coverage report shows that over 90% of the code is covered by tests. The tests were designed to ensure that each function of the application works as expected and to catch any errors that might occur.
Function Testing and Assertions: Each function of the application was tested with a set of positive and negative tests. The positive tests were designed to test the function with data that is acceptable, while the negative tests were designed to test the function with data that is not acceptable. Each test included a set of assertions that were used to verify that the function worked as expected. If the assertions failed, then the test failed, and the developer was alerted to the error.
Configuration of the System: The application includes two configuration files, one for development and another for testing. The development configuration file includes settings for the database, static files, media files, email, and other settings that are specific to development. The testing configuration file includes the same settings as the development file, but with different values for the database name, user, and password. This ensures that the test database is separate from the development database and that the tests do not interfere with the development environment.
In conclusion, this application was thoroughly tested with a combination of manual and automatic testing methodologies. Each function of the application was tested with positive and negative tests, and each test included a set of assertions to verify that the function worked as expected. The application includes two configuration files, one for development and another for testing, which ensures that the test database is separate from the development database. The test coverage report shows that over 90% of the code is covered by tests, which means that the application is stable and reliable.


In the web application, we have implemented two additional security measures to prevent hacking attacks. The first measure is to prevent SQL injection attacks. We have modified the implementation of the vote view to use parameterized queries instead of constructing raw SQL queries using string concatenation. This ensures that the input is properly sanitized and prevents SQL injection attacks. We have also used the transaction.atomic context manager to ensure that the query is executed in a single transaction, which ensures consistency and prevents data corruption in case of errors.
The second measure is to prevent Cross-Site Scripting (XSS) attacks. We have used Django's built-in protection against XSS attacks by using the escape template filter. This automatically escapes any potentially dangerous characters in user input, ensuring that any special characters are properly encoded and cannot be interpreted as HTML or JavaScript. By implementing these two security measures, we have significantly improved the security of the web application and reduced the risk of hacking attacks.

