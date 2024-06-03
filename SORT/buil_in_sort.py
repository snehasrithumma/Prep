# To sort in-place:
a = [2, 1, 3]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# To return a sorted list:
x = sorted(a)
x = sorted(a, reverse=True)
print(x)
# To sort a dictionary:
a = {'d':4, 'a':1, 'c':3, 'b':2}
b = sorted(a.items(), key=lambda x: x[1]) # by value
c = sorted(a.items(), key=lambda x: x[0]) # by key
print(b)
print(c)
