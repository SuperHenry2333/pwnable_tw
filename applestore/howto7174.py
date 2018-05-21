lst=[0xc7,0x12b,0x1f3,0x18f]
target=7174

a=[[0 for i in range(5)] for i in range(7175)]
a[0][0]=1
# print a
for i in range(0xc7,7175):
	# print i
	for j in range(1,5):
		if(i>=lst[j-1]):
			if(a[i-lst[j-1]][0]==1):
				for k in range(4):
					a[i][k]=a[i-lst[j-1]][k]
				a[i][j]=a[i][j]+1
				print a[i],i,j
				break

print a[0xc6]
