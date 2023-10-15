def bucketSort(array):
    min_val = min(array)
    num_buckets = int((max(array) - min_val) / 10) + 1  # Calculate the number of buckets based on width

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Insert elements into their respective buckets
    for num in array:
        index_b = int((num - min_val) / 10)
        buckets[index_b].append(num)

    # Sort the elements of each bucket
    for i in range(num_buckets):
        buckets[i].sort()

    # Output the buckets along with their range
    for i in range(num_buckets):
        bucket_min = min_val + i * 10
        bucket_max = min_val + (i + 1) * 10
        print(f"Bucket {i + 1} (Range: {bucket_min}-{bucket_max - 1}): {buckets[i]}")

    # Concatenate the sorted elements from buckets
    k = 0
    for i in range(num_buckets):
        for num in buckets[i]:
            array[k] = num
            k += 1
    return array


def bucketSortMain(arr):
    print("=================== Bucket Sort ======================\n")
    print("\nOriginal Array:")
    print(arr)

    sorted_array = bucketSort(arr)

    print("\nSorted Array in ascending order:")
    print(sorted_array)
    
if __name__=='__main__':
    try:
        input_str = input("Enter elements separated by spaces: ")
        array = list(map(float, input_str.split()))

        print("\nOriginal Array:")
        print(array)

        sorted_array = bucketSort(array)

        print("\nSorted Array in ascending order:")
        print(sorted_array)

    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")
