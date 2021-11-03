
from singleLinkedList import insertBegin


class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
def printList(head):
    ptr=head
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.link
    
def insertEnd(head,data):
    if head==None:
        return Node(data)
    ptr=head
    while ptr.link!=None:
        ptr=ptr.link
    ptr.link=Node(data)
    return head
    
def delFirstNode(head):
    if head==None:
        return None
    else:
        return head.link
    
def delLastNode(head):
    if head==None:
        return None
    if head.link==None:
        return None
    ptr=head
    while ptr.link.link!=None:
        ptr=ptr.link
    ptr.link=None
    return head   

def addElement_InSortedList(head,ele):
    ptr=head
    temp=Node(ele)
    if ptr==None:
        return temp 
    elif ptr.data>ele:
        return insertBegin(head,ele)
    else:
        ptr=head
        while ptr.link!=None and ptr.link.data<ele:
            ptr=ptr.link
        temp.link=ptr.link
        ptr.link=temp
        return head
def reverse(head):
    ptr1=head
    ptr2=head
    
    
head=None
head=insertEnd(head,1)
head=insertEnd(head,2)
head=insertEnd(head,3)
head=insertEnd(head,4)
head=delFirstNode(head)
head=delLastNode(head)
printList(head)

