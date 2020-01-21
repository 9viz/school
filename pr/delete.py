def find(item, lst):
    def helper(lst, item, low, high):
        if low > high: return -1
        mid = (low + high) // 2
        if   item > lst[mid] : return helper(lst, item, low + 1, high)
        elif item < lst[mid] : return helper(lst, item, low, high - 1)
        else                 : return mid
    return helper(lst, item, 0, len(lst) - 1)

def delete(item, lst):
    pos = find(item, lst)
    if pos < 0: return -1
    del lst[pos]
    return lst

lst = list(range(1, 10, 2))
lst = delete(1, lst)
print(lst)
