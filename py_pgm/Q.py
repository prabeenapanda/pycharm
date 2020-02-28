queue = []
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue:")
print(queue)
# Removing elements from the queue
print("\nElements dequeued from queue:")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements:")
print(queue)


#DEQUEUE
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)

import queue
# Initializing a queue which should have 3 elements
q = queue.Queue(maxsize=3)
# qsize() give the maxsize
print(q.qsize())
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
# Return Boolean for Full queue
# mid=(q.qsize())//2
# q.put(mid,"d")
# print(q)
print("\nFull: ", q.full())
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())



