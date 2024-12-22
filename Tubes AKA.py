import time
import random
import matplotlib.pyplot as plt

# Fungsi untuk pencarian linear
def linear_search_iteratif(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Fungsi untuk pencarian biner
def binary_search_iteratif(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Fungsi untuk mengukur waktu eksekusi
def measure_time(func, *args, iterations=10):
    start_time = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end_time = time.perf_counter()
    return (end_time - start_time) / iterations


# Main program
if __name__ == "__main__":
    # Ukuran data
    data_sizes = [123, 1234, 9999]  # Ubah ukuran sesuai kebutuhan
    iterations = 10
    linear_times_iteratif = []
    binary_times_iteratif = []

    for size in data_sizes:
        print(f"\nData size: {size}")
        
        # Data acak untuk linear search
        random_data = [random.randint(1, size) for _ in range(size)]
        target = random.choice(random_data)
        
        # Data terurut untuk binary search
        sorted_data = sorted(random_data)
        
        # --- Linear Search ---
        linear_iterative_time = measure_time(linear_search_iteratif, random_data, target, iterations=iterations)
        linear_times_iteratif.append(linear_iterative_time)
        print(f"Linear Search Iterative Time: {linear_iterative_time:.6f} seconds")
    
        
        # --- Binary Search ---
        binary_iterative_time = measure_time(binary_search_iteratif, sorted_data, target, iterations=iterations)
        binary_times_iteratif.append(binary_iterative_time)
        print(f"Binary Search Iterative Time: {binary_iterative_time:.6f} seconds")

    # Plot the results
    plt.plot(data_sizes, linear_times_iteratif, label='Linear Search Iteratif')
    plt.plot(data_sizes, binary_times_iteratif, label='Binary Search Iteratif')
    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.title('Search Time Comparison')
    plt.legend()
    plt.show()