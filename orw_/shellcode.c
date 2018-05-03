int fd=open("/home/orw/flag",0);
char flag[20];
read(fd,flag,20);
write(1,flag,20);