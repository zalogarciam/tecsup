array = [3, 5, 6, 9, 11, 18, 20, 21, 24, 30, 31]
target = 20

# O(n)
def linear_search(target , array):
    for num in array:
        if num == target:
            return True
    return False

# print(linear_search(20, array))

def binary_search(array, target):
    right = len(array) - 1
    left = 0
    while right >= left:
        mid = (left + right) // 2
        if array[mid] == target: return True
        if target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

# print(binary_search(array, 6))
# print(binary_search(array, 0))

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

# print(ternary_search(array, 6))

import math
def jump_search(array, target):
    block_size = math.sqrt(len(array))
    start = 0
    next = int(block_size)

    while start < len(array) and array[next-1] < target:
        start = next
        next += int(block_size)
        if next >= len(array) : next = len(array)
    print(array[start:next])
    return linear_search(target, array[start:next])
        
# print(jump_search(array, 31))

def exponential_search(array, target):
    bound = 1
    while array[bound] < target and bound < len(array):
        bound = bound * 2
    left = (bound // 2) + 1
    right = min(len(array), bound + 1)
    return binary_search(array[left:right], target)

print(exponential_search(array, target))
