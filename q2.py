# BUBBLE SORT
# Complexity: O(N^2)

# Explanation:
# Bubble Sort is the simplest sorting algorithm that works by making multiple passes through a list. 
# It compares adjacent items and exchanges those that are out of order. 
# Each pass through the list places the next largest value in its proper place. 
# In essence, each item “bubbles” up to the location where it belongs.

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# QUICK SORT
# Complexity: O(NlogN)

# Explanation:
# QuickSort is a Divide and Conquer algorithm. 
# It picks an element as pivot and partitions the given array around the picked pivot

# Sort that pick pivot in different ways.
#     - Always pick first element as pivot.
#     - Always pick last element as pivot (implemented below)
#     - Pick a random element as pivot.
#     - Pick median as pivot.

# The key process in quickSort is partition(). 
# Target of partitions is, given an array and an element x of array as pivot, 
# put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, 
# and put all greater elements (greater than x) after x.

# Partition Function:
# We start from the leftmost element and keep track of index of smaller (or equal to) elements as i. 
# While traversing, if we find a smaller element, we swap current element with arr[i]. 
# Otherwise we ignore current element.

def partition(arr,low,high): 
    i = (low - 1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 

        if arr[j] <= pivot: 
            i = i+1 
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr, low, high) 

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


# MERGE SORT
# Complexity: O(NlogN)

# Explanation:
# Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, and 
# calls itself for the two halves and then merges the two sorted halves. 
# The next steps are used for merging two halves. 
# The merging process is the key process that assumes that arr[l..m] and arr[m+1..r] are sorted and 
# merges the two sorted sub-arrays into one

# STEPS:
# If r > l
#     1. Find the middle point to divide the array into two halves:  
#         middle m = (l+r)/2
#     2. Call mergeSort for first half:   
#         Call mergeSort(arr, l, m)
#     3. Call mergeSort for second half:
#         Call mergeSort(arr, m+1, r)
#     4. Merge the two halves sorted in step 2 & 3:
#         Merge arr[l..m] and arr[m+1..r], two sorted sub-arrays into one. Repeating this step untill all
#         the sorted sub-arrays are merged

def mergeSort(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2
        L = arr[:mid] # First half
        R = arr[mid:] # Second half

        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half
  
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

# SELECTION SORT
# Complexity: O(N^2)

# Explanation:
# The selection sort algorithm sorts an array by repeatedly finding the minimum element 
# (considering ascending order) from unsorted part and putting it at the beginning. 

# The algorithm maintains two subarrays in a given array.
#     1) The subarray which is already sorted.
#     2) Remaining subarray which is unsorted.

# In every iteration of selection sort, the minimum element (considering ascending order) 
# from the unsorted subarray is picked and moved to the sorted subarray

def selectionSort(arr):
    for i in range(len(arr)): 
          
        # Find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 


if __name__ == '__main__':
    arr1 = [10, 7, 8, 9, 1, 5]
    arr2 = [10, 7, 8, 9, 1, 5]
    arr3 = [10, 7, 8, 9, 1, 5]
    arr4 = [10, 7, 8, 9, 1, 5]
    n = len(arr1)

    print("Input:", arr1)

    bubbleSort(arr1)
    print("\nBUBBLE SORT") 
    print(arr1)

    quickSort(arr2, 0, n-1) 
    print("\nQUICK SORT") 
    print(arr2)

    mergeSort(arr3)
    print("\nMERGE SORT") 
    print(arr3)

    selectionSort(arr4)
    print("\nSELECTION SORT") 
    print(arr4)