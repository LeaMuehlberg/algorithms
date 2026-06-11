array = [8, 49, 12, 36, 88, 15, 6, 61]
# früherer abbruch möglich? nein weil unsortierter teil der liste trd durchlaufen werden muss
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selection_sort(array))

# früherer abbruch möglich? erkennung am ende wenn keine verschiebung stattfindet
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
    return arr
print(insertion_sort(array))