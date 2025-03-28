import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

test = [
        list(map(lambda _: random.randint(0, 10000), ([0] * 1_000))),
        list(map(lambda _: random.randint(0, 10000), ([0] * 10_000))),
        list(map(lambda _: random.randint(0, 10000), ([0] * 100_000))),
]

for arr in test:
    start = time.perf_counter()
    bubble_sort(arr)
    end = time.perf_counter()
    print(f"Bubble sort {len(arr)} timing: {end - start:.4f} seconds")
    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()
    print(f"Merge sort {len(arr)} timing: {end - start:.4f} seconds")
    


