# Rotate Array
# Implement rotateArr(arr, shiftBy) that
# accepts array and offset. Shift arr’s values to the
# right by that amount. ‘Wrap-around’ any values
# that shift off array’s end to the other side, so that
# no data is lost. Operate in-place: given
# ([1,2,3],1), change the array to [3,1,2].

def rotate_arr(arr, shift_by):
    while shift_by > len(arr):
        shift_by -= len(arr)
    left_arr = arr[0:shift_by]
    right_arr = arr[len(arr) - shift_by - 1: len(arr)]
    
    for idx, num in enumerate(right_arr):
        arr[idx] = num
    for idx, num in enumerate(left_arr):
        arr[idx + len(right_arr)] = num

my_list = [1,2,3,4,5,6,7]

rotate_arr(my_list, 3)

print(my_list)