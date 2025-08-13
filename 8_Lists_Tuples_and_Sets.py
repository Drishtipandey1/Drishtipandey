
"""
Topic 8: Lists, Tuples, and Sets
-----------------------------------------
Theory:
- List: ordered, mutable, duplicates allowed. []
- Tuple: ordered, immutable. ()
- Set: unordered, unique elements only. {}
- Common operations: indexing, slicing, add/remove, unions/intersections.
"""

# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("banana")
fruits[1] = "mango"
print("list:", fruits, "| slice:", fruits[1:3])

# Tuples (immutable)
coords = (10, 20)
x, y = coords
print("tuple:", coords, "| x+y:", x+y)

# Sets (unique)
s1 = {1,2,2,3}
s2 = {3,4,5}
print("set s1:", s1)
print("union:", s1 | s2, "| intersection:", s1 & s2, "| difference:", s1 - s2)

# List comprehensions
squares = [n*n for n in range(6)]
unique_letters = set("cybersecurity")
print("squares:", squares, "| unique letters:", unique_letters)
