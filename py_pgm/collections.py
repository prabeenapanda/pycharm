from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import ChainMap
from collections import namedtuple
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt)
cn = Counter({1:3,2:4})
#print(list(cn.elements()))
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt.most_common())
cnt = Counter({1:5,2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])
print(nums['one'])
count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
#print(names_list)
for names in names_list:
    count[names] += 1
print(count)
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
print(od)
# for key, value in od.items():
#     print(key, value)
list = ["a","b","c"]
deq = deque(list)
print(deq)
deq.append("d")
deq.appendleft("e")
print(deq)
deq.pop()
deq.popleft()
print(deq)
list = ["a","b","c"]
deq = deque(list)
print(deq)
print(deq.clear())
list = ["a","a","b","c"]
deq = deque(list)
print(deq.count("a"))
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
print(chain_map['a'])
dict2['c'] = 5
print(chain_map.maps)
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.lname)
s2 = Student._make(['Adam','joe','18'])
print(s2)
s2 = s1._asdict()
print(s2)
s2 = s1._replace(age='14')
print(s1)
print(s2)