class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublell:
    def __init__(self):
        self.head=None

    def push(self, data):
        new = node(data)
        new.next = self.head
        new.prev = None
        if self.head is not None:
            self.head.prev = new
        self.head = new

    def append(self,data):#adding element at last
        new=node(data)
        if self.head == None:
           new.prev=None
           self.head=new
        else:
           temp=self.head
           while temp.next != None:
               temp=temp.next
           temp.next=new
           new.prev=temp
           new.next=None

    def prepend(self,data):#adding element at first
        new=node(data)
        if self.head == None:
            self.head=new
            new.prev=None
        else:
            self.head.prev=new
            new.next = self.head
            self.head=new
            new.prev=None

    def print(self):
        temp= self.head
        while temp != None:
            print(temp.data)
            temp=temp.next

dll=doublell()
dll.push(1)
dll.push(2)
dll.prepend(5)
dll.prepend(9)
dll.append(3)
dll.append(4)
dll.prepend(8)
dll.print()


