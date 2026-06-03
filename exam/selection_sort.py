# nimm das kleinste/größte elem und schick es nach vorne
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selection_sort([3, 23, 5, 19, 21, 7]))

def sort(arr):
    for i in range(len(arr) - 1): # man braucht das letzte elem  nicht weil es schon sortiert ist
        min_index = i
        for j in range(i + 1, len(arr)): # restliche elemente durchgehen
            if arr[j] < arr[min_index]: # ein element ist kleiner als schon das behauptete kleinste
                min_index = j # neuer index
        arr[i], arr[min_index] = arr[min_index], arr[i] # vertauscht die elemente, bzw macht "garnichts" wenn kein kleineres element gefunden wird
    return arr
print(sort([3, 23, 5, 19, 21, 7]))