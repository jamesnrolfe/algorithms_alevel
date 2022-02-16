# ========== MERGE SORT ==========

# merge sort works by recursively splitting the array into smaller sub arrays until 
# the sub arrays are of length 1
# it then recombines the sub arrays such that they are ordered

# ========= ALGORITHM ==========

def mergeSort(array):
    # we first need to split two lists down the middle and so on
    if len(array) > 1: # we cant split a list of size 1
        mid = len(array) // 2 # find the index to split the lists at
        left = array[:mid] # python shorthand for splitting lists from a certain index - you can use this in an exam
        right = array[mid:]
        mergeSort(left) # do the same for all the lists of len>1 on the left...
        mergeSort(right) #...and the right

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            # until we run out of items in either list
            if left[i] < right[j]: # if the left one is smaller than the right
                array[k] = left[i] # add that to the sorted array
                i += 1
            else: # otherwise j is smaller or equal
                array[k] = right[j] # so add right one to sorted list
                j += 1
            k += 1 # and incremement k so we don't override

        while i < len(left):
            # so if some items still remain in the left half
            array[k] = left[i] # we need to add them to the list
            i += 1
            k += 1

        while j < len(right):
            # likewise with the other half
            array[k] = right[j]
            j += 1
            k += 1

    return array #should now be sorted

# ========== TEST ============

numbers = [3,1,62,4,3,2,6,4,1,0]
sortedNumbers = mergeSort(numbers)
print(numbers) # works :)
