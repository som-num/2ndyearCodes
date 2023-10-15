# Function to find the partition position
def partition(array, low, high):
    # Choose the leftmost element as pivot
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        
        while i <= j and array[i] <= pivot: # Move the left pointer to the right
            i = i + 1
        
        while array[j] >= pivot and j >= i: # Move the right pointer to the left
            j = j - 1
        if j < i:
            break
        else:
            
            array[i], array[j] = array[j], array[i] # Swap array[i] and array[j]
            print("Swapped:",array[i]," and ",array[j], array)
    # Swap pivot with array[j]
    array[low], array[j] = array[j], array[low]
    print("Pivot ",pivot," :", array)
    return j

# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

def quickSortMain(arr):
    print("=============== Quick SOrt ==============\n")
    quicksort(arr, 0, len(arr) - 1)
    print('Sorted array:', arr)
    # for x in arr:
    #     print(x, end=" ")
# Driver code
if __name__ == '__main__':
    input_string = input("Enter the array elements separated by space: ")
    input_array = [int(x) for x in input_string.split()]

    # Function call
    quicksort(input_array, 0, len(input_array) - 1)
    print('Sorted array:')
    for x in input_array:
        print(x, end=" ")
