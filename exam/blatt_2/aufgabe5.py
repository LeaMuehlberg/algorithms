array = [6, 2, 3, 7, 1]
def bubble_sort(arr):
    changed = True
    while changed:
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
    return arr
print(bubble_sort(array))
# 6,2,3,7,1 -> 2,6,3,7,1 -> 2,3,6,7,1 -> 2,3,6,7,1 -> 2,3,6,1,7 -> while changed. .... 2,3,1,6,7 -> .... 2,1,3,6,7 -> .... 1,2,3,6,7