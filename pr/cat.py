# not a kitty cat

with open("app", "a") as a:
    with open("in") as i:
        a.write(i.readlines())
