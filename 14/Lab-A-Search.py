def lineal_search(array, target):
    for item in array:
        if item == target:
            return True
    return False

array = [3, 5, 6, 9, 11, 18, 20, 21, 24, 30]
target = 24
# print(lineal_search(array, target))

def binary_search(array, target):
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        middle = (left_index + right_index) // 2
        if target == array[middle]:
            return True
        if target > middle:
            left_index = middle + 1
        else:
            right_index = middle - 1
    return False

# print(binary_search(array, target))

def ternary_search(array, target):
    left_index = 0 
    right_index = len(array) - 1
    while left_index < right_index:
        partition_size = (right_index - left_index) // 3
    
        mid_1 = left_index + partition_size
        mid_2 = right_index - partition_size
        if target == array[mid_1]: return True
        if target == array[mid_2]: return True
        if target < array[mid_1]:
            right_index = mid_1
        if target > array[mid_1] and target < array[mid_2]:
            left_index = mid_1
            right_index = mid_2
        if target > array[mid_2]:
            left_index = mid_2 
    return False

print(ternary_search(array, target))

    