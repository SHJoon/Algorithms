# You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without
# any duplicates. You are allowed to swap any two elements. You need to find the minimum number
# of swaps required to sort the array in ascending order.

# For example, given the array arr=[7,1,3,2,4,5,6] we perform the following steps:

# i   arr                     swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took 5 swaps to sort the array.


# Function Description

# Complete the function minimumSwaps in the editor below. It must return an integer representing
# the minimum number of swaps to sort the array.

# minimumSwaps has the following parameter(s):

# arr: an unordered array of integers


# Input Format

# The first line contains an integer, n, the size of arr.
# The second line contains n space-separated integers arr[i].


# Output Format

# Return the minimum number of swaps to sort the given array.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0
    
    for i,v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1
    # Fails certain test cases as the code is inefficient and time consuming
    # for i, num in enumerate(arr):
    #     if num - 1 != i:
    #         for idx, val in enumerate(arr):
    #             if val - 1 == i:
    #                 arr[i], arr[idx] = arr[idx], arr[i]
    #                 swaps += 1
    #                 break
            
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
