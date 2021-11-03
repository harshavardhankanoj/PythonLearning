s1='listen'
s2='silent'
fl=[]
sl=[]
for i,j in zip(s1,s2):
    fl.append(i)
    sl.append(j)
fl.sort()
sl.sort()
print(fl==sl)