# geht der reihe nach durch die liste. setzt das folgeelement an der richtigen stelle ein.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
    return arr
print(insertion_sort([3, 23, 5, 19, 21, 7]))

def sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i] # das jetzige elem
        j = i - 1 # das davorige elem
        # wenn das davorige elem größer ist als das jetzige
        while arr[j] > current_value and j >= 0:
            arr[j + 1] = arr[j] # das vorherige word beim jetzigen eingesetzt
            j -= 1 # index geht eins zurück fürs umtauschen
        arr[j + 1] = current_value # ansonsten bleibts gleich bzw es wird umgetauscht
    return arr
# arr[j + 1] = arr[i] aber nicht wirklich
print(sort([3, 23, 5, 19, 21, 7]))