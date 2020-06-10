def bsearch(lst, key, low, high):
    if low > high:
        return -1
    mid = (low+high) // 2
    if lst[mid] == key:
        return mid
    elif lst[mid] < key:
        return bsearch(lst, key, low + 1, high)
    else:
        return bsearch(lst, key, low, high - 1)
