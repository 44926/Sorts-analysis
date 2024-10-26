import time
import matplotlib.pyplot as plt

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge Sort Implementation
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

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Measure time and display for each sort
def measure_time_and_display(sort_func, cases):
    times = {}
    for name, case in cases.items():
        start_time = time.time()
        if sort_func == quick_sort:
            _ = sort_func(case.copy())
        else:
            sort_func(case.copy())
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken for {name} using {sort_func.__name__}: {elapsed_time:.10f} seconds")
        times[name] = elapsed_time

    sorted_cases = sorted(times.items(), key=lambda x: x[1])
    return sorted_cases

# Main function to execute sorting algorithms
def main():
    cases = {
        "Best Case": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],          # Already sorted
        "Average Case": [3, 5, 1, 4, 2, 6, 9, 8, 10, 7],     # Random order
        "Worst Case": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]        # Reverse sorted
    }

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    plt.figure(figsize=(10, 5))

    # Measure and plot for each sort
    for algo_name, algo_func in algorithms.items():
        print(f"\n{algo_name}:")
        sorted_cases = measure_time_and_display(algo_func, cases)
        cases_labels = [case[0] for case in sorted_cases]
        times_values = [case[1] for case in sorted_cases]

        plt.plot(cases_labels, times_values, marker='o', label=algo_name)

    plt.title('Sorting Algorithms Time Complexity')
    plt.xlabel('Cases (Best, Average, Worst based on time)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
