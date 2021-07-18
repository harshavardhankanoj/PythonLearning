def max_num(n1,n2,n3):
	if n1==n2==n3 :
		print("Numers are equal")
	elif n1>n2 and n1>n3 :
		print(n1,("is greater"))
	elif n2>n1 and n2>n3 :
		print (n2,("is greater"))
	else:
		print (n3,("is greater"))
n1=input ("Enter 1st number:")
n2=input ("Enter 2nd number:")
n3=input ("Enter 3rd number:")
max_num(n1,n2,n3)