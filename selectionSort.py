# Function to take user input and convert it into a list of integers
def input_array():
    user_input = input("Enter numbers separated by space: ")
    input_list = list(map(int, user_input.split()))
    return input_list

# Function to perform selection sort and display the array after every swap
def selection_sort(A):
    n = len(A)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if A[min_idx] > A[j]:
                min_idx = j
        # Display the array after each swap
        print(f"After swap {i + 1}: {A}")
        
        # Swap the found minimum element with the first element
        A[i], A[min_idx] = A[min_idx], A[i]
        
        

def selectionSortMain(arr):
    print("============== Selection Sort================\n")
    print("Original array:", arr)
    
    selection_sort(arr)
    
    print("Sorted array:", arr)
    
# Main function
if __name__ == "__main__":
    A = input_array()
    
    print("Original array:", A)
    
    selection_sort(A)
    
    print("Sorted array:", A)
