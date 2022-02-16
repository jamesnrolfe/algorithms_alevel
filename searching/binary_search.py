# ========== BINARY SEARCH =========

# works by splitting the list in half and looking at the half that must have to have the target in it
# only works for ordered lists

# ========== ALGORITHM ==========

def binarySearch(array, target):
    # takes in array to be searched and the search target and returns the index of the target value if it exists
    # otherwise, it just returns None
    sta = 0
    end = len(array)
    while sta <= end:
        mid = (sta+end) // 2 # integer division such that we get an index value for halfway through the list
        if target > array[mid]:
            sta = mid + 1 # if our target is greater than the middle value, we want to only consider the half
            # of the list it could possibly be in, thus we look at the half greater than the middle
        elif target < array[mid]:
            end = mid - 1 # likewise as above, but just the opposite
        elif target == array[mid]:
            return mid
    return None # if we don't find a value, return None

# ========= TEST ============
 
x = [1,3,6,8,10,23,432,6546] # len = 8

# equal to mid value
print(binarySearch(x, 8))

# less than mid value
print(binarySearch(x, 3))

# greater than mid value
print(binarySearch(x, 6546))

# not in list
print(binarySearch(x, 423))

# passed all tests :)