# Remove Negatives
# Implement a function removeNegatives() that
# accepts an array and removes any values that
# are less than zero.
# Second-level challenge: don’t use nested loops.

def remove_negatives(lst):
    curr_idx = 0
    while curr_idx < len(lst):
        if lst[curr_idx] < 0:
            lst.pop(curr_idx)
        else:
            curr_idx += 1

my_lst = [-1,2,3,-5,-6,-7,2]
my_lst1 = [-1,2,3,-5,-6,-7,2,-6,-7,2]

remove_negatives(my_lst)
remove_negatives(my_lst1)
print(my_lst)
print(my_lst1)