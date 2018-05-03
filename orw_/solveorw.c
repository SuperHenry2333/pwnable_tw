#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
int main(int argc, char const *argv[])
{
	
	int fd=open("./flag",O_RDONLY);
	char str[30];
	read(3,str,30);
	write(1,str,30);
	return 0;
}