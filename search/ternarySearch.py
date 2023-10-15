import math as mt

# Function to perform Ternary Search
def ternarySearch(l, r, key, ar):

    while r >= l:
        # Find the mid1 and mid2
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        # Print the array for reference
        print("Array:", ar)
        print(f'mid1 is {mid1} and mid2 is {mid2}')
        print(f"Searching for {key} in indices {l} to {r}... \n")

        # Check if key is present at any mid
        if ar[mid1] == key:
            return mid1
        if ar[mid2] == key:
            return mid2

        # Since key is not present at mid,
        # check in which region it is present
        # then repeat the Search operation
        # in that region
        if key < ar[mid1]:
            print(f"{key} is in the left third.")
            r = mid1 - 1
        elif key > ar[mid2]:
            print(f"{key} is in the right third.")
            l = mid2 + 1
        else:
            print(f"{key} is in the middle third.")
            l = mid1 + 1
            r = mid2 - 1

    # Key not found
    return -1

def ternarySearchMain(ar,key):
        # Starting index
    l = 0

    # end element index
    r = len(ar) - 1

    # Search the key using ternarySearch
    p = ternarySearch(l, r, key, ar)

    # Print the result
    if p != -1:
        print(f"Element {key} is found at index {p}")
    else:
        print(f'Element {key} is not found in the array')

if __name__== '__main__':
    # Input the array as space-separated numbers
    input_str = input("Enter space-separated integers in the array: ")
    ar = [int(x) for x in input_str.split()]

    # Sort the array if not sorted
    ar.sort()

    # Key to be searched in the array
    key = int(input("Enter the element to search for: "))

    # Starting index
    l = 0

    # end element index
    r = len(ar) - 1

    # Search the key using ternarySearch
    p = ternarySearch(l, r, key, ar)

    # Print the result
    if p != -1:
        print(f"Element {key} is found at index {p}")
    else:
        print(f"Element {key} is not found in the array")
