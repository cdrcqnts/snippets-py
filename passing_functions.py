print("G'day mate")

li = [1, 2, 3, 4, 5]


def div_two(n):
    return n % 2


print(list(filter(lambda n: n % 2, li)))
