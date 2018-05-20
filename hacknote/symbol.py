from pwn import *
e=ELF('/lib/i386-linux-gnu/libc-2.23.so')
# print hex(e.address)
# print hex(e.symbols['malloc'])
print hex(e.symbols['system'])
# print hex(e.symbols['puts'])
# print hex(e.symbols['system']-e.symbols['fread'])
# print hex(0x45390-0x6e1a0)