# Define a binary search function to search for a target element (x) in a sorted array.
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r) // 2  # Calculate the middle index of the current subarray
        print("Array:", arr[:l] + [f'[{arr[mid]}]'] + arr[l + 1:r + 1])  # Highlight the middle index in the current subarray
        print(f"Searching for {x} in indices {l} to {r}...")

        if arr[mid] == x:
            return mid  # If the middle element is the target, return its index

        elif arr[mid] < x:
            l = mid + 1  # If the target is greater, narrow the search to the right half of the subarray

        else:
            r = mid - 1  # If the target is smaller, narrow the search to the left half of the subarray

    return -1  # If the target element is not found, return -1

# Define a function to perform binary search and print the result.
def binarySearchMain(arr, key):
    result = binarySearch(arr, 0, len(arr) - 1, key)  # Call binarySearch to search for the key in the array.
    if result != -1:
        print(f'Element {key} is present at index {result}')
    else:
        print(f'Element {key} is not present in the array')

if __name__ == '__main__':
    data = input("Enter Number separated by space: ").split()
    data = [int(x) for x in data]
    x = int(input("Enter the numbe to search: "))
    
    result = binarySearch(data, 0, len(data)-1, x)
    if result != -1:
        print(f'Element {x} is present at index {result}')
    else:
        print(f'Element {x} is not present in the array')
    