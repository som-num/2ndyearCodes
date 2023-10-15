def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = (array[i] // place) % 10  # Update this line to handle negative integers
        count[index] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = (array[i] // place) % 10  # Update this line to handle negative integers
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)
    min_element = min(array)

    if min_element < 0:
        max_element = max(max_element, abs(min_element))

    place = 1

    while max_element // place > 0:
        print("Sorting by", end=" ")
        if place == 1:
            print("ones:")
        elif place == 10:
            print("tenths:")
        elif place == 100:
            print("hundredths:")
        else:
            print("thousandths:")

        countingSort(array, place)
        place *= 10
        print(array)  # Print the array at each step


def radixSortMain(arr):
    print("================ Radix Sort================\n")
    radixSort(arr)
    print("Sorted Array:", arr)

if __name__=='__main__':

    # Get user input as space-separated integers
    input_str = input("Enter integers separated by spaces: ")
    data = list(map(int, input_str.split()))

    radixSort(data)
    print("Sorted Array:", data)
