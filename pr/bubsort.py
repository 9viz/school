from random import randint

def bubsort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = [randint(1, 100) for _ in range(100)]
print(a)
print(bubsort(a))
