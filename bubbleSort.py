# Define a function to perform the Bubble Sort algorithm on an input array.
def bubbleSort(array):
    n = len(array)  # Get the length of the input array
    
    # Iterate through the array for each pass.
    for i in range(n):
        swapped = False  # Initialize a flag to track whether any swaps were made in this pass.
        print(f'Pass {i + 1}:')  # Print the current pass number.
        
        # Iterate through the unsorted part of the array.
        # In each iteration, compare adjacent elements and swap them if they are in the wrong order.
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # Swap the elements
                swapped = True  # Set the flag to True, indicating a swap was made.
            
            # Print the current state of the array after each comparison or swap.
            print(f" [{array[j]}] and [{array[j+1]}]: {array}")
        
        # If no two elements were swapped in the inner loop, the array is already sorted.
        if not swapped:
            print("No swap")
            break  # Exit the loop early because the array is already sorted.

# Define a function to execute the Bubble Sort algorithm and print the sorted array.
def bubbleSortMain(arr):
    print("================== Bubble Sort =================\n")
    bubbleSort(arr)  # Call the bubbleSort function to sort the array.

    print('Sorted Array in Ascending Order:')
    print(arr)  # Print the sorted array.

# Main program starts here.
if __name__ == '__main__':
    # Take user input for the array and convert it to a list of integers.
    data = list(map(int, input("Enter elements of the array separated by spaces: ").split()))

    bubbleSort(data)  # Call the bubbleSort function to sort the input array.

    print('Sorted Array in Ascending Order:')
    print(data)  # Print the sorted array.
