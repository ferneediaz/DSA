def sort_array(source_array):
    # Extract and sort the odd numbers
    odd_sorted = sorted([i for i in source_array if i % 2 != 0])
    
    # Replace the odd numbers in the original array with the sorted ones
    odd_index = 0
    result = []
    for i in source_array:
        if i % 2 != 0:
            result.append(odd_sorted[odd_index])
            odd_index += 1
        else:
            result.append(i)
    
    return result
