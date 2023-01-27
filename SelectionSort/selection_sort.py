def selection_sort(array):
    n = len(array)
    for i in range (n -1):
        minIndex = i
        for j in range (i+1 , n):
            if array[j] < array[minIndex]:
                minIndex = j
        if minIndex!=i:
            temp = array[i]
            array[i] = array[minIndex]
            array[minIndex] = temp
    return array

el = [21,6,9,33,3]
print(selection_sort(el))


# second implementation
def findSmallest(arr):
    smallest = arr[0] 
    smallest_index = 0 
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print(selectionSort([5, 3, 6, 2, 10]))