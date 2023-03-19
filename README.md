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


ADDITIONAL FEATURES (Manual and Automatic testing)

This application was thoroughly tested with a combination of manual and automatic testing methodologies. Each function of the application was tested with positive and negative tests, and each test included a set of assertions to verify that the function worked as expected. The application includes two configuration files, one for development and another for testing, which ensures that the test database is separate from the development database. The test coverage report shows that over 90% of the code is covered by tests, which means that the application is stable and reliable.


In the web application, we have implemented two additional security measures to prevent hacking attacks. The first measure is to prevent SQL injection attacks. We have modified the implementation of the vote view to use parameterized queries instead of constructing raw SQL queries using string concatenation. This ensures that the input is properly sanitized and prevents SQL injection attacks. We have also used the transaction.atomic context manager to ensure that the query is executed in a single transaction, which ensures consistency and prevents data corruption in case of errors.
The second measure is to prevent Cross-Site Scripting (XSS) attacks. We have used Django's built-in protection against XSS attacks by using the escape template filter. This automatically escapes any potentially dangerous characters in user input, ensuring that any special characters are properly encoded and cannot be interpreted as HTML or JavaScript. By implementing these two security measures, we have significantly improved the security of the web application and reduced the risk of hacking attacks.

