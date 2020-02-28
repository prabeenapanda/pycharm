
# Python program to delete a node in a linked list
# at a given position

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Given a reference to the head of a list

    # and a position, delete the node at a given position
    def traverse(self):
        if (self.head == None):
            print("linked list is empty")
        else:
            temp = self.head
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
    def deleteNode(self, position):

        # If linked list is empty
        if self.head == None:
            print("empty ll")

        # If head needs to be removed
        if position == 0:
            self.head = self.head.next

        temp = self.head
            # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

            # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        new = temp.next.next
        temp.next = None
        temp.next = new

    def insertAfter(self,position, data):
        # 1. check if the given prev_node exists
        new = Node(data)
        if position == None:
            print("The given previous node must in LinkedList.")

        #  2. Create new node &
        #  3. Put in the data
        else:
             temp = self.head
             for i in range(position):
                  temp = temp.next
             last= temp.next
             temp.next = new
             new.next=last

myll=LinkedList()
myll.push(5)
myll.push(4)
myll.push(2)
myll.push(3)
myll.push(1)
myll.deleteNode(3)
myll.traverse()
print("done")
myll.insertAfter(2,7)
myll.traverse()