import time
import matplotlib.pyplot as plt

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
        merge_sort(case.copy())
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken for {name}: {elapsed_time:.10f} seconds")
        times[name] = elapsed_time

    # Sort cases based on time taken
    sorted_cases = sorted(times.items(), key=lambda x: x[1])
    return [case[0] for case in sorted_cases], [case[1] for case in sorted_cases]

# Plotting the time complexity
def plot_merge_sort():
    cases, times = display_time_complexity()

    plt.figure(figsize=(8, 4))
    plt.plot(cases, times, marker='o', color='green', linestyle='-')
    plt.title('Merge Sort Time Complexity')
    plt.xlabel('Cases (Best, Average, Worst based on time)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()

plot_merge_sort()
