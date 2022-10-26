# HW4Q3
# Comparing Dictionary Structures

from numpy import random
from time import time
from matplotlib import pyplot as plt
from statistics import mean
import sortedcontainers
from sortedcontainers import SortedList

"""
https://www.geeksforgeeks.org/hash-map-in-python/
"""


class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_val(self, key, val):

        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

"""
https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/
"""

sorted_list = sortedcontainers.SortedList()


hashTime = []
sortedTime = []
inputs = []
# loop through array of size 150
for n in range(1, 10000, 10):
    hash_small = []
    sorted_small = []

    hash_table = HashTable(n)

    time_first_hash = time()  # starting time for hash
    hash_table.set_val(n, 'value')
    time_last_hash = time()  # ending time for hash
    htime_diff = time_last_hash - time_first_hash  # duration of hash

    time_first_sorted = time()  # starting time for sorted array
    sorted_list.add((n, 'value'))
    time_last_sorted = time()  # ending time for sorted array
    stime_diff = time_last_sorted - time_first_sorted  # duration of sorted array

    hash_small.append(htime_diff)
    sorted_small.append(stime_diff)

    inputs.append(n)
    hashTime.append(mean(hash_small))
    sortedTime.append(mean(sorted_small))
    print("Test:", n)
    fastest = "Hash Table" if (htime_diff / n) <= (stime_diff / n) else "Sorted Array"
    print("Sorted Array:{}, Hash Table:{}, {}  is faster ".format(stime_diff / n, htime_diff / n, fastest))

plt.plot(inputs, hashTime, label='Hash Table')
plt.plot(inputs, sortedTime, label='Sorted List')
plt.title("Hash Table vs Sorted List")
plt.xlabel("Size")
plt.ylabel("Time")
plt.legend()
plt.show()
