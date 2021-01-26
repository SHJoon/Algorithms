# Binary Search
# Given a sorted array and a value, return whether
# that value is present in the array. Do not
# sequentially iterate the entire array. Instead,
# ‘divide and conquer’, taking advantage of the fact
# that the array is sorted.

def binary_search(sorted_list, num):
    start = 0
    end = len(sorted_list) - 1
    while start < end:
        mid = (start + end) // 2
        if num > sorted_list[mid]:
            start = mid + 1
        elif num < sorted_list[mid]:
            end = mid - 1
        else:
            return True
    return False

my_list = [0,1,5,7,10,15,50,62,98]
print(binary_search(my_list, 4))
print(binary_search(my_list, 10))
print(binary_search(my_list, 62))
print(binary_search(my_list, 90))