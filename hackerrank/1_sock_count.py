# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# ar = [1,2,1,2,1,3,2]
# There is one pair of color 1 and one of color 2.
# There are three odd socks left, one of each color. The number of pairs is 2.

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs

# Input Format

# The first line contains an integer n, the number of socks represented in ar.
# The second line contains n space-separated integers, ar[i], the colors of the socks in the pile.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_dict = {sock:ar.count(sock) for sock in ar}
    
    count = 0
    for key in sock_dict:
        count += sock_dict[key] // 2
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

def blah(arr):
    freq_table = {}
    for num in arr:
        if num in freq_table:
            freq_table[num] += 1
        else:
            freq_table[num] = 1