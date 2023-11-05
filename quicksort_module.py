import math

def block_size(n):
    b = 2**(10/26 * math.log2(n))
    return int(b)

def quicksort(arr,lo, hi):
    if lo >= hi:
        return
    if arr[lo] > arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    b = block_size(hi-lo+1)
    p, q = partition(arr,lo,hi,b)   
    quicksort(arr,lo,p-1)
    quicksort(arr, p, q-1)
    quicksort(arr, q+1,hi)


def partition(arr, lo, hi,b):
    p = arr[lo]
    q = arr[hi]
    block = [0] * b
    i, j, k = lo + 1, lo + 1, lo + 1
    num_p,num_q =  0, 0

    while k<hi:
        t = min(b, hi-k)
        for c in range(t):
            block[num_q] = c
            num_q = num_q + (q >= arr[k+c])
        for c in range(num_q):
            arr[j+c], arr[k+block[c]] = arr[k+block[c]],arr[j+c]
        k = k +t
        for c in range(num_q):
            block[num_p] = c
            num_p = num_p + (p>arr[j+c])
        for c in range(num_p):
            arr[i], arr[j+block[c]] = arr[j+block[c]], arr[i]
            i = i+1
        j = j + num_q
        num_p, num_q= 0 ,0
    arr[lo], arr[i-1] = arr[i-1], arr[lo]
    arr[j] , arr[hi] = arr[hi], arr[j]

    return i-1, j

arr_sorted = [1,2,3,4,5,6,7,8,9,10]
quicksort(arr_sorted, 0, len(arr_sorted)-1)
print(f"Sorting an sorted array:{arr_sorted}")
arr_random = [2,3,30,12,11,9,10,20,4]
quicksort(arr_random, 0, len(arr_random)-1)
print(f"Sorting an random array:{arr_random}")
arr_reversed = [10,9,8,7,6,5,4,3,2,1]
quicksort(arr_reversed, 0, len(arr_reversed)-1)
print(f"Sorting an reversed array:{arr_reversed}")

