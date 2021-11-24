from math import factorial


def fact():
    num = 1
    for i in {1, 2, 3, 4, 5}:
        yield i
        num += 1


print(fact())
for f in fact():
    print(factorial(f))
