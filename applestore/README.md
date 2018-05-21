# applestore

## 步骤
先写个动态规划，达到7174，然后iphone8结构体在栈上，cart()里读取输入时把name地址改到got表，泄漏libc地址，然后通过libc的environ泄漏栈地址，在delete函数中，把ebp改到got.atoi+22，在handler中改变atoi的地址到system，顺便带上‘||sh’，成功！
## environ包含栈地址，peda种p environ可以看到这个值，脚本中e.symbol['environ']查找environ偏移
## delete的巧妙使用，这个用法真是绝了，我刚开始想不出怎么用，参考了别人的解法