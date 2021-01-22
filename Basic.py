# Print 1-255
# Print all the integers from 1 to 255.
for num in range(1, 256):
    print(num)


# Print Sum 0-255
# Print integers from 0 to 255, and with each integer print the sum so far.
sum = 0
for num in range(256):
    print(num)
    sum += num
    print(sum)


# Find and Print Max
# Given an array, find and print its largest element.
my_list = [-3,5,0,12,35,6,12,-1]
max_num = my_list[0]

for num in my_list:
    if num > max_num:
        max_num = num

print(max_num)


# Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).
my_arr = []

# for num in range(1,256):
#     if num % 2 == 1:
#         my_arr.append(num)
# print(my_arr)

# Better since the program handles half the iterations
for num in range(1,256,2):
    my_arr.append(num)
print(my_arr)


# Greater Than Y
# Given an array and a value Y, count and print the number of array values greater than Y.
my_list = [-3,5,0,12,35,6,12,-1]
Y = 3
count = 0

for num in my_list:
    if num > Y:
        count += 1
        print(num)
print(count)

curr_iter = 0
while curr_iter < len(my_list):
    if my_list[curr_iter] > Y:
        print(my_list[curr_iter])
        count += 1
    curr_iter += 1

print(count)


# Max, Min, Average
# Given an array, print the max, min and average values for that array.
my_list = [-3,5,0,12,35,6,12,-1]
max_num = min_num = my_list[0]
sum = 0

for num in my_list:
    # Finds the max num
    if num > max_num:
        max_num = num

    # Finds the min num
    if num < min_num:
        min_num = num

    # For average later
    sum += num

print(max_num)
print(min_num)
print(sum / len(my_list))


# Swap String For Array Negative Values
# Replace any negative array values with 'Dojo'.
my_list = [-3,5,0,12,35,6,12,-1]
# for(int i = 0; i < 10; i++) {
#     my_list[i]
# }

# idx = 0
# for num in my_list:
#     if num < 0:
#         my_list[idx] = "Dojo"
#     idx += 1
# print(my_list)

for i,num in enumerate(my_list):
    if num < 0:
        my_list[i] = "Dojo"
print(my_list)


# Print Odds 1-255
# Print all odd integers from 1 to 255.

for num in range(1,256):
    if num % 2 == 1:
        print(num)

for num in range(1,256,2):
    print(num)


# Iterate and Print Array
# Iterate through a given array, printing each value.
my_list = [-3,5,0,12,35,6,12,-1]
my_str = ""
for num in my_list:
    my_str += str(num) + " "
print(my_str)

for num in my_list:
    print(num)


# Get and Print Average
# Analyze an array’s values and print the average.
my_list = [-3,5,0,12,35,6,12,-1]
sum = 0
idx = 0
while idx < len(my_list):
    sum += my_list[idx]
    idx += 1
print(sum / len(my_list))

# for num in my_list:
#     sum += num
# print(sum / len(my_list))


# Square the Values
# Square each value in a given array, returning that same array with changed values.
my_list = [-3,5,0,12,35,6,12,-1]
for idx,num in enumerate(my_list):
    my_list[idx] = my_list[idx] ** 2
print(my_list)


# Zero Out Negative Numbers
# Return the given array, after setting any negative values to zero.
my_list = [-3,5,0,12,35,6,12,-1]
for idx, num in enumerate(my_list):
    if num < 0:
        my_list[idx] = 0
print(my_list)


# Shift Array Values
# Given an array, move all values forward by one index,
# dropping the first and leaving a '0' value at the end.
my_list = [-3,5,0,12,35,6,12,-1]

for idx, num in enumerate(my_list):
    if idx < len(my_list) - 1:
        my_list[idx] = my_list[idx + 1]
    else:
        my_list[idx] = '0'
        asdkofjosidjdifoj
print(my_list)