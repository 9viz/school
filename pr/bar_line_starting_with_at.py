with open("in") as f:
    ls = list(filter(lambda x: x[0] != "@", f.readlines()))

with open("out", "w") as f:
    f.writelines(ls)
