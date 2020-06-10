# explanation: https://www.programiz.com/dsa/insertion-sort

def sort(a):
    n = len(a)
    for i in range(1, n):
        k = a[i]
        j = i - 1
        while j >= 0 and k < a[j]:
            a[j+1] = a[j]
            j -= 1
        else:
            a[j+1] = k
    return a
