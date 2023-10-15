def interpolationSearch(arr, lo, hi, x):
    if lo <= hi and x >= arr[lo] and x <= arr[hi]:
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))

        # Print the array for reference
        print("Array:", arr)

        print(f"Searching for {x} in indices {lo} to {hi}...")

        # Condition of target found
        if arr[pos] == x:
            return pos

        # If x is larger, x is in the right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1, hi, x)

        # If x is smaller, x is in the left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x)
    return -1

def interpolationSearchMain(arr, key):
    n = len(arr)

    # Search for the element using interpolationSearch
    index = interpolationSearch(arr, 0, n - 1, key)

    # Print the result
    if index != -1:
        print(f"Element {key} found at index {index}")
    else:
        print(f"Element {key} not found in the array")




if __name__ == '__main__':
    # Input the array as space-separated numbers
    input_str = input("Enter space-separated integers in the sorted array: ")
    arr = [int(x) for x in input_str.split()]

    # Element to be searched
    x = int(input("Enter the element to search for: "))
    n = len(arr)

    # Search for the element using interpolationSearch
    index = interpolationSearch(arr, 0, n - 1, x)

    # Print the result
    if index != -1:
        print(f"Element {x} found at index {index}")
    else:
        print(f"Element {x} not found in the array")
