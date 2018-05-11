# dubble sort
## 漏洞
### 1.read(int fd,char *buf,unsigned int size)不在字符串buf后面添加'\x00'
### 2."%u"匹配"+"或"-"不会修改内存
## 技巧
### 1.需要libc地址时，可以gdb在附近地址寻找类似libc地址的内存
### 2.在gdb中查找字符串find "str"
### 3.指定libc
#### a)gdb中set environment LD_PRELOAD=...
#### b)脚本中p=process("./dubblesort",env={"LD_PRELOAD":"./libc_32.so.6"})
