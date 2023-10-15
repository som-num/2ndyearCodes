from tabulate import tabulate

# Structure for an item which stores weight and corresponding value of Item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Main greedy function to solve the problem
def fractionalKnapsack(W, arr):
    # Sorting Item on the basis of ratio
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    # Result (value in Knapsack)
    finalvalue = 0.0

    # Table headers
    table = [['Item', 'Profit', 'Weight']]

    # Looping through all Items
    for i, item in enumerate(arr, start=1):
        # If adding Item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
            table.append([i, item.profit, item.weight])

        # If we can't add the current Item, add the fractional part of it
        else:
            fraction = W / item.weight
            finalvalue += item.profit * fraction
            table.append([i, item.profit * fraction, W])
            break

    # Display the table using tabulate
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    # Returning final value
    return finalvalue

# Driver Code
if __name__ == "__main__":
    W = int(input("Enter the maximum weight (W): "))
    n = int(input("Enter the number of items: "))
    arr = []

    for i in range(n):
        profit = int(input(f"Enter the profit for item {i + 1}: "))
        weight = int(input(f"Enter the weight for item {i + 1}: "))
        arr.append(Item(profit, weight))

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(f"Maximum value in the knapsack: {max_val}")
