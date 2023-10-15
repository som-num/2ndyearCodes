# Shell Sort Implementation in Python

def shellSort(arr):
    # Get the length of the input array
    n = len(arr)
    
    # Initialize the gap to half of the array size
    gap = n // 2

    # Start the shell sort algorithm
    while gap > 0:
        j = gap
        # Iterate over the array elements from the gap to the end
        while j < n:
            i = j - gap
            # Compare and swap elements with a gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    # Swap elements and print the array after the swap
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                    print(f"Swap {arr[i]}, {arr[i+gap]}:", arr)
                i = i - gap
            j += 1
        # Print the gap value used in this iteration
        print("Gap Calculation:", gap)
        
        # Reduce the gap size
        gap = gap // 2

def shellSortMain(arr):
    print("================== Shell Sort =================\n")
    print("Input array:", arr)

    # Call the shellSort function to sort the input array
    shellSort(arr)
    print("Sorted array:", arr)
    
    
# Driver code
if __name__=='__main__':
    input_str = input("Enter elements separated by space: ")
    arr = [int(x) for x in input_str.split()]
    print("Input array:", arr)

    # Call the shellSort function to sort the input array
    shellSort(arr)
    print("Sorted array:", arr)
