# Python3 code to linearly search x in arr[].
def search(arr, N, x):
    for i in range(0, N):
        print("Array:", arr[:i]+ [f'[{arr[i]}]']+ arr[i+1:N])        
        if arr[i] == x:
            return i
        print(f'Element {arr[i]} is not equal to {x}')
    return -1

def linearSearchMain(data,x):
	result = search(data, len(data), x)
	if(result == -1):
		print("Element is not present in array")
	else:
		print("Element is present at index", result,"\n")

    
    
# Driver Code
if __name__ == "__main__":
	data = input("Enter number separated by space: ").split()
	data = [int(x) for x in data]
	x = int(input("Enter the number you want to search: "))
	# Function call
	result = search(data, len(data), x)
	if(result == -1):
		print("Element is not present in array")
	else:
		print("Element is present at index", result,"\n")
