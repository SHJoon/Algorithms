# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some.
# There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain 
# amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices
# and an amount to spend, determine the maximum number of gifts he can buy.

# Note Each toy can be purchased only once.

# Example


# The budget is  units of currency. He can buy items that cost  for , or  for  units. The maximum is  items.

# Function Description

# Complete the function maximumToys in the editor below.

# maximumToys has the following parameter(s):

# int prices[n]: the toy prices
# int k: Mark's budget
# Returns

# int: the maximum number of toys
# Input Format

# The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend.
# The next line contains  space-separated integers 

# Constraints




# A toy can't be bought multiple times.

# Sample Input

# 7 50
# 1 12 5 111 200 1000 10
# Sample Output

# 4
# Explanation

# He can buy only  toys at most. These toys have the following prices: .


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    count = 0
    prices.sort()
    
    for price in prices:
        if (price <= k):
            count += 1
            k -= price
        else:
            break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
