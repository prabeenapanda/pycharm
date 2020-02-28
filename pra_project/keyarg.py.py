# What are keyword arguments? Give an exampleWhat are keyword arguments? Give an example
# In python functionas can be called with argumants name with their respective values irrespective of their positions.

def calc_area(length, breadth):
    return length * breadth

area1 = calc_area(length=100, breadth=50)
area2 = calc_area(breadth=50, length=100)
area3 = calc_area(100,50)
print(area1, area2, area3)

