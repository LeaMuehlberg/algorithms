array = [1, 4, 9, 7, 11, 5, 10, 6, 2]
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort(array))

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
print(quick_sort_ip(array, 0, 8))