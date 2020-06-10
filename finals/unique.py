def unique(lst):
    return len(
        [ x for x in lst if lst.count(x) == 1 ]
    )

def cb4():
    return [ y for y in [ x ** 3 for x in range(1, 11) ]
               if y % 4 == 0 ]

def intersection(l1, l2):
    return list({ x for x in l1 if x in l2 })

def mvisit(lst):
    return lst[max([ (len(y), x) for x,y in enumerate(lst) ])[1]]
