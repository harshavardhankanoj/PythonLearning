def BinarySearch(l,element):
    length=len(l)
    s_list=sorted(l)
    low,high=0,length-1
    while low<=high:
        mid=(low+high)//2
        if s_list[mid]==ele:
            return mid
        elif s_list[mid]<ele:
            low=mid+1
        elif s_list[mid]>ele:
            high=mid-1
    return False
print("Enter the list")
l=list(map(int,input().split()))
ele=int(input("Enter the element to be searched:"))
print(BinarySearch(l,ele))