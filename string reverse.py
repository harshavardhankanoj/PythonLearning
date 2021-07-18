st=input ("Enter the string:")
print (len(st))
print (st[::-1])
i=len(st)-1
while i>=0:
	print (st[i],end='')
	i-=1