# Challenge
Ta co file vuln.c nhu sau:

![challenge](https://github.com/OceanTran999/PicoCTF2022_bufferoverflow1/assets/100577019/96bb049b-4029-4657-b651-04061cc04de6)

# Disassemble vuln() function
Vì hàm nhập gets() được cho là nguy hiểm và thường không được khuyên để sử dụng nên ta sẽ phân tích input ở hàm vuln().

![disassemble_vuln](https://github.com/OceanTran999/PicoCTF2022_bufferoverflow1/assets/100577019/2b51e57f-839d-4b0d-b08e-3b230a942de6)


Đặt breakpoint ở hàm get() và hàm get_return_address(), sau đó ta sẽ run chương trình thử, thì chương trình sẽ bắt mình nhập. Mình sẽ nhập thử "AAAA..." trước

![after_input](https://github.com/OceanTran999/PicoCTF2022_bufferoverflow1/assets/100577019/33709561-760a-4fa7-9ca7-edd5e734201c)


Sau khi xem mã Assembly của hàm main ta có thể thấy, địa chỉ trả về (return address) của hàm vuln() nằm ở địa chỉ 0x0804932f

![ret_addr_vuln](https://github.com/OceanTran999/PicoCTF2022_bufferoverflow1/assets/100577019/a481be98-84f7-44c4-926d-6a41ed620667)

# Tìm địa chỉ hàm win() và overwrite return address
Vì vậy, dựa vào hình dưới, ta sẽ cần 48 bytes để overwrite: trong đó 44 bytes ký tự bất kỳ + 4 bytes hàm win()

![return_addr_vuln_](https://github.com/OceanTran999/PicoCTF2022_bufferoverflow1/assets/100577019/358c37d8-3c58-4a66-b5eb-be3415a3737b)


Đây là địa chỉ hàm win()

![addr_Of_win_func](https://github.com/OceanTran999/PicoCTF2022_bufferoverflow1/assets/100577019/286209ba-4564-488a-98be-09070ba10753)

# Flag solved
Bingoooo!!! Ta đã có flag của challenge

![flag](https://github.com/OceanTran999/PicoCTF2022_bufferoverflow1/assets/100577019/d7d812b9-875b-4928-a4d4-ceeba3ed6e44)
