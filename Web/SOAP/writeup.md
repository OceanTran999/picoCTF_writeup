The challenge gives me a website with 3 blogs, when clicking each blog it doesn't happen, so I decide to read the website source code.

First, I saw there's a subdirectory named `/data`, and in order to upload it, I have to send HTTP POST method. Each block will contain a variable called `ID` with value `from 1 to 3`.



I try using `Burp Suite` to create a HTTP Request Post but the server does not response. Reading the hint they said `XML External Injection`, so I google it and understand this exploit.


Also, in the source code it includes 2 `.js` files, reading the code, I understand that this website will handle the `XML` in HTTP Request.


Reading this file, I understand that it uses `UTF-8 encoding`, and must include `<data>` tag to display the content.


First, I test sending to the server with the XML with the tag `<ID>` and its value to check whether the website responses with 3 blogs. And indeed, it displays each blog's content.


Therefore, to display the `/etc/passwd`, I will use `XML TDT`, inside it I will call an Entity that call the `/etc/passwd` in the target server. Finally, using `<data>` and `<ID>` tags to display the content of the defined XML and we will get the flag.