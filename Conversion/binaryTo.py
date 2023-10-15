import tabulate

def binaryToDec(binary_str):
    binary_str = binary_str[::-1]
    decimal = 0
    exp = 1
    table_data = []

    headers = ["Binary Digit", "Decimal"]
    for i in binary_str:
        table_data.append([i, exp])
        if i == '1':
            decimal += exp
        exp *= 2
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(decimal)
    return decimal

def binaryToOctal(binary_str):
    # Pad the binary string to make its length a multiple of 3
    while len(binary_str) % 3 != 0:
        binary_str = '0' + binary_str

    octal = ""
    table_data = []

    headers = ["Binary Group", "Octal"]
    for i in range(0, len(binary_str), 3):
        binary_group = binary_str[i:i + 3]
        octal_digit = int(binary_group, 2)
        table_data.append([binary_group, octal_digit])
        octal += str(octal_digit)
    
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(octal)
    return octal

def binaryToHex(binary_str):
    # Pad the binary string to make its length a multiple of 4
    while len(binary_str) % 4 != 0:
        binary_str = '0' + binary_str

    hex_str = ""
    table_data = []

    headers = ["Binary Group", "Hexadecimal"]
    for i in range(0, len(binary_str), 4):
        binary_group = binary_str[i:i + 4]
        hex_digit = hex(int(binary_group, 2))[2:]
        table_data.append([binary_group, hex_digit])
        hex_str += hex_digit
    
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(hex_str)
    return hex_str

# Example usage:
if __name__ == "__main__":
    binary_str = "1101011010"
    print("Binary to Decimal:")
    decimal_result = binaryToDec(binary_str)
    print(f"Decimal Result: {decimal_result}")

    print("\nBinary to Octal:")
    octal_result = binaryToOctal(binary_str)
    print(f"Octal Result: {octal_result}")

    print("\nBinary to Hexadecimal:")
    hexadecimal_result = binaryToHex(binary_str)
    print(f"Hexadecimal Result: {hexadecimal_result}")
