# ========== INSERTION SORT ===========

# iterates from index 1 to index n (where list is length n)
# compares the current key to its predecessor
# if the predecessor is larger than the current key, compare it to the elements before
# move greater elements one position up to make space for the swapped element

# ========== EXAMPLE ==========

# take list 12, 11, 13, 5
# loop for i = 1 to i = 3 (last item)
# i = 1: as 11 < 12, move 12 and put 11 before it
# now we have 11, 12, 13, 5
# i = 2: 13 will remain here as everything before it is smaller than it
# note, by this point, 11, 12, 13 is all sorted
# i = 3: as 5 is smaller than 13, 12, 11, it will move to the start of the list
# now, we have reached i = 3 and we have our sorted list: 5, 11, 12, 13

# ========= ALGORTIHM ==========

def insertionSort(array):
    for i in range(1, len(array)): # loop from i = 1 to i = n (where n is length array)
        item = array[i] # set a temporary value with the initial one we are looking at
        # so we can change it back later
        while i > 0 and array[i-1] > item:
            # whilst we haven't gone off the end of the list
            # and the item predecessor is larger than the one we are looking at now
            array[i] = array[i-1] # swap the items, as the predecessor is larger
            i -= 1 # go back one and try the process again until we hit the end of the list
            # OR we find an item that is smaller than the one we are looking at
        array[i] = item # now insert the current item in the list

# =========== TEST ===========

x = [23, 43, 12, 1, 24, 26, 2, 24]
insertionSort(x)
print(x) # works :)