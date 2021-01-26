# RemoveAt
# Given an array and an index into the array,
# remove and return the array value at that index.
# Do this without using any built-in array methods
# except pop(). Think of PopFront(arr) as
# equivalent to RemoveAt(arr,0).

def remove_at(lst, idx):
    for i in range(idx, len(lst) - 1):
        lst[i] = lst[i + 1]
    lst.pop()

my_lst = [0,1,2,3]

remove_at(my_lst, 2)
print(my_lst)