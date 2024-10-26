import random
import time

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Create arrays
size = 1000
array1 = list(range(size))  # Best case (already sorted)
array2 = random.sample(range(size), size)  # Average case (random order)
array3 = list(range(size, 0, -1))  # Worst case (reverse sorted)

# Function to measure sorting time
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())  # Copy to avoid modifying the original array
    return time.time() - start_time

# Measure and print results
results = {}
algorithms = [bubble_sort, selection_sort, merge_sort, quick_sort]
arrays = [array1, array2, array3]
array_names = ['Best Case', 'Average Case', 'Worst Case']

for i, arr in enumerate(arrays):
    results[array_names[i]] = {}
    for sort_func in algorithms:
        time_taken = measure_time(sort_func, arr)
        results[array_names[i]][sort_func.__name__] = time_taken

# Display results
for case, times in results.items():
    print(f"\n{case} Performance:")
    for algo, time_taken in times.items():
        print(f"{algo}: {time_taken:.6f} seconds")
