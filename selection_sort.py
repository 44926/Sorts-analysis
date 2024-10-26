import time
import matplotlib.pyplot as plt

# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Time complexity display
def display_time_complexity():
    cases = {
        "Best Case": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],          # Already sorted
        "Average Case": [3, 5, 1, 4, 2, 6, 9, 8, 10, 7],     # Random order
        "Worst Case": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]        # Reverse sorted
    }

    times = {}

    # Measure the time for each case
    for name, case in cases.items():
        start_time = time.time()
        selection_sort(case.copy())
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken for {name}: {elapsed_time:.10f} seconds")
        times[name] = elapsed_time

    # Sort cases based on time taken
    sorted_cases = sorted(times.items(), key=lambda x: x[1])
    return [case[0] for case in sorted_cases], [case[1] for case in sorted_cases]

# Plotting the time complexity
def plot_selection_sort():
    cases, times = display_time_complexity()

    plt.figure(figsize=(8, 4))
    plt.plot(cases, times, marker='o', color='orange', linestyle='-')
    plt.title('Selection Sort Time Complexity')
    plt.xlabel('Cases (Best, Average, Worst based on time)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()

plot_selection_sort()
