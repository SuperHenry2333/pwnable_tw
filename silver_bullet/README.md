# silver_bullet
## strncat()会在拼接完的字符串后面添加一个’\x00′
## 函数调用时栈的变化：
### call：把caller的下一条指令地址push
### 注意：push ebp由callee完成
### ret：把栈顶pop到eip
### 注意：pop ebp要由callee显式完成