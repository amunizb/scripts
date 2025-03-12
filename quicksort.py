import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

def quick_sort(array):
    if len(array) == 0:
        return []
    
    n = len(array)
    index = np.random.randint(n)
    smaller, larger = [], []
    for i in range(n):
        if i == index:
            continue
        
        if array[i] < array[index]:
            smaller.append(array[i])
        else:
            larger.append(array[i])
    
    sorted = quick_sort(smaller) + [array[index]] + quick_sort(larger)

    return sorted


def test(sorting_algorithm, n_tests=1000):
    for _ in range(n_tests):
        size = np.random.randint(50)
        array = np.random.randint(-100, 100, size=size)
        unsorted_array = array.copy()
        my_sort = quick_sort(array)
        array.sort()
        if not np.array_equal(my_sort, array):
            print(f'Test failed')
            print(f'Last input: {unsorted_array}')
            print(f'Your sort: {my_sort}')
            print(f'Correct sort: {array}')
            break
    print(f'All test passed')

def time_complexity(sorting_algorithm, n_range, n_tests):
    try:
        times = np.load('times.npy')
        print("Loaded times from 'times.npy'")
        return times
    except FileNotFoundError:
        print("File 'times.npy' not found. Calculating times...")
        times = []
        for n in tqdm(n_range):
            times_n = []
            for i in range(n_tests):
                array = np.random.randint(-100, 100, size=n)
                start_time = time.time()
                quick_sort(array)
                end_time = time.time()
                times_n.append(end_time - start_time)
            times.append(np.mean(times_n))
    return times
    
n_max = 10000
n_range = range(1, n_max, 50)

times = time_complexity(quick_sort, n_range, n_tests=20) 
np.save('times.npy', times)
print("Saved times to 'times.npy'")

plt.figure(figsize=(12,6))
scaled_times = np.array(times) * n_max * np.log(n_max) / times[-1]
plt.plot(n_range, scaled_times , linestyle='--', linewidth=2, marker='o', label='Experimental complexity')
x = np.linspace(1, n_max, 1000)
plt.plot(x, x * np.log(x), label='Theoretical complexity')
plt.xlabel('Input size')
plt.ylabel('Average time')
plt.legend()
plt.show()
