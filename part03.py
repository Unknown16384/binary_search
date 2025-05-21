import timeit
def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
def binary_search(arr, num):
    first = 0
    mid = len(arr) // 2
    last = len(arr) - 1
    while num != arr[mid] and first <= last:
        if num > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
    if first > last:
        return -1
    else:
        return mid
def compare(arr_len, index=-1):
    arr_new = [a for a in range(arr_len)]
    a = timeit.timeit(lambda: linear_search(arr_new, index), number=1000)
    b = timeit.timeit(lambda: binary_search(arr_new, index), number=1000)
    if a <= b:
        print(f'линейный поиск эффективнее на {1-a/b:.2%}')
    else:
        print(f'бинарный поиск эффективнее на {1-b/a:.2%}')

compare(10)
compare(15)
compare(100)
compare(10000)
