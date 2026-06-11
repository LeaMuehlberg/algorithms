def heap_sort(arr):
    heap = MaxHeap.createHeap(arr)
    sorted_list = []
    while len(heap) > 0:
        biggest = heap.pop()
        sorted_list.append(biggest)
    return sorted_list
print(heap_sort([3, 23, 5, 19, 21, 7]))    