# hacknote
## use after free
free之后，为对指针处理，可以用新的堆进行覆盖，并更改note的指针到got表，泄漏libc地址。
然后free，再用新的堆覆盖，更改函数指针到system，更改note为"||sh"或";sh"
## fastbin中后free的堆在下次malloc时先被使用
## fastbin不合并相邻堆
## "||sh"或";sh"