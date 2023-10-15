# Define a function to heapify a given array (used for building a min-heap)
import binarytree
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Find the largest element among the root and its left and right children
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        # Swap the root with the largest element
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Define a function for heap sort
def heapSort(arr):
    n = len(arr)

    # Build a max-heap (not a min-heap) from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(arr)

    # Extract elements one by one from the max-heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap
        
def minheapSortMain(arr):
    print("Input array:", arr)

    # Perform heap sort to sort the array
    heapSort(arr)

    print("Sorted array:", arr)
    print(binarytree.build(arr))

if __name__ == '__main__':
    # Input from the user
    input_string = input("Enter space-separated numbers: ")
    arr = list(map(int, input_string.split()))

    print("Input array:", arr)

    # Perform heap sort to sort the array
    heapSort(arr)

    print("Sorted array:", arr)
    print(binarytree.build(arr))
