# Function to calculate the next gap for Comb Sort
def getNextGap(gap):
    gap = (gap * 10) / 13  # Calculate the next gap using the Comb Sort formula
    if gap < 1:
        return 1  # Ensure that the minimum gap is 1
    return int(gap)  # Convert the gap to an integer and return it

# Function to sort an array using Comb Sort
def combSort(arr):
    n = len(arr)
    gap = n  # Initialize the initial gap to the length of the array
    swapped = True  # Initialize a flag to track whether any swaps were made

    while gap != 1 or swapped:
        gap = getNextGap(gap)  # Get the next gap for this iteration
        swapped = False  # Reset the swapped flag for this pass

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]  # Swap elements if they are in the wrong order
                swapped = True  # Set the swapped flag to True to indicate a swap
                print(f"Swapped: {arr[i]} and {arr[i+gap]}, Array = {arr}, Gap: {gap}")

# Function to execute Comb Sort and print the sorted array
def combSortMain(arr):
    print("===================== Comb Sort ===================\n")
    print("Initial array:")
    print(arr)

    combSort(arr)  # Call the combSort function to sort the array

    print("\nSorted array:")
    for i in range(len(arr)):
        print(arr[i], end=" ")

# Main program starts here.
if __name__ == '__main__':
    # Take user input for the array and convert it to a list of integers.
    arr = input("Enter the elements separated by spaces: ").split()
    arr = [int(x) for x in arr]

    print("Initial array:")
    print(arr)

    combSort(arr)  # Call the combSort function to sort the input array

    print("\nSorted array:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
