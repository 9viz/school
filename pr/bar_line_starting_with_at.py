### functional-eqsue {
with open("in") as f:
    ls = list(filter(lambda x: x[0] != "@", f.readlines()))

with open("out", "w") as f:
    f.writelines(ls)
### }

### iterative {
# ls = []
# with open("in") as f:
#     for i in f.readlines():
#         if i[0] != "@": ls.append(i)
#
# with open("out", "w") as f:
#     f.writelines(ls)
### }
