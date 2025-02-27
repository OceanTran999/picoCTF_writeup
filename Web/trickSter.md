![chal](https://github.com/user-attachments/assets/44d965fd-11e3-488e-a60e-cce72b3addd8)


The challenge gives the an upload PNG file. W1hen uploading a random file which is not a PNG file, it will give an error contains a hexa number.

![web](https://github.com/user-attachments/assets/6794a11b-2395-4a10-b191-d7c8106bd974)


I search Google and found that it's called `file's magic number`, so if I change the first bytes of a file to PNG file's magic number, I will bypass this filter, right?

![change_file](https://github.com/user-attachments/assets/575bce38-daed-46aa-8a87-811cb2c14e93)


![success1](https://github.com/user-attachments/assets/436e7729-222b-471f-a692-325796cc8503)


And great!!! We've just bypassed the first filter. The second filter is the file must have `.png` extension, or else it will return the error. At first, I tried to use the reverse shell payload of PentestMonkey and change it from `.php` to `.php.png`, but it seems the payload did not execute....

![fail1](https://github.com/user-attachments/assets/291e1467-50d7-44b1-abe1-07dbf8c2035b)


But, when I use the `.php` file and change the file's magic number, then upload again, the file really execute on the server although having error about file name.

![fail2](https://github.com/user-attachments/assets/e13e6ad1-9b7b-432e-b0bc-5aafe87d6dc4)


The next case I tried is change `.png` to `.png.php` and sent to server. And when accessing to that URL contains the name of PHP file, I saw that I successfully made a RCE.

![test3](https://github.com/user-attachments/assets/b007d1f8-7ea8-41ee-b7a1-82d4f61b73f9)


![success3](https://github.com/user-attachments/assets/925008d9-28ea-4daf-9a52-6b90c27cf258)


In order to save time, I use `find` command to search the flag through `.txt` file.

![find_file](https://github.com/user-attachments/assets/63a31b41-c410-4544-9aec-99315aa88690)


![flag](https://github.com/user-attachments/assets/b53adb3e-52d0-4b5a-9941-28c07557aca8)
