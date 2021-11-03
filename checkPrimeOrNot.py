#check enterd number is prime or composite
n=int(input("Enter the number to check prime or composite:"))
if(n==0):
    print("Neither prime nor composite")
elif(n==2 or n==3):
    print("Prime number")
for i in range(2,n):
    if(n%i==0):
         print("Composite")
         break
else:
    print("Prime number")