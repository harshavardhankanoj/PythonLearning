from collections import OrderedDict
l=[]
for i in range(int(input())):
    l.append(input())
s=set(l)
dic=OrderedDict()
dic.values=0
dic.keys=""
print(len(s))
for i in l:
    if i in dic:
        dic[i]=int(dic[i])+1
    else:
        dic[i]=1
for k,v in dic.items():
    print(v,end=" ")