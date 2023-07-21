# Challenge
Ta co file vuln.c nhu sau:

![challenge](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/32480630-28df-4f31-8b4e-ebfee0eea543)

# Disassemble vuln() function
Vì hàm nhập gets() được cho là nguy hiểm và thường không được khuyên để sử dụng nên ta sẽ phân tích input ở hàm vuln().

![disassemble_vuln](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/1a9b8957-1f56-4df5-bd09-94c740d9b3e0)


Đặt breakpoint ở hàm get() và hàm get_return_address(), sau đó ta sẽ run chương trình thử, thì chương trình sẽ bắt mình nhập. Mình sẽ nhập thử "AAAA..." trước

![after_input](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/e83560c9-6336-4dfe-a112-fe5cf1afad1c)


Sau khi xem mã Assembly của hàm main ta có thể thấy, địa chỉ trả về (return address) của hàm vuln() nằm ở địa chỉ 0x0804932f

![ret_addr_vuln](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/a36ef752-87fe-465b-a7a1-13eed3314416)

# Tìm địa chỉ hàm win() và overwrite return address
Vì vậy, dựa vào hình dưới, ta sẽ cần 48 bytes để overwrite: trong đó 44 bytes ký tự bất kỳ + 4 bytes hàm win()

![return_addr_vuln_](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/8d093855-0696-46f2-80b2-2b116ce4a93e)


Đây là địa chỉ hàm win()

![addr_Of_win_func]![addr_Of_win_func](https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/a4b8c1b5-9d2a-4fdf-87bf-bc2ed5ab043f)

# Flag solved
Bingoooo!!! Ta đã có flag của challenge

![flag]
(https://github.com/OceanTran999/picoCTF_writeup/assets/100577019/c38aa0b2-e42f-474c-bfca-b5bb8220a660)
