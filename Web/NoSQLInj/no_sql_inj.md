![Chal](https://github.com/user-attachments/assets/012d22aa-d9f9-48a9-b275-1d4d739cca11)


The challenge gives us a login web and also its source code.

![web](https://github.com/user-attachments/assets/f6bee303-964a-4205-a5a6-b59142e6b72a)


Using normal login, I see that my HTTP POST is in JSON type, and the server return the `false` value.

![normal_login](https://github.com/user-attachments/assets/841d1228-9fcf-49c6-aa6e-24b1fbfe07a3)


Reading the source code, I understand that the server is using **MongoDB**, also there's a leaked email and it seems the flag is the `token` value and return if we successfully login to the server. We will use NoSQL technique to exploit.

![leak_mail](https://github.com/user-attachments/assets/5365d727-7303-4e7f-8a6e-d468b11f002e)


So to exploit, I will use the given email to the `email` field, and using the {"$ne":"invalid"} in the `password` field. This payload means that it will return all values that does not match to the value `invalid` of NoSQL Operator `$ne`.

![success](https://github.com/user-attachments/assets/8e0d1630-919f-445f-b7a7-8716c2f72d71)


![flag](https://github.com/user-attachments/assets/710aa5ab-4c96-407e-96bc-1f8f2113adee)


# References
- https://www.mongodb.com/docs/manual/tutorial/query-documents/?msockid=0aa89b8068446d88075f895b69566cfb
- https://portswigger.net/web-security/nosql-injection
