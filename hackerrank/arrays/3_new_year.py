# It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
# Each person wears a sticker indicating their initial position in the queue from 1 to n.
# Any person can bribe the person directly in front of them to swap positions, but they still
# wear their original sticker. One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order.
# Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.


# Example

# q = [1,2,3,5,4,6,7,8]
# If person 5 bribes person 4, the queue will look like this: 1,2,3,5,4,6,7,8. Only 1 bribe is required. Print 1.

# q = [4,1,2,3]
# Person 4 had to bribe 3 people to get to the current position. Print Too chaotic.


# Function Description

# Complete the function minimumBribes in the editor below.

# minimumBribes has the following parameter(s):

# int q[n]: the positions of the people after all bribes


# Returns

# No value is returned. Print the minimum number of bribes necessary or Too chaotic if
# someone has bribed more than 2 people.


# Input Format

# The first line contains an integer i, the number of test cases.

# Each of the next t pairs of lines are as follows:
# - The first line contains an integer t, the number of people in the queue
# - The second line has n space-separated integers describing the final state of the queue.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    
    for idx, num in enumerate(q):
        if num - idx - 1 > 2:
            print("Too chaotic")
            return
        
        for j in range(max(num-2, 0), idx):
            if q[j] > num:
                count += 1
    
    print(count)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
