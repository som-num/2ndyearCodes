import insertionSort,mergeSort, quickSort, selectionSort, shellSort, bucketSort, bubbleSort, combSort, radixSort, maxheapSort, minheapSort, treeSort, tournamentSort
# import insertionSort,mergeSort
sorting_algoriithms = {
    1: insertionSort.insertionSortMain,
    2: mergeSort.mergeSortMain,
    3: quickSort.quickSortMain,
    4: selectionSort.selectionSortMain,
    5: shellSort.shellSortMain,
    6: bucketSort.bucketSortMain,
    7: bubbleSort.bubbleSortMain,
    8: combSort.combSortMain,
    9: radixSort.radixSortMain,
    10: maxheapSort.maxheapSortMain,
    11: minheapSort.minheapSortMain,
    12: treeSort.treeSortMain,
    13: tournamentSort.tournamentSortMain,
}
def main():
    data = input('Enter elements separated by spaces: ').split()
    data = [int(x) for x in data]
    ans = 'y'
    while ans == 'y':
        print("Choose a sorting algorithm")
        print("1. Insertion Sort")
        print("2. Merge Sort")
        print("3. Quick Sort")
        print("4. Selection Sort")
        print("5. Shell Sort")
        print("6. Bucket Sort")
        print("7. Bubble Sort")
        print("8. Comb Sort")
        print("9. Radix Sort")
        print("10. Maxheap Sort")
        print("11. Minheap Sort")
        print("12. Tree Sort")
        print("13. Tournament Sort")
        choice= int(input("Enter the number of the Sorting Algorithm: "))
        
        if choice in sorting_algoriithms:
            sorting_function = sorting_algoriithms[choice]
            sorting_function(data)
            # print(f"Sorted array using selected sorting algorithm: {sorted_arr}")
            ans = input("Do you want to select another? y/n ")
            print()

    
    
    
if __name__=="__main__":
    main()