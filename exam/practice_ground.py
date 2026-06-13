# array: [3, 23, 5, 19, 21, 7]

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        current_value, arr[j + 1] = arr[j + 1], current_value
    return arr
print(insertion_sort([3, 23, 5, 19, 21, 7]))

# selection sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  
    return arr
print(selection_sort([3, 23, 5, 19, 21, 7]))      

# bubble sort
def bubble_sort(arr):
    changed = True
    while changed:
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
    return arr
print(bubble_sort([3, 23, 5, 19, 21, 7]))

# quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort([3, 23, 5, 19, 21, 7]))

# quick sort in place
def partition(arr, left, right):
    pivot = arr[left]
    i = left - 1
    j = right + 1
    while True:
        j -= 1
        while arr[j] > pivot:
            j -= 1
        i += 1
        while arr[i] < pivot:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j
def quick_sort_ip(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quick_sort_ip(arr, left, mid)
        quick_sort_ip(arr, mid + 1, right)
    return arr
print(quick_sort_ip([3, 23, 5, 19, 21, 7], 0, 5))
 
#quick sort iterativ
def quick_sort_it(arr):
    stack = []
    left = 0
    right = len(arr) - 1
    while True:
        while left < right:
            mid = partition(arr, left, right)
            stack.append(mid + 1)
            stack.append(right)
            right = mid
        if stack == []:
            break
        right = stack.pop()
        left = stack.pop()
    return arr
print(quick_sort_it([3, 23, 5, 19, 21, 7]))
        

# merge sort
def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a[0])
            a = a[1:]
        else:
            result.append(b[0])
            b = b[1:]
    return result + a + b
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))
print(merge_sort([3, 23, 5, 19, 21, 7]))


# heap_sort
def heap_sort(arr):
    heap = MaxHeap.createHeap(arr)
    sorted_list = []
    while len(heap) > 0:
        biggest = heap.pop()
        sorted_list.append(biggest)
    return sorted_list