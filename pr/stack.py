c   = "y"
top = -1
s   = []

print("1. push", "2. pop", "3. peek",
      "4. display", sep="\n")

while c[0].lower() == "y":
    ch = input(">> ")
    if ch == "1":
        top += 1
        s.append(int(input("enter number: ")))
    elif ch == "2":
        if top < 0:
            print("underflow")
            continue
        s.pop(top)
        top -= 1
    elif ch == "3":
        print(s[top], "<- top")
    elif ch == "4":
        for n, i in enumerate(s[::-1]):
            print(i,
                  "<- top\n" if n == 0 else "\n",
                  end="")
    else:
        c = input("do u want to continue [y/n]? ")
