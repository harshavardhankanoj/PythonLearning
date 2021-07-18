j=float(input("Enter 1st number:"))
k=int(input("Enter 2nd number:"))
l=int(input("Enter 3rd number:"))
def greater(j,k,l):
	large=0
	if (j>k) and (j>l):
		print(j," is greater")
		large=j
	elif (k>j) and (k>l):
		print(k," is greater")
		larger=k
	else:
		print(l,"is greater")
		large=l
	return large
print("large=",greater(j,k,l))

