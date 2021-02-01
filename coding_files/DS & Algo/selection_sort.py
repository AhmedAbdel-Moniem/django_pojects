def find_smallest(arr):
    smallest_element = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array


print(selection_sort(([6, 4, 3, 2, 7, 89, 6, 43, 23])))
