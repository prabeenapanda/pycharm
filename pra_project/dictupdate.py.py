l1 = {1: 'One' ,2: 'Three'}

# Update using Key
l1[1] = 'Onee'
print(l1)

# Update using update method
l2 = {1: 'One' ,2: 'Two'}
l1.update(l2)
print(l1)