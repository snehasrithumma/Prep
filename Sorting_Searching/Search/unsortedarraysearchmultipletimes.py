def build_hash_table(arr):
    hashamp = {}
    for i, n in enumerate(arr):
        hashamp[n] = i
    return hashamp

def hash_table_search(hashamp, element):
    return hashamp.get(element, -1)


arr = [4, 2, 7, 1, 3, 6]
hash_table = build_hash_table(arr)
target = 3
print( hash_table_search(hash_table, target))

# the linear search is straightforward and works well for small arrays or a single search, 
# while more advanced techniques like hash tables or sorting can optimize searches for larger arrays or multiple searches.