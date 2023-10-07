# Challenge
Ta có file vuln.c của chall như sau:

![Chall_code](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/0eed0485-b54f-4d61-995c-8910e18dbcfd)

# Check file
Đầu tiên ta xem dạng file và Endian của file

![Readelf](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/01a7c10d-a2ac-4b13-ba90-5245c539defe)


Sau đó kiểm tra file có bị giới hạn gì không:

![Checksec](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/d6d0d0eb-d950-4169-aa78-25a2363e05be)

# Disassemble vuln() and win() function
Đầu tiên ta sẽ xem mã Assem của hàm vuln(), ta thấy trước khi gọi hàm Gets(), vị trí (ebp – 0x6c = ebp – 108) sẽ được đưa vào stack => đây có thể là nơi ta nhập input vào

![Disassemble_vuln](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/b0e34bdc-aa58-4595-bbca-15f59ff097e9)


Tiếp theo, ta kiểm tra hàm win() để xác định vị trí của 2 biến args1 và args2, thì thấy giá trị 0xcafef00d ở vị trí ebp+8 => Ta cần 4 byte ký tự bất kỳ + 0xcafef00d + 0xf00df00d

![Disassemble_win](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/0a750cea-e7d7-4433-9212-84301ba17b6a)


# Stack
Ta có stack như sau:

![stack](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/fed7d8b4-460e-4f51-a288-d5a33b9c458d)

=> Payload để overwrite: 116 bytes (108 bytes bất kỳ + 4 bytes ebp + 4 byte win()) + 4 bytes bất kỳ + 0xcafef00d + 0xf00df00d


# Flag solved
Yayyy!!! Ta đã tìm ra được flag

![flag](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/8371954f-9f80-4285-b838-7db244aca445)
