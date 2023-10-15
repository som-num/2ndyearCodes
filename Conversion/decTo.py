import tabulate

def decToBinary(n):
    binaryNum = [0]*n
    i = 0
    exp = 1
    table_data = []  # Create an empty list to store table data
    
    while (n > 0):
        binaryNum[i] = n % 2
        n = int(n / 2)
        i += 1
        
        # Append data to the table for this step
        table_data.append([exp, binaryNum[i - 1]])
        exp *= 2
    
    # Create a header for the table
    headers = ["Decimal", "Binary Digit"]
    
    # Print the table using tabulate
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    
    # Print the binary representation
    print("Binary Representation:", end=" ")
    for j in range(i - 1, -1, -1):
        print(binaryNum[j], end="")
    print()

def decToOctal(n):
    octal_str = oct(n)[2:]  # Convert decimal to octal and remove the '0o' prefix
    table_data = [[n, octal_str]]
    
    headers = ["Decimal", "Octal"]
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(octal_str)
    return octal_str

def decToHex(n):
    hex_str = hex(n)[2:]  # Convert decimal to hexadecimal and remove the '0x' prefix
    table_data = [[n, hex_str]]
    
    headers = ["Decimal", "Hexadecimal"]
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(hex_str)
    return hex_str

# Example usage:
if __name__ == "__main__":
    decimal_value = 128
    print("Decimal to Binary:")
    decToBinary(decimal_value)

    print("\nDecimal to Octal:")
    octal_result = decToOctal(decimal_value)
    print(f"Octal Result: {octal_result}")

    print("\nDecimal to Hexadecimal:")
    hexadecimal_result = decToHex(decimal_value)
    print(f"Hexadecimal Result: {hexadecimal_result}")
