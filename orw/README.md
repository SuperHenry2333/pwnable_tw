# orw
## 注意：
### 1.32位和64位系统调用号不同
### 2.gcc编译32位程序 -m32
### 3.C语言中的open等函数不是直接系统调用，是经过包装的
### 4.pwntools:
#### i.用gdb.attach()时，脚本后面要interactive(),否则程序会退出
#### ii.contex(arch='i386',log_level='debug')
#### iii.快速得到字符串的trick
		call open_ebx
		.ascii "/home/orw/flag"
    	.byte 0
	open_ebx:
		pop ebx
#### iv.asm("asm code")把汇编代码转为字节码
### 5.sysenter相当于int 0x80
## 疑问：
在open()的int 0x80之前，eax怎么是0x127？