print("Algorithms file loaded")

def quicksort(arr):
    if len(arr) <2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num +1] = arr[num + 1], arr[num]