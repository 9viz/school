def search(item, lst):
    for n, i in enumerate(lst):
        if i == item: return n
    return -1
