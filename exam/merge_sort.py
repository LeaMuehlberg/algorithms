# alles halbieren und aufteilen. dann nach und nach zusammenfügen während man es sortiert
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0: # macht eine liste leer
        if a[0] <= b[0]: 
            result.append(a[0])
            a = a[1:] # das kleinere wird immer zum result "rausgenommen"
        else:
            result.append(b[0])
            b = b[1:]
    return result + a + b # zb [3, 5] + [7] + [], mit a = [3, 7] b =[5]
print(merge_sort([3, 23, 5, 19, 21, 7]))