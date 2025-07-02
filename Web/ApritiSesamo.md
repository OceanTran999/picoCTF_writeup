The challenge provide us a login web and believe that we can't exploit their vulnerability :)

When I try some special characters like `", ', {, }` there is nothing different between the output, therefore I think this challenge might not use SQL to inject queries, the login page also use PHP. Therefore, the only I think is to use `Type Confusion` vulnerability, I will change the type of variable input `username` and `password` from `String()` type to `Array[]` type, after sending to the server we will get the flag XD

# References
- https://socradar.io/understanding-the-type-confusion-vulnerability/
- https://learn.snyk.io/lesson/type-confusion/?ecosystem=javascript
