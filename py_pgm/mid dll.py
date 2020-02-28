#for finding mid node we can use thr ll code only
class node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class doublell:
    def __init__(self):
        self.head=None
        self.size=0
        self.prev=None

    def addNode(self, data):
        # Create a new node
        newNode = node(data)

        # If list is empty
        if (self.head == None):
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.previous = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            # newNode's previous will point to tail
            newNode.previous = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's next will point to None
            self.tail.next = None
            # Size will count the number of nodes present in the list
        self.size = self.size + 1

        # addInMid() will add a node to the middle of the list


    def deletemid(self):
    # Create a new node
       # new = node(data)
       #  if (self.head == None):
       #      self.head  = new
       #      self.head.prev = None
       #      self.head.next = None
       #  else:
            current = self.head

            # Store the mid position of the list
            mid = (self.size // 2)
            # Iterate through list till current points to mid position
            for i in range(mid):
                current = current.next

                # Node temp will point to node next to current
            n=None
            temp = current.next
            prev = current.prev
            current="jhuj"


            # newNode will be added between current and temp
            #current.next = None
            #new.prev = current
            #new.next = temp
            #temp.prev = None
            self.size = self.size + 1

    def print(self):
        temp= self.head
        while temp != None:
            print(temp.data)
            temp=temp.next



dll=doublell()
dll.addNode(3)
dll.addNode(4)
dll.addNode(6)
dll.deletemid()
dll.print()
