a=[]
n=int(input("Enter the number of Elements:"))
for i in range(n):
	ele=int(input())
	a.append(ele)
print("List is:",a)
x=int(input("Enter the elemet to be searched:"))
status=False
for i in range(n):
	if x==a[i]:
		print("Element",x,"found at Index:", i)
		status=True
if status==False:
	print("Element did not find:")