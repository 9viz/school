q = []
f = r = -1
c = "y"

print("1. enqueue", "2. dequeue", "3. display", sep="\n")
while c[0].lower() == "y":
    ch = input(">> ")
    if ch == "1":
        if f == r == -1 : f = r = 0
        else            : r += 1
        q.append(int(input("enter number: ")))
    elif ch == "2":
        if f == r == -1:
            print("underflow")
            continue
        q.pop(f)   # f will always be one
        r -= 1
    elif ch == "3":
        for n, i in enumerate(q):
            print(i,
                  (n == f and "<- front\n") or \
                  (n == r and "<- rear\n")  or \
                  "\n", end="")
    else:
        c = input("do u want to continue [y/n]? ")
