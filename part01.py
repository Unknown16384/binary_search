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