def count_substring(string, sub_string):
    # count=0
    # lsub=len(sub_string)
    # for i in range(len(string)):
    #     if sub_string==string[i:i+lsub]:
    #         count+=1
    # return count
    c=0
    x=-1
    while x<len(string):
        z=string.find(sub_string,x+1)
        if z==-1:
            break
        c+=1
        x=z
    return c

            
        
            

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)