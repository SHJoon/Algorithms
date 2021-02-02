#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'efficientJanitor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY weight as parameter.
#

def efficientJanitor(weight):
    # Write your code here
    weight.sort()
    count = 0
    
    light_idx = 0
    heavy_idx = len(weight) - 1
    
    while light_idx <= heavy_idx:
        if weight[light_idx] + weight[heavy_idx] <= 3:
            light_idx += 1
        heavy_idx -= 1
        count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    weight_count = int(input().strip())

    weight = []

    for _ in range(weight_count):
        weight_item = float(input().strip())
        weight.append(weight_item)

    result = efficientJanitor(weight)

    fptr.write(str(result) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'weightCapacity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY weights
#  2. INTEGER maxCapacity
#
from itertools import combinations

def weightCapacity(weights, maxCapacity):
    # Write your code here
    # Too inefficient to pass all tests
    possible_dict = {}
    
    for i in range(len(weights) + 1):
        for comb in list(combinations(weights, i)):
            possible_dict[sum(comb)] = comb
    
    possible_sums = [key for key in possible_dict.keys() if key <= maxCapacity]
    print(possible_sums)
    return max(possible_sums)

    # Also too inefficient
    current_weight = 0
    
    for i in range(len(weights) + 1):
        for comb in list(combinations(weights, i)):
            total_sum = sum(comb)
            if total_sum > current_weight and total_sum <= maxCapacity:
                current_weight = total_sum
    
    return current_weight
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    weights_count = int(input().strip())

    weights = []

    for _ in range(weights_count):
        weights_item = int(input().strip())
        weights.append(weights_item)

    maxCapacity = int(input().strip())

    result = weightCapacity(weights, maxCapacity)

    fptr.write(str(result) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'variantsCount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER s0
#  3. INTEGER k
#  4. INTEGER b
#  5. INTEGER m
#  6. LONG_INTEGER a
#


def variantsCount(n, s0, k, b, m, a):
    # Write your code here

    # # Too inefficient
    # s = [s0]
    # for i in range(1, n):
    #     s.append(((k * s[i-1] + b) % m) + 1 + s[i-1])
    
    # free_count = 0
    
    # for s1 in s:
    #     for s2 in s:
    #         if s1 * s2 <= a:
    #             free_count += 1
    #         else:
    #             break
    
    # return free_count


    # # Better than above, but still too inefficient
    s = [s0]
    for i in range(1, n):
        s.append(((k * s[i-1] + b) % m) + 1 + s[i-1])
    
    free_count = 0
    start_idx = 0
    end_idx = n-1
    
    while start_idx <= end_idx:
        if s[start_idx] * s[end_idx] <= a:
            free_count += 2 * (end_idx - start_idx) + 1
            start_idx += 1
        else:
            end_idx -= 1
    
    return free_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s0 = int(input().strip())

    k = int(input().strip())

    b = int(input().strip())

    m = int(input().strip())

    a = int(input().strip())

    result = variantsCount(n, s0, k, b, m, a)

    fptr.write(str(result) + '\n')

    fptr.close()
