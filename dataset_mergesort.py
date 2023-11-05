import time
import sys
import random
from mergesort import mergeSort


def quicksort_analysis(size, variation):
    if variation == 'sorted':
        data = generate_sorted_dataset(size)
    elif variation == 'random':
       data = generate_random_dataset(size)
    elif variation == 'reversed':
       data =generate_reversed_dataset(size)

    memory_before = sys.getsizeof(data)  # in bytes
    start_time = time.time()

    mergeSort(data)

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    memory_after = sys.getsizeof(data) 

    return execution_time, memory_before, memory_after

def generate_sorted_dataset(length):
    return list(range(1, length + 1))
def generate_random_dataset(length):
   return random.sample(range(length), length)
def generate_reversed_dataset(length):
    return list(range(size, 0, -1))


variations = ["sorted", "random", "reversed"]
sizes = [2**9,2**13,2**16]

for size in sizes:
    for variation in variations:
        execution_time, memory_before, memory_after = quicksort_analysis(size, variation)
        print(f"Size: {size}")
        print(f"Variations: {variation}")
        print(f"Execution Time: {execution_time:} ms")
        print(f"Memory Before Sorting: {memory_before} bytes")
        print(f"Memory After Sorting: {memory_after} bytes")
        print("-------------")
