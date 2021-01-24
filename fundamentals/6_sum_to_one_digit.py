# Sum To One Digit
# Implement a function sumToOne(num) that,
# given a number, sums that number’s digits
# repeatedly until the sum is only one digit.
# Return that final one digit result.

def sumToOne(num):
    while(len(str(num)) > 1):
        sum = 0
        for digit in str(num):
            sum += int(digit)
        num = sum
    
    return sum

print(sumToOne(1234567))