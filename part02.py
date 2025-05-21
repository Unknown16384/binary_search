from random import randint
from part01 import binary_search
arr = []
for _ in range(100):
    arr.append(randint(1, 100))
arr.sort()

print(binary_search(arr, 10))
print(binary_search(arr, 40))
print(binary_search(arr, 77))