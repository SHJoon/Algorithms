# PushFront
# Given an array and an additional value, insert this
# value at the beginning of the array. Do this
# without using any built-in array methods.

def pushFront(lst, val):
    lst.append(lst[len(lst) - 1])
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = val

my_list = [0,1,2]
pushFront(my_list, 0)
print(my_list)