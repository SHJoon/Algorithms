# A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
# For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].
# Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

# Given an array a of n integers and a number, d, perform d left rotations on the array.
# Return the updated array to be printed as a single line of space-separated integers.


# Function Description

# Complete the function rotLeft in the editor below.

# rotLeft has the following parameter(s):

# int a[n]: the array to rotate
# int d: the number of rotations


# Returns

# int a'[n]: the rotated array


# Input Format

# The first line contains two space-separated integers n and d, the size of a and the number of left rotations.
# The second line contains n space-separated integers, each an a[i].

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
