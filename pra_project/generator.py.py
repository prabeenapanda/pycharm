# What is the generator, what are the ways to create it?
# Generators are simple functions which return an iterable set of items, one at a time. So they are much more memory efficient when dealing with large datasets

import memory_profiler  as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSc', 'Arts', 'Business']



def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice( )
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in random(num_people):
        yield {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
print('Memory (Before: {}MB)'.format(str(mem_profile.memory_usage())))

t1 = time.time()
people = people_generator(1000000)
# people = people_list(1000000)
t2 = time.time()

print('Memory (After: {}MB)'.format(str(mem_profile.memory_usage())))
print('Took (After: {} Seconds) '.format(t2-t1))
