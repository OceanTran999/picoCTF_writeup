![chall](https://github.com/user-attachments/assets/4287010e-4894-4c6a-81e4-c707b0263f51)

The challenge gives me a website with 3 blogs, when clicking each blog it doesn't happen, so I decide to read the website source code.

First, I saw there's a subdirectory named `/data`, and in order to upload it, I have to send HTTP POST method. Each block will contain a variable called `ID` with value `from 1 to 3`.

![source1](https://github.com/user-attachments/assets/79329b2b-0dae-4642-b47f-f14b5ea49bf1)

I try using `Burp Suite` to create a HTTP Request Post but the server does not response. Reading the hint they said `XML External Injection`, so I google it and understand this exploit. Also, in the source code it includes 2 `.js` files, reading the code, I understand that this website will has ability to handle the `XML` in HTTP Request. Reading the `xmlDetails[..].js` file, I understand that it uses `UTF-8 encoding`, and must include `<data>` tag to display the content. The other source code file just handles the usual request from the user. 

![source3](https://github.com/user-attachments/assets/94706a92-d683-4a7f-a613-fa00698967db)


First, I test by sending a HTTP Request with the XML format using the `<ID>` tag to the server with its value is from 1 to 3 to check whether the website responses with 3 blogs. And indeed, it displays each blog's content.

![test](https://github.com/user-attachments/assets/9f83e0de-f7fc-49c2-8cb9-2068675dd156)


Therefore, to display the `/etc/passwd`, I will use `XML TDT`, inside it I will call an `Entity()` that call the `/etc/passwd` file in the target server. Finally, using `<data>` and `<ID>` tags to display the content of the defined XML and we will get the flag.

![flag](https://github.com/user-attachments/assets/f4e34c1b-c35d-4714-8722-13410f7b42a4)
