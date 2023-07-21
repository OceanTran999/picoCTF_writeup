# Challenge
Ta có file vuln.c của chall như sau:

![Chall_code](https://github.com/OceanTran999/PicoCTF_BufferOverflow2/assets/100577019/12cd6615-0a70-4313-9cbc-2359ebd524fd)

# Check file
Đầu tiên ta xem dạng file và Endian của file

![Readelf](https://github.com/OceanTran999/PicoCTF_BufferOverflow2/assets/100577019/aefa4e90-ab2a-46c7-a5b9-2a8eb485d943)


Sau đó kiểm tra file có bị giới hạn gì không:

![Checksec](https://github.com/OceanTran999/PicoCTF_BufferOverflow2/assets/100577019/185c150a-530c-45bf-9dc1-84bc3bd6c477)

# Disassemble vuln() and win() function
Đầu tiên ta sẽ xem mã Assem của hàm vuln(), ta thấy trước khi gọi hàm Gets(), vị trí (ebp – 0x6c = ebp – 108) sẽ được đưa vào stack => đây có thể là nơi ta nhập input vào

![Disassemble_vuln](https://github.com/OceanTran999/PicoCTF_BufferOverflow2/assets/100577019/df916651-cea9-42e3-8d58-3e6cdee4776e)


Tiếp theo, ta kiểm tra hàm win() để xác định vị trí của 2 biến args1 và args2, thì thấy giá trị 0xcafef00d ở vị trí ebp+8 => Ta cần 4 byte ký tự bất kỳ + 0xcafef00d + 0xf00df00d

![Disassemble_win](https://github.com/OceanTran999/PicoCTF_BufferOverflow2/assets/100577019/3077476b-c451-4d09-bf6b-a61ddd824330)


# Stack
Ta có stack như sau:

![stack](https://github.com/OceanTran999/PicoCTF_BufferOverflow2/assets/100577019/e72d04c9-3937-4fcc-bd7d-bf631741cf2b)

=> Payload để overwrite: 116 bytes (108 bytes bất kỳ + 4 bytes ebp + 4 byte win()) + 4 bytes bất kỳ + 0xcafef00d + 0xf00df00d


# Flag solved
Yayyy!!! Ta đã tìm ra được flag

![flag](https://github.com/OceanTran999/PicoCTF_BufferOverflow2/assets/100577019/0f862d1e-bc65-4656-8f3b-4389dbd7e6ee)
