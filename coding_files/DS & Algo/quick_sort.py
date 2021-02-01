# Quick sort, recursively.
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less    = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


array = [6,4,54,6,7,33,7,99]
print(quick_sort(array))