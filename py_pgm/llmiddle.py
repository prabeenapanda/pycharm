# Node class
class node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Function to get the middle of
    # the linked list
    def traverse(self):
        if (self.head == None):
            print("linked list is empty")
        else:
            temp = self.head
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
    def Middlenode(self):
        slow = self.head
        fast = self.head

        if self.head != None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next
            print("The middle element is: ", slow.data)

    def Midinsert(self, value):  # with deleting the mid node
        slow = self.head
        fast = self.head
        new = node(value)
        prev = None

        if self.head != None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = new
            new.next = slow.next
            slow.next = new

    def Minsert(self, value):  # without deleting the mid node
        slow = self.head
        fast = self.head
        new = node(value)

        if self.head != None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next
            new.next = slow.next
            slow.next = new

    def Middelete(self):  # with deleting the mid node
        slow = self.head
        fast = self.head
        prev = None

        if self.head != None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = slow.next

        # Driver code


myll= LinkedList()
myll.push(5)
myll.push(4)
myll.push(2)
myll.push(3)
myll.push(1)
myll.Middlenode()
myll.Midinsert(0)
myll.traverse()
print("done")
myll.Minsert(9)
myll.traverse()
print("done")
myll.Middelete()
myll.traverse()
