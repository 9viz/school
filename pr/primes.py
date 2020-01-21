def prime(x):
    if x in (1, 2):
        return False
    elif x != 2 and x % 2 == 0:
        return False

    for i in range(3, x):
        if x % i == 0: return False
    return True

[print(i) for i in range(1, 101) if prime(i)]
