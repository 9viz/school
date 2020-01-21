import timeit

def num2list(x):
    n = []
    while x != 0:
        n.append(x % 10)
        x //= 10

    # the order doesnt matter since addition is commutative
    return n

def happy(x):
    s = 0
    for i in num2list(x):
        s += i * i
    if   s == 1: return True
    elif s <= 9: return False
    return happy(s)

print(timeit.timeit("[i for i in range(100) if happy(i)]", setup="from __main__ import happy, num2list", number=1))
