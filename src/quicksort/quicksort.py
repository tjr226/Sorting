import random

def failed_quicksort(arr):
    if len(arr) <= 1:
        return arr

    # value at array position 0
    pivot_value = arr[0]

    smaller_array = []
    larger_array = []

    for i in arr[1:]:
        # test = range(1, len(arr))
        # print(test)
        if i <= pivot_value:
            smaller_array.append(i)
        else:
            # print("no larger?")
            larger_array.append(i)

    # print("smaller", smaller_array)
    # print("larger", larger_array)    

    sorted_smaller = quicksort(smaller_array)
    sorted_larger = quicksort(larger_array)

    # print(pivot_value)
    # print("sorted smaller", sorted_smaller)
    # print("sorted larger", sorted_larger)
    # sorted_smaller.append(pivot_value)

    return sorted_smaller + [pivot_value] + sorted_larger

def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right

def quicksort(data):
    if data == []:
        return data

    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)


test_arr = random.sample(range(30), 20)
print(test_arr)
print(quicksort(test_arr))
print(failed_quicksort(test_arr))