# Deque is an optimal version of list used for inserting and removing items.
#  It can add/remove items from either start or the end of the list.
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


# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# The Namedtuple() solves a very major problem in the field of computer science. 
# Usual tuples need to remember the index of each field of a tuple object, 
# however, namedtuple() solves this by simply returning with names for each position in the tuple.
# In the following code, an index is not required to print the name of a student rather passing an attribute is sufficient for the required output.

#  namedtuple
from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')  
s1 = Student('Peter', 'James', '13')  
print(s1.fname) 


# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# ChainMap

# ChainMap combines a lot of dictionaries together and returns a list of dictionaries. 
# ChainMaps basically encapsulates a lot of dictionaries into one single unit with no restriction on the number of dictionaries.

import collections

dictionary1 = { 'a' : 1, 'b' : 2 }  
dictionary2 = { 'c' : 3, 'b' : 4 }  
chain_Map = collections.ChainMap(dictionary1, dictionary2)  
print(chain_Map.maps)  


# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# OrderedDict

# OrderedDict is a dictionary that ensures its order is maintained.
# For example, if the keys are inserted in a specific order, then the order is maintained. 
# Even if you change the value of the key later, the position will remain the same.

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