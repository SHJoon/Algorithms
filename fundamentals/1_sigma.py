# Sigma
# Implement a function sigma(num) that, given a
# number, returns the sum of all positive integers
# from 1 up to number (inclusive). Ex.: sigma(3)
# = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5)

def sigma(num):
    sum = 0
    for i in range(num + 1):
        sum += i

    return sum


print(sigma(3))
print(sigma(5))