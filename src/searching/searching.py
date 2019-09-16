# STRETCH: implement Linear Search	
# 
import random

# test_arr = random.randrange(0, 20)
# test_arr = random.sample(range(50), 20)

def linear_search(arr, target):
  if len(arr) == 0:
    return -1

  for i in range(len(arr)):
    if arr[i] == target:
      # print("i, target: ", i, target)
      return i
  # TO-DO: add missing code

  return -1   # not found

# print(test_arr)
# print(linear_search(test_arr, 4))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  search_index = (len(arr)-1)//2

  if arr[search_index] == target:
    return search_index

  while search_index != high and search_index != low:
    if arr[search_index] == target:
      return search_index
    elif arr[search_index] < target:
      low = search_index
      search_index = (search_index + high) // 2
    elif arr[search_index] > target:
      high = search_index
      search_index = search_index // 2
  return -1 # not found


# test_arr = random.sample(range(50), 3)
# test_arr = []
# print(test_arr)
# test_arr.sort()
# print(test_arr)
# print(binary_search(test_arr, 10))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  # middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty

  if len(arr) == 1:
    if arr[0] == target:
      # if len(arr) == 1, low and high should be the same
      return low
    else:
      return -1 # array does not have target

  # this is the middle index for the temp array
  temp_middle_index = len(arr) // 2

  if len(arr) > 1:
    left_arr = arr[:temp_middle_index]
    right_arr = arr[temp_middle_index:]

    left_arr_result = binary_search_recursive(left_arr, target, low, high - len(right_arr))
    right_arr_result = binary_search_recursive(right_arr, target, low + len(left_arr), high)

    return max(left_arr_result, right_arr_result)

test_arr = random.sample(range(30), 20)

print(test_arr)
test_arr.sort()
print(test_arr)
print(binary_search_recursive(test_arr, 10, 0, len(test_arr)))
