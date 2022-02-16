# =========== QUICK SORT ============

# below are the steps for the partition function, which is where the actual sorting takes place

# first, we take a pivot value, which is usually the first item in the list
# then, we set a left pointer. This is the second index of the list
# then, we set a right pointer. This is the last index of the list
# now, we move the left pointer right until we find a value greater than the pivot
# OR if it passes the right pointer
# now we move the right pointer left until we find a value smaller than the pivot
# OR if it passes the left pointer 
# ...if the left pointer is still less than the right pointer, then swap the values at the 
# left and right pointers
# now repeat from line 6
# ...otherwise, swap the pivot value with the value at the right pointer
# this list is now partitioned, which means that the middle value is in the correct spot.
# that is: every item before it is smaller and every item after it is bigger

# ========== EXAMPLE ===========

# take the list B A G F A C E
# we first set up the pointers. pivot is B, leftPointer is A and rightPointer is E
# now we move the leftPointer right, leftPointer -> G, which is > B, so we stop
# now we move the rightPointer left, rightPointer -> C > B
# rightPointer -> A < B, so we swap the leftPointer and rightPointer
# our list becomes B A A F G C E 
# now move the leftPointer right, leftPointer -> F > B
# now move the rightPointer left, rightPointer -> F > B 
# rightPointer -> A < B AND we've crossed the leftPointer
# so now we swap the rightPointer and pivot
# so our list becomes A A B F G C E 
# this list is now partitioned. This means that the PIVOT VALUE IS IN THE CORRECT POSITION
# ALL THE VALUES TO THE RIGHT ARE NOT SMALLER THAN THE PIVOT VALUE
# that means we can recurisvely call the partition function on the left and right sides 
# of the pivot value, and sort those to get a full list

# ========== ALGORITHM ==========

def quickSort(array, start, end):
    if start < end: # terminating case, if start is equal or less than end,
        # we have an array of length 0 or 1
        split = partition(array, start, end) # find the pivot split 
        quickSort(array, start, split-1) # recursively call the function with either half
        quickSort(array, split+1, end)
    return array

def partition(array, start, end):
    pivotValue = array[start]
    leftPointer = start + 1
    rightPointer = end
    while leftPointer <= rightPointer:
        # whilst we haven't crossed pointers
        while array[leftPointer] <= pivotValue and leftPointer <= rightPointer:
            # if the value of the left pointer is less than the pivot value
            leftPointer += 1 # move on to the next value
        while array[rightPointer] >= pivotValue and leftPointer <= rightPointer: # likewise with right pointer
            rightPointer -= 1
        
        if leftPointer <= rightPointer:
            # if we HAVE NOT crossed pointers, swap the values at left and right
            tmp = array[leftPointer]
            array[leftPointer] = array[rightPointer]
            array[rightPointer] = tmp
    # after they do cross, i.e. this while loop is broken, we need to swap the rightPointer 
    # with the pivot value
    array[start] = array[rightPointer]
    array[rightPointer] = pivotValue
    return rightPointer # to be used to determine the split

# ========= TEST =========

x = [1, 123, 234, 12, 25, 6, 1]
quickSort(x, 0, len(x)-1)
print(x) # works :)