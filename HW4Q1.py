# HW4Q1
# Merge sort vs. Insertion sort

from numpy import random
from time import time
from matplotlib import pyplot as plt
from statistics import mean

"""
https://www.geeksforgeeks.org/python-program-for-merge-sort/
https://www.geeksforgeeks.org/insertion-sort/
"""


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    midpoint = len(arr) // 2
    return merge(merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:]))


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


mergeTime = []
insertionTime = []
inputs = []
# loop through array of size 150
for n in range(1, 151):
    merge_small = []
    insertion_small = []

    array = [random.randint(0, 1000) for i in range(n)]
    a1 = array.copy()
    a2 = array.copy()

    time_first_merge = time()  # starting time for merge
    merge_sort(a1)
    time_last_merge = time()  # ending time for merge
    mtime_diff = time_last_merge - time_first_merge  # duration of merge sort

    time_first_insert = time()  # starting time for insertion
    insertionSort(a2)
    time_last_insert = time()  # ending time for insertion
    itime_diff = time_last_insert - time_first_insert  # duration of insertion sort

    merge_small.append(mtime_diff)
    insertion_small.append(itime_diff)

    inputs.append(n)
    mergeTime.append(mean(merge_small))
    insertionTime.append(mean(insertion_small))
    print("Test:", n)
    fastest = "Merge" if mtime_diff / n <= itime_diff / n else "Insertion"
    print("insertion:{}, merge:{}, {}  is faster ".format(itime_diff / n, mtime_diff / n, fastest))

plt.plot(inputs, mergeTime, label='Merge Sort')
plt.plot(inputs, insertionTime, label='Insertion Sort')
plt.xlabel("Size")
plt.ylabel("Time")
plt.legend()
plt.show()
