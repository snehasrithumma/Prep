list2 = list
print(list2)
print(list)
list[0] = 10
print(list2)
print(list)
import copy
list3 = copy.deepcopy(list)
print(list3)
list[0] = 100
print(list3)
print(list)