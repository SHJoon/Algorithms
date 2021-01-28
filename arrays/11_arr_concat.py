# arrConcat
# Replicate JavaScript’s concat(). Create a
# standalone function that accepts two arrays.
# Return a new array containing the first array’s
# elements, followed by the second array’s
# elements. Do not alter the original arrays. Ex.:
# arrConcat( ['a','b'], [1,2] ) should
# return ['a','b',1,2].

def concat(arr1, arr2):
    new_arr = []
    for val in arr1:
        new_arr.append(val)
    for val in arr2:
        new_arr.append(val)
        
    return new_arr