from .mergelib import merge_sorted

# Implement merge_sort
# merge_sorted is a helper function that merges 2
# already sorted lists in linear time and space
# with respect to the combined lengths of the lists.

def merge_sort(data):

    if len(data) <= 1:
        return list(data)

    mid = len(data) // 2
    left = data[0:mid]
    right = data[mid:]

    sorted_left = merge_sort(left)  
    sorted_right = merge_sort(right)  


    sorted_data = merge_sorted(sorted_left, sorted_right)

    return sorted_data