import math

def jumpSearch(arr, x, n):
    step = int(math.sqrt(n))
    prev = 0

    print(f"Searching for {x} in the array:")

    while arr[min(step, n) - 1] < x:
        print("Array:", [f"[{elem}]" if i == prev else elem for i, elem in enumerate(arr)], "Jump: ",step)
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        print("Array:", [f"[{elem}]" if i == prev else elem for i, elem in enumerate(arr)],"Jump: ", step)  # Highlight the current element
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        print("Array:", [f"[{elem}]" if i == prev else elem for i, elem in enumerate(arr)],"Index: ", prev)  # Highlight the found element
        return prev

    return -1

def jumpSearchMain(arr, key):
    n = len(arr)

    # Find the index of 'x' using Jump Search
    index = jumpSearch(arr, key, n)

    # Display the process of comparing elements
    if index != -1:
        print(f"Number {key} is found at index {index}")
    else:
        print(f"Number {key} is not found in the array")

    # Display the array for reference
    print("Final Array:", arr)

if __name__ == "__main__":
    # Input from the user
    arr = [int(x) for x in input("Enter space-separated integers in the array: ").split()]
    x = int(input("Enter the element to search for: "))
    n = len(arr)

    # Find the index of 'x' using Jump Search
    jumpSearchMain(arr, x)
