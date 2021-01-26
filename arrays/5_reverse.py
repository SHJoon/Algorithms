# Reverse Array
# Given a numerical array, reverse the order of the
# values. The reversed array should have the same
# length, with existing elements moved to other
# indices so that the order of elements is reversed.

def reverse_array(lst):
    for i in range(len(lst) // 2):
        temp = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = temp

my_lst = [0,1,2,3,4]
my_lst2 = [0,1,2,3,4,5]
reverse_array(my_lst)
reverse_array(my_lst2)
print(my_lst)
print(my_lst2)