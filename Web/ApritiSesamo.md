![chall](https://github.com/user-attachments/assets/ad7d2a37-6018-44cb-a998-93757f9746d6)

The challenge provide us a login web and believe that we can't exploit their vulnerability :)

![login](https://github.com/user-attachments/assets/edafb3d7-d088-4761-bdef-8838bed6b7b6)


When I try some special characters like `", ', {, }` there is nothing different between the output, so I think this challenge might not use SQL to inject queries, the login page also use PHP. To solve this, the only way I think is to use `Type Confusion` vulnerability, I will change the type of variable input `username` and `password` from `String` type to `Array[]` type, after sending to the server we will get the flag XD

![flag](https://github.com/user-attachments/assets/2ffa194d-dd08-4880-9f70-4e1d93497734)


# References
- https://socradar.io/understanding-the-type-confusion-vulnerability/
- https://learn.snyk.io/lesson/type-confusion/?ecosystem=javascript
