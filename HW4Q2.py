# HW4Q2
# Hybrid sorting

from numpy import random
from time import time
from matplotlib import pyplot as plt

"""
https://www.geeksforgeeks.org/timsort/
"""


def calcMinRun(n):
    r = 0
    while n >= K:
        r |= n & 1
        n >>= 1
    return n + r


def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size


k_size = []
time_list = []
for n in range(1, 151):
    K = n
    arr = [random.randint(0, 1000) for i in range(n)]

    time1 = time()
    timSort(arr)
    time2 = time()
    time_diff = time2 - time1

    k_size.append(n)
    time_list.append(time_diff)

    print("Test:", n)
    print("time: {}".format(time_diff / n))


plt.plot(k_size, time_list, label='Tim Sort')
plt.title("Tim Sort")
plt.xlabel("Size of partition size")
plt.ylabel("Time")
plt.legend()
plt.show()