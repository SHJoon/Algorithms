# Fibonacci
# Implement the Fibonacci function, a famous mathematical equation that
# generates a numerical sequence such that each number is the sum of the
# previous two. The Fibonacci numbers at index 0 and 1, coincidentally, have
# values of 0 and 1. Your function should accept an argument of which Fibonacci number.
# Examples: fibonacci(2) = 1, fibonacci(3) = 2, fibonacci(4) = 3, fibonacci(5) = 5, etc.

def fibonacci(num):
    if num in (0,1):
        return num
    
    first = 0
    second = 1
    count = 0

    while count < num:
        temp = second
        second = first + second
        first = temp
        count += 1
    
    return first

print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
