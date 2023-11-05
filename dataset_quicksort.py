import time
import sys
import random
from quicksort_module import quicksort

new_limit = 1000000  
sys.setrecursionlimit(new_limit)

def quicksort_analysis(size, variation):
    if variation == 'sorted':
        data = generate_sorted_dataset(size)
    elif variation == 'random':
       data = generate_random_dataset(size)
    elif variation == 'reversed':
       data =generate_reversed_dataset(size)

    memory_before = sys.getsizeof(data)  # in bytes
    start_time = time.time()

    quicksort(data, 0, len(data) - 1)

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    memory_after = sys.getsizeof(data) 

    return execution_time, memory_before, memory_after

def generate_sorted_dataset(length):
    return list(range(1, length + 1))
def generate_random_dataset(length):
    dataset = list(range(1, length + 1))
    random.shuffle(dataset)
    return dataset
def generate_reversed_dataset(length):
    return list(range(length, 0, -1))


variations = ["sorted", "random", "reversed"]
sizes = [2**9,2**13, 2**16]

print("------")
print("Two Pivot Block Quicksort Analysis:")
print("------")
for size in sizes:
    for variation in variations:
        execution_time, memory_before, memory_after = quicksort_analysis(size, variation)
        print(f"Size: {size}")
        print(f"Variations: {variation}")
        print(f"Execution Time: {execution_time:} ms")
        print(f"Memory Before Sorting: {memory_before} bytes")
        print(f"Memory After Sorting: {memory_after} bytes")
        print("-------------")
