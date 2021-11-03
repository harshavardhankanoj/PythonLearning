def count(l,ele):
    return l.count(ele)
print("Enter the elements of list:",end="")
l=list(map(int,input().split()))
ele=int(input("Enter the Element to be searched:"))
print(count(l,ele))