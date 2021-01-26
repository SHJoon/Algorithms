# Skyline Heights
# You are given an array with heights of consecutive buildings in the city.
# For example, [-1,7,3] would represent three buildings: first is actually
# below street level, second is seven stories high, and third is three stories
# high (but hidden behind the seven-story onbe). You are situated at street level.
# Return an array containing heights of the buildings you can see, in order.
# Given [1,-1,7,3] return [1,7].

def skyline_heights(lst):
    highest_floor = lst[0]
    visible = [highest_floor]
    
    for floor in lst:
        if floor > highest_floor:
            visible.append(floor)
            highest_floor = floor

    return visible

print(skyline_heights([1,-1,7,3]))
print(skyline_heights([1,5,7,-6]))
print(skyline_heights([-1,8,7,3]))