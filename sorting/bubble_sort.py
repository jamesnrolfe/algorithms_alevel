# ========== BUBBLE SORT ===========

# works by going through the list repeatedly and swapping adjecent items that are out of place
# only stops once no swaps are made 

# ========== ALGORITHM ===========

def bubbleSort(array):
    flag = True # we need some way to tell if we haven't made any swaps, i.e. 
    # the list is sorted, so we use a flag
    n = 0 # an optimisation, look below to see effect
    while flag == True: # whilst we do have swaps remaining 
        flag = False # assume no swaps
        for i in range(len(array)-1-n): # for all items. After the nth pass, every item n items from the right is
            # guaranteed to be sorted so we don't have to look through it
            if array[i] > array[i+1]: # if the item is bigger than the next one
                tmp = array[i] # swap them
                array[i] = array[i+1]
                array[i+1] = tmp
                flag = True # flag is true as we've made a swap
        n += 1 # increment n
    
# ========= TEST ==========

x = [5,1,4,8,2,6]
bubbleSort(x)
print(x) # passed :)