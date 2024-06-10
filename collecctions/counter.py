# Counter is a built-in data structure which is used to 
# count the occurrence of each value present in an array or list.

from collections import Counter  
list = [1,2,2,4,5,6,7]  
answer=Counter()
answer = Counter(list)  
print(answer[2])  
