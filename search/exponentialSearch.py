# A recursive binary search function returns
# location of x in the given array arr[l..r] if
# present, otherwise -1
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        
        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid
        
        # If the element is smaller than mid,
        # then it can only be present in the left subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        
        # Else, the element can only be present in the right subarray
        return binarySearch(arr, mid + 1, r, x)
    
    # We reach here if the element is not present
    return -1

# Returns the position of the first
# occurrence of x in the array
def exponentialSearch(arr, n, x):
    # If x is present at the first location itself
    if arr[0] == x:
        return 0
    
    # Find the range for binary search (j) by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    
    # Call binary search for the found range
    return binarySearch(arr, i // 2, min(i, n - 1), x)


def exponentialSearchMain(arr,key):
    n = len(arr)

    # Iterate through the exponential search and display the array
    i = 1
    while i < n and arr[i] <= key:
        print("Array:", arr[:i])
        print(f"Searching for {key} in indices 0 to {i - 1}...")
        i = i * 2

    # Search for the element using exponentialSearch
    result = exponentialSearch(arr, n, key)

    # Print the result
    if result == -1:
        print("Element not found in the array")
    else:
        print(f"Element is present at index {result}")
        print("Array:", arr[:i])

if __name__=='__main__':
    # Input the array as space-separated numbers
    input_str = input("Enter space-separated integers in the sorted array: ")
    arr = [int(x) for x in input_str.split()]

    # Element to be searched
    x = int(input("Enter the element to search for: "))
    n = len(arr)

    # Iterate through the exponential search and display the array
    i = 1
    while i < n and arr[i] <= x:
        print("Array:", arr[:i])
        print(f"Searching for {x} in indices 0 to {i - 1}...")
        i = i * 2

    # Search for the element using exponentialSearch
    result = exponentialSearch(arr, n, x)

    # Print the result
    if result == -1:
        print("Element not found in the array")
    else:
        print(f"Element is present at index {result}")
        print("Array:", arr[:i])
