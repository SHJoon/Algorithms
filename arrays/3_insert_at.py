# InsertAt
# Given an array, index, and additional value, insert
# the value into the array at the given index. Do this
# without using built-in array methods. You can
# think of PushFront(arr,val) as equivalent to
# InsertAt(arr,0,val).

def insert_at(lst, idx, val):
    lst.append(0)
    for i in reversed(range(idx, len(lst))):
        lst[i] = lst[i - 1]
    lst[idx] = val

my_lst = [0,1,3]
insert_at(my_lst, 2, 2)
print(my_lst)