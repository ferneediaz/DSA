def sort_array(source_array):

    oddSortedArray = sorted([x for x in source_array if x%2 != 0])
    n = 0
    
    for i, el in enumerate(source_array):
        
        if el%2 !=0:
            source_array[i] = oddSortedArray[n]
            n += 1
            
    return source_array
source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

