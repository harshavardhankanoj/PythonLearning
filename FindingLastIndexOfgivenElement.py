def index(l,ele):
    s_list=sorted(l)
    low,high=0,len(l)-1
    while low<=high:
        mid=(low+high)//2
        if s_list[mid]<ele:
            low=mid+1
        elif s_list[mid]>ele:
            high=mid-1
        else:
            if mid==len(l)-1 or s_list[mid+1]!=s_list[mid]:
                return mid
            else:
                low=mid+1
    return -1



print("Enter the elements of list:",end="")
l=list(map(int,input().split()))
ele=int(input("Enter the Element to be searched:"))
print(index(l,ele))