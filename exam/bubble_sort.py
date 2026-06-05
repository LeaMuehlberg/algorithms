# vergleiche das element mit dem danach. wenns kleiner ist -> vertauschen

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

def sort(arr):
    changed = True # damit es in die schleife geht
    while changed:
        changed = False # wenn es schon fertig sortiert ist -> abbrechen
        for i in range(len(arr) - 1): # -1 weil wir mit [i + 1] vergleichen
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] # vertauschen
                changed = True # nochmal ein durchgang nötig
    return arr
print(sort([3, 23, 5, 19, 21, 7]))