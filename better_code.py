""" VARIABLE ASSIGNMENT WITH TERNARY CONDITION
"""

condition = True

# if condition:
#     x = 1
# else:
#     x = 0

x = 1 if condition else 0

print(x)

""" IMPROVE READABILITY OF LARGE NUMBERS
"""

num1 = 10_000_000_000  # underscore does not affect the value
num2 = 100_000_000

total = num1 + num2

print(f"{total:,}")  # print total as an f-string, use colons to format output


""" OPENING AND CLOSING RESOURCES (FILES, DB, ...) WITH CONTEXT MANAGER
"""

with open("./test.txt", "r") as f:
    file_content = f.read()

# no need to .close() the file

words = file_content.split(" ")
word_count = len(words)
print(word_count)

""" ENUMERATE WITH CUSTOM INDEX STARTING POINT
"""
names = ["Anna", "Bob", "Charles"]
names_indexed = [(i, n) for i, n in enumerate(names, start=1)]
print(names_indexed)

""" ITERATE OVER MULTIPLE LISTS PAIRWISE
"""
animals = ["Dog", "Cat", "Bird", "Worm"]
legs = [4, 4, 2, 0]
fur = [1, 1, 0, 0]
animals_zipped = [(a, l, f) for a, l, f in zip(animals, legs, fur)]
print(animals_zipped)

""" UNPACKING
"""

# normal
items = (1, 2, 3, 4, 5, 6, 7)
print(items)

# unpacking
a, _, *c, d = items
print(a)
print(c)
print(d)

""" LIST VALID ATTRIBUTES / METHODS
"""

from datetime import datetime

print(dir(datetime))
