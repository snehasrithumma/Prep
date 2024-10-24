# list2 = list
# print(list2)
# print(list)
# list[0] = 10
# print(list2)
# print(list)
# import copy
# list3 = copy.deepcopy(list)
# print(list3)
# list[0] = 100
# print(list3)
# print(list)


nums = [1,3, 2, 8, 7, 9]
square = list(map(lambda x: x**2, nums))
print(square)

even_ = list(filter(lambda x: x%2 == 0, nums))
print('even - '+even_)

from functools import reduce 
val = reduce(lambda x, y: x+y , nums, 0)
print(val)