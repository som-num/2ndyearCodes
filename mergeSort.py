def mergeSort(array):
    if len(array) > 1:
        # Determine the midpoint to split the array
        mid = len(array) // 2

        # Split the array into two halves
        L = array[:mid]
        M = array[mid:]

        # Print the array before splitting
        print("Splitting:", array)

        # Recursively sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Merge the sorted halves back together
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # Handle remaining elements in L and M
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

        # Print the array after merging
        print("Merged array:", array)
        
def mergeSortMain(array):
    print("\n ==========Merge Sort=============")
    print("Initial array:")
    printList(array)

    mergeSort(array)

    print("\nSorted array is:")
    printList(array)

# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = input("Enter the array elements separated by spaces: ").split()
    array = [int(x) for x in array]

    print("Initial array:")
    printList(array)

    mergeSort(array)

    print("\nSorted array is:")
    printList(array)
