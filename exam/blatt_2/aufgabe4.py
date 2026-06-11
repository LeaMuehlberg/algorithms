array = [7, 38, 2, 6, 12, 4, 8, 11, 34]
def heap_sort(arr):
    heap = MaxHeap.createHeap(arr)
    sorted_list = []
    while len(heap) > 0:
        biggest = heap.pop()
        sorted_list.append(biggest)
    return sorted_list