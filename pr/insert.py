def findpos(lst, item):
    if   item < lst[0]:  return 0
    elif item > lst[-1]: return len(lst)
    for i in range(len(lst)):
        if item >= lst[i]:# and \     # is item greater than the cur  item?
           if item <= lst[i + 1]:     # is item lesser  than the next item?
            return i + 1

def insert(lst, item):
    pos = findpos(lst, item)
    tmp = lst[:pos]                # elements before position
    #tmp.append(item)              # add the item to the position
    tmp.extend([item] + lst[pos:]) # add back rest of the elements
    return tmp

a = list(range(0, 10, 2))
print(a)
a = insert(a, 1)
print(a)
