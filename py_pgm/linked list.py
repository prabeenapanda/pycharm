class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedl:
    def __init__(self):
        self.head=None
    def traverse(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            temp=self.head
            while(temp != None):
                print(temp.data,end=" ")
                temp=temp.next

    def insertlast(self,value):
        New=node(value)
        if(self.head==None):
            self.head=New
        else:
            temp=self.head
            while(temp.next != None):
                temp=temp.next
            temp.next=New
    #
    def insertfirst(self,value):
        New=node(value)
        temp=self.head
        self.head=New
        New.next=temp

    def deletefirst(self):
        if(self.head == None):
            print("nothing to delete")
        else:
            #temp=self.head(it will store the first node)
            self.head=self.head.next#python automatically deletes the node which don't have reference

    def deletelast(self):
        if (self.head == None):
            print("nothing to delete")
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None






myll=linkedl()
myll.insertlast(10)
myll.insertlast(20)
myll.insertlast(30)
myll.insertfirst(2)
myll.insertfirst(4)
myll.traverse()
print("done")
myll.deletefirst()
myll.traverse()
print("done")
myll.deletelast()
myll.traverse()
print("done")
#myll.Middlenode()
myll.traverse()