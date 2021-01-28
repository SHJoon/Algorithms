# There is a new mobile game that starts with consecutively numbered clouds.
# Some of the clouds are thunderheads and others are cumulus. The player can jump on
# any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
# The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump
# from the starting postion to the last cloud. It is always possible to win the game.

# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

# Example

# c = [0,1,0,0,0,1,0]

# Index the array from 0...6. The number on each cloud is its index in the list so the player
# must avoid the clouds at indices 1 and 5. They could follow these two paths: 0->2->4->6 or 0->2->3->4->6.
# The first path takes 3 jumps while the second takes 4. Return 3.

# Function Description

# Complete the jumpingOnClouds function in the editor below.
# jumpingOnClouds has the following parameter(s):
# int c[n]: an array of binary integers

# Returns

# int: the minimum number of jumps required

# Input Format

# The first line contains an integer n, the total number of clouds.
# The second line contains n space-separated binary integers describing clouds c[i] where 0<=i<n.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    moves = 0
    pos = 0
    
    while pos < len(c):
        if pos + 2 == len(c) - 1 or pos + 1 == len(c) - 1:
            moves += 1
            break
        
        pos = pos + 1 if c[pos +2] == 1 else pos + 2
        moves += 1
    
    return moves
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
