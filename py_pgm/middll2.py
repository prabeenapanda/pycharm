# Represent a node of doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class InsertMid:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        # addNode() will add a node to the list

    def addNode(self, data):
        # Create a new node
        newNode = Node(data)

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

    def addInMid(self, data):
        # Create a new node
        newNode = Node(data)

        # If list is empty
        if (self.head == None):
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.previous = None
            # tail's next point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # current will point to head
            current = self.head

            # Store the mid position of the list
            mid = (self.size // 2) if (self.size % 2 == 0) else ((self.size + 1) // 2)

            # Iterate through list till current points to mid position
            for i in range(1, mid):
                current = current.next

                # Node temp will point to node next to current
            temp = current.next
            temp.previous = current

            # newNode will be added between current and temp
            current.next = newNode
            newNode.previous = current
            newNode.next = temp
            temp.previous = newNode
        self.size = self.size + 1

        # display() will print out the nodes of the list

    def display(self):
        # Node current will point to head
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.data)
            current = current.next

        print()


dList = InsertMid()
# Add nodes to the list
dList.addNode(1)
dList.addNode(2)

print("Original list: ")
dList.display()

# Adding node '3' in the middle
dList.addInMid(3)
print("Updated List: ")
dList.display()

# Adding node '4' in the middle
dList.addInMid(4)
print("Updated List: ")
dList.display()

# Adding node '5' in the middle
dList.addInMid(5)
print("Updated List: ")
dList.display()