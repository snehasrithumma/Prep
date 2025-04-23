s1 = {1,2,3,4,5, 6}
print(type(s1))
s1.add(9)
s1.remove(6)
s1.discard(10)     # No error if 10 is not found
s1.pop()          # Removes a random element
s1.clear()        # Empties the set
print(s1)

s = {1, 2, 3, 4} 
# Set Operations
print(s.union(s1))
print(s & s1)
print(s - s1)
print(s ^ s1)
print(s <= s1)
print(s1 >= s)

# Set Comprehensions

print(s)
squared = {x**2 for x in s}
print(squared)

# Frozen Set (Immutable Set)
fs = frozenset([1, 2, 3])
fs.add(4)  # ❌ TypeError (immutable)

# #  Edge Cases
# ✔ Set of immutable elements only ({1, 2, (3, 4)} ✅, {1, [2, 3]} ❌)
# ✔ Removing non-existent elements → remove() throws an error, discard() does not
# ✔ Iteration order is arbitrary
# ✔ Sets don’t support indexing (s[0] ❌)

# # 8️⃣ When to Use Sets?
# ✅ Fast lookups (checking membership in O(1))
# ✅ Removing duplicates from a list
# Mathematical operations (Union, Intersection, Difference)