from collections import deque  
#initialization
list = ["a","b","c"]  
deq = deque(list)
print(deq)
deq.append('g')
deq.appendleft('z')

print(deq)

deq.pop()
deq.popleft()
print(deq)

#  namedtuple
from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')  
s1 = Student('Peter', 'James', '13')  
print(s1.fname) 

import collections

dictionary1 = { 'a' : 1, 'b' : 2 }  
dictionary2 = { 'c' : 3, 'b' : 4 }  
chain_Map = collections.ChainMap(dictionary1, dictionary2)  
print(chain_Map.maps)  

# OrderedDict

from collections import OrderedDict  
order = OrderedDict()  
order['a'] = 1  
order['b'] = 2  
order['c'] = 3  
print(order)  

#unordered dictionary
unordered=dict()
unordered['a'] = 1  
unordered['b'] = 2  
unordered['c'] = 3 
print("Default dictionary", unordered)


values = {'a': 11, 'b': 2, 'c': 31} 
sorted_dict = dict(sorted(values.items(), key = lambda x: x[1]))
print(sorted_dict)