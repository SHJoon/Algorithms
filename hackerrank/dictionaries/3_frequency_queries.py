# You are given q queries. Each query is of the form two integers described below:
# - 1 x: Insert x in your data structure.
# - 2 y: Delete one occurence of y from your data structure, if present.
# - 3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

# The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation,
# and queries[i][1] contains the data element. For example, you are given array
# queries=[(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)].

# The results of each operation are:

# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# Return an array with the output: [0,1].


# Function Description

# Complete the freqQuery function in the editor below. It must return an array of integers where each
# element is a 1 if there is at least one element value with the queried number of occurrences in the
# current array, or 0 if there is not.

# freqQuery has the following parameter(s):

# - queries: a 2-d array of integers


# Input Format

# The first line contains of an integer q, the number of queries.
# Each of the next q lines contains two integers denoting the 2-d array queries.


# Output Format

# Return an integer array consisting of all the outputs of queries of type 3.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.

# Failed one test case as inefficient code
# def freqQuery(queries):
#     data = {}
#     output = []
    
#     for query in queries:
#         if query[0] == 1:
#             if query[1] in data:
#                 data[query[1]] += 1
#             else:
#                 data[query[1]] = 1
#         elif query[0] == 2:
#             if query[1] in data:
#                 if data[query[1]] == 1:
#                     del data[query[1]]
#                 else:
#                     data[query[1]] -= 1
#         else:
#             if query[1] in data.values():
#                 output.append(1)
#             else:
#                 output.append(0)    
            
#     return output

from collections import Counter

def freqQuery(queries):
    freq = Counter()

    cnt = Counter()

    arr = []

    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1

        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1

        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)

    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
