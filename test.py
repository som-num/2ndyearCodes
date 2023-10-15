from binarytree import build

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def tournamentIterative(arr):
    n = len(arr)

    # Pad the list to make its length a power of two
    while not is_power_of_two(n):
        arr.append('-inf')
        n = len(arr)

    stack = [list(arr)]  # Initialize the stack with the input array
    print(arr)

    while n > 1:
        unsortedArr = []

        for i in range(0, n, 2):
            if (i + 1) < n:
                if (isinstance(arr[i], str) and isinstance(arr[i + 1], int)):
                    largest = arr[i + 1]
                    unsortedArr.append(largest)
                    largest = '.inf'
                elif (isinstance(arr[i], int) and isinstance(arr[i + 1], str)):
                    largest = arr[i]
                    unsortedArr.append(largest)
                    largest = '.inf'
                elif isinstance(arr[i], int) and isinstance(arr[i + 1], int):
                    largest = max(arr[i], arr[i + 1])
                    unsortedArr.append(largest)
                    largest = '.inf'
            else:
                unsortedArr.append(arr[i])

        # Pad the unsortedArr to make its length a power of two
        while not is_power_of_two(len(unsortedArr)):
            unsortedArr.append('-inf')

        stack.append(unsortedArr)
        n = len(unsortedArr)
        arr = unsortedArr.copy()

    return stack if stack else arr[0]

def tournamentSort(arr):
    unSorted = []
  
    x = tournamentIterative(arr)
    print(x)
    x.reverse()
        
    for i in range(len(x)):
        for j in range(len(x[i])):
            unSorted.append(x[i][j])

    print(unSorted)
    tree = build(unSorted)
    print(tree)
    print(arr)

if __name__ == "__main__":
    arr = [55, 2, 4, 99, 25, 78, 3, 48, 8, 5, 100, 44, 6]

    print("Unsorted arr: ", arr)
    tournamentSort(arr)
