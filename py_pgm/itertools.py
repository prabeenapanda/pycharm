import itertools
import operator
data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
for each in result:
    print(each)
data = [5, 2, 6, 4, 5, 9, 1]
result = itertools.accumulate(data, max)
for each in result:
    print(each)
#Passing a function is optional.
data = [5, 2, 6, 4, 5, 9, 1]
result = itertools.accumulate(data)
for each in result:
    print(each)
#If no function is designated the items will be summed
shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for each in result:
    print(each)
result = itertools.combinations(shapes, 3)
for each in result:
    print(each)
result = itertools.combinations_with_replacement(shapes, 2)
for each in result:
    print(each)
#itertools.count(start=0, step=1)
for i in itertools.count(10,3):
    print(i)
    if i > 20:
        break
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
for color in itertools.cycle(colors):
    print(color)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
shapes = ['circle', 'triangle', 'square', 'pentagon']
result = itertools.chain(colors, shapes)
for each in result:
    print(each)
shapes = ['circle', 'triangle', 'square', 'pentagon']
selections = [True, False, True, False]
result = itertools.compress(shapes, selections)
for each in result:
    print(each)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.takewhile(lambda x: x<5, data)
for each in result:
    print(each)
robots = [{
    'name': 'blaster',
    'faction': 'autobot'
}, {
    'name': 'galvatron',
    'faction': 'decepticon'
}, {
    'name': 'jazz',
    'faction': 'autobot'
}, {
    'name': 'metroplex',
    'faction': 'autobot'
}, {
    'name': 'megatron',
    'faction': 'decepticon'
}, {
    'name': 'starcream',
    'faction': 'decepticon'
}]
for key, group in itertools.groupby(bots, key=lambda x: x['faction']):
    print(key)
    print(list(group))
colors = ['red', 'orange', 'yellow', 'green', 'blue',]
few_colors = itertools.islice(colors, 2)
for each in few_colors:
    print(each)
alpha_data = ['a', 'b', 'c']
result = itertools.permutations(alpha_data)
for each in result:
    print(each)
num_data = [1, 2, 3]
alpha_data = ['a', 'b', 'c']
result = itertools.product(num_data, alpha_data)
for each in result:
    print(each)
for i in itertools.repeat("spam", 3):
    print(i)
data = [(2, 6), (8, 4), (7, 3)]
result = itertools.starmap(operator.mul, data)
for each in result:
    print(each)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
alpha_colors, beta_colors = itertools.tee(colors)
for each in alpha_colors:
    print(each)
print('..')
for each in beta_colors:
     print(each)
colors = ['red', 'orange', 'yellow', 'green', 'blue',]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
for each in itertools.zip_longest(colors, data, fillvalue=None):
    print(each)
#https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8
#website to know everything about itertools