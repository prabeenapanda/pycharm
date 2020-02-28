class Stack:
    def __init__(self ,items = []):
        self.items = items

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def last(self):
        return self.items[len(self.items) - 1]

    def first(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return format(self.items)

names = Stack(['Amar', 'Akbar', 'Anthony', 'Ram'])

print(names)
print(names.first())
print(names.last())
print(names.size())
print(names.pop())
print(names)
names.push('Sanjib')
print(names)
