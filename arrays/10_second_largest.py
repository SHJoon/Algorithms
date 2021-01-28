# Second-Largest
# Return the second-largest element of an array.

def second_largest(arr):
    if len(arr) < 2:
        return
    
    if arr[0] > arr[1]:
        largest = arr[0]
        next_largest = arr[1]
    else:
        largest = arr[1]
        next_largest = arr[0]
    
    for i in range(2, len(arr)):
        if arr[i] > largest:
            next_largest = largest
            largest = arr[i]
        elif arr[i] > next_largest and not arr[i] == largest:
            next_largest = arr[i]
    
    return next_largest

print(second_largest([0, 1, 4, 3.14, 7]))
print(second_largest([1, 1, 4, 3.14, 7]))
print(second_largest([4, 1, 4, 3.14, 7]))
print(second_largest([8, 1, 4, -2, 7, 6, 9]))