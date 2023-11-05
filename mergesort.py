
#source: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1: 
        mid = len(arr)//2
        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)

        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
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
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
arr_sorted = [1,2,3,4,5,6,7,8,9,10]
mergeSort(arr_sorted)
print(f"Sorting an sorted array:{arr_sorted}")
arr_random = [2,3,30,12,11,9,10,20,4]
mergeSort(arr_random)
print(f"Sorting an random array:{arr_random}")
arr_reversed = [10,9,8,7,6,5,4,3,2,1]
mergeSort(arr_reversed)
print(f"Sorting an reversed array:{arr_reversed}")