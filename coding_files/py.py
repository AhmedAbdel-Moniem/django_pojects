def binary_search(array, target, low, high):
    while low <=high:
        mid = low + (high-low)//2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return -1


array = [1,2,3,4,5]
target = 8
result = binary_search(array, target, 0, len(array)-1)
if result != -1:
    print('found in index number :' + str(result))
else:
    print('wrong index')