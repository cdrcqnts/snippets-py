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
