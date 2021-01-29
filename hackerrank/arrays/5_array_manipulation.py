# Starting with a 1-indexed array of zeros and a list of operations, for each
# operation add a value to each the array element between two given indices, inclusive.
# Once all operations have been performed, return the maximum value in the array.


# Example

# n = 10
# queries = [[1,5,3],[4,8,7],[6,9,1]]

# Queries are interpreted as follows:
#     a b k
#     1 5 3
#     4 8 7
#     6 9 1

# Add the values of k between the indices a and b inclusive:

# index->	 1 2 3  4  5 6 7 8 9 10
# 	    [0,0,0, 0, 0,0,0,0,0, 0]
# 	    [3,3,3, 3, 3,0,0,0,0, 0]
# 	    [3,3,3,10,10,7,7,7,0, 0]
# 	    [3,3,3,10,10,8,8,8,1, 0]
# The largest value is 10 after all operations are performed.


# Function Description

# Complete the function arrayManipulation in the editor below.

# arrayManipulation has the following parameters:

# - int n - the number of elements in the array
# - int queries[q][3] - a two dimensional array of queries where each queries[i] contains
# three integers, a, b, and k.


# Returns

# - int - the maximum value in the resultant array


# Input Format

# The first line contains two space-separated integers n and m, the size of the array
# and the number of operations. Each of the next m lines contains three space-separated
# integers a, b and k, the left index, right index and summand.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
        
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
            
    return max_value
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
