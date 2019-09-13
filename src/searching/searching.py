# STRETCH: implement Linear Search	
# 

test_arr = [2,4,6,8,10]

def linear_search(arr, target):
  if len(arr) == 0:
    return -1

  for i in range(len(arr)):
    if arr[i] == target:
      # print("i, target: ", i, target)
      return i
  # TO-DO: add missing code

  return -1   # not found

print(linear_search(test_arr, 4))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
