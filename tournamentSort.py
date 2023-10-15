from binarytree import build

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

def tournamentIterative(arr):
    n = len(arr)
    arrCopy = list(arr)
    stack = []
    
    while not(is_power_of_two(len(arrCopy))):
        arrCopy.append('-inf')

    stack.append(arrCopy)
    print(arrCopy)
    while n > 1:
        unsortedArr = []
        for i in range(0, n, 2):  # Adjusted the range to avoid IndexError
            if (i + 1) < n:  # Check if there's a pair to compare
                if (isinstance(arrCopy[i], str) and isinstance(arrCopy[i + 1], int)):
                    largest = arrCopy[i + 1]
                    unsortedArr.append(largest)
                elif (isinstance(arrCopy[i], int) and isinstance(arrCopy[i + 1], str)):
                    largest = arrCopy[i]
                    unsortedArr.append(largest)
                elif isinstance(arrCopy[i], int) and isinstance(arrCopy[i + 1], int):
                    largest = max(arrCopy[i], arrCopy[i + 1])
                    unsortedArr.append(largest)
            else:
                unsortedArr.append(arrCopy[i])  # Handle odd-length lists
        while not(is_power_of_two(len(unsortedArr))):
            unsortedArr.append('-1')

        stack.append(unsortedArr)
        n = len(unsortedArr)
        arrCopy = list(unsortedArr)

    return stack if stack else arr[0]

def tournamentSort(arr):
    arrCopy = []
    sorted = []
    
    for num in arr:
        arrCopy.append(num)
        
    for i in range(len(arrCopy)):
        unSorted=[]
        
        x = tournamentIterative(arrCopy)
        print(x)
        x.reverse()
        for j in range(len(x)):
            for k in range(len(x[j])):
                unSorted.append(x[j][k])
                
        largest = unSorted[0]
        print(largest)
        tree = build(unSorted)
        print(tree)
        sorted.append(largest)
        
        iter = 0 
        while arrCopy[iter] != largest:
          iter+=1
        else:
           arrCopy.remove(largest)
           arrCopy.append('-1')
           iter = 0

    print(sorted)


def tournamentSortMain(arr):
    # arr = [55,2,4,99,25,78,3,48,8,5,100,44,6]
    # arr = [55 ,2 ,4 ,99, 25]

    print("Unsorted arr: ", arr)
    tournamentSort(arr)
