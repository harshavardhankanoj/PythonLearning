# To open the file " open('File name','r')"
"""
r->read the file
w->write the file
a->append
rb->read the binary file
wb->write the binary in the file
"""
#Lets open file
f1=open("MyData",'r')
print(f1.read(),end='')
f2=open('abc','w')
f2.write("Hi.....................................................")
   