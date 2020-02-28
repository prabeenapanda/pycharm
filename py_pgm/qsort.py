import queue
q = queue.Queue(maxsize=3)
q.put(1)
q.put(6)
q.put(2)
#print(q)
s = q.qsize()
#new = queue.Queue(maxsize=3)
while s:
    a=q.get()
    while s-1:
        b=q.get()
        if a < b:
            q.put(b)
        else:
            q.put(a)
    q.put(a)
print(q)
