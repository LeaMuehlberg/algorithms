# wähle pivot. eine seite ist kleiner als pivot, eine größer als pivot

# rekursion: erstellt neue listen
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort([3, 23, 5, 19, 21, 7]))

# in place: arbeitet direkt in ursprünglicher liste
# gibt ungefähren trennindex zurück wo man die liste optimal teilen kann. und bringt elemente auf die richtige seite
def partition(arr, left, right):
    pivot = arr[left]
    i = left - 1
    j = right + 1
    while True:
        j -= 1
        while arr[j] > pivot: # j landet an elem was größer als pivot ist, von rechts aus
            j -= 1
        i += 1
        while arr[i] < pivot: # i landet an elem was kleiner als pivot ist, von links aus
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



###### ich check das nicht bro
# iterativ: rekursion wird ersetzt durch eigenen stack
def quick_sort_it(arr):
    left = 0
    right = len(arr) - 1
    stack = []
    while True:
        while left < right:
            mid = partition(arr, left, right)
            stack.append(mid + 1) # rechte hälfte wird sortiert
            stack.append(right)
            right = mid # linke seite wird sortiert. linke ende war mid -> rechts
        if stack == []:
            break
        right = stack.pop()
        left = stack.pop()
    return arr
print(quick_sort_it([3, 23, 5, 19, 21, 7]))