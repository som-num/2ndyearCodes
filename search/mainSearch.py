import linearSearch,jumpSearch,binarySearch,ternarySearch,interpolationSearch,exponentialSearch

searching_algorithms = {
    1: linearSearch.linearSearchMain,
    2: jumpSearch.jumpSearchMain,
    3: binarySearch.binarySearchMain,
    4: ternarySearch.ternarySearchMain,
    5: interpolationSearch.interpolationSearchMain,
    6: exponentialSearch.exponentialSearchMain,
}

def main():
    data = input("Enter number separated by space: ").split()
    data = [int(x) for x in data]
    ans ='y'
    while ans == 'y':
        key = int(input("Enter the number to find: "))

        print("Choose a searching algorithm")
        print("1. Linear Search")
        print("2. Jump Search")
        print("3. Binary Search")
        print("4. Ternary Search")
        print("5. Interpolation Search")
        print("6. Exponential Search")
        choice = int(input("Enter the number of the Searching Algorithm: "))
        data.sort()

        if choice in searching_algorithms:
            sorting_function = searching_algorithms[choice]
            sorting_function(data,key)
        print()
        ans = input("Do you want to try again? y/n ")
        


if __name__ == '__main__':
    main()