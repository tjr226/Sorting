# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j 
             
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        print(arr)
    return arr

# selection_sort([0, 3, 7, 1, 2, 8, 5, 4, 6, 9])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for j in range(len(arr) - 1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# print(bubble_sort([0, 3, 7, 1, 2, 8, 5, 4, 6, 9]))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr
        
    maximum = max(arr)
    temp_arr = [0]*(maximum + 1)
    # print(temp_arr)
    # print(len(temp_arr))
    for i in arr:
        temp_arr[i] += 1
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
    
    return_arr = []
    for i in range(len(temp_arr)):
        while temp_arr[i] > 0:
            return_arr.append(i)
            temp_arr[i] -= 1
    return return_arr

# print(count_sort([0, 3, 7, 1, 2, 8, 5, 4, 6, 9]))