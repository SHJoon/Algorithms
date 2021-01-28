# There is a string, s, of lowercase English letters that is repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

# Example

# s='abcac'
# n=10

# The substring we consider is abcacabcac, the first 10 characters of the infinite string.
# There are 4 occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below.

# repeatedString has the following parameter(s):

# - s: a string to repeat
# - n: the number of characters to consider


# Returns

# int: the frequency of a in the substring


# Input Format

# The first line contains a single string, s.
# The second line contains an integer, n.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count = s.count('a')
    num_repeated = n // len(s)
    a_count *= num_repeated
    a_count += s[:n - (num_repeated * len(s))].count('a')
    
    return a_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
