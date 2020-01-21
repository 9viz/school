def bs(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if key > arr[mid]:
        return bs(arr, key, low + 1, high)
    elif key < arr[mid]:
        return bs(arr, key, low, high - 1)
    else:
        return mid

arr = list(range(1, 10, 2))
print(arr)
print(bs(arr, 0, 0, len(arr) - 1)) # -1
print(bs(arr, 3, 0, len(arr) - 1)) #  1
