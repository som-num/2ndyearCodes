import tabulate

def octalToDec(octal_str):
    octal_str = octal_str[::-1]
    decimal = 0
    exp = 1
    table_data = []

    headers = ["Octal Digit", "Decimal"]
    for i in octal_str:
        table_data.append([i, exp])
        decimal += int(i) * exp
        exp *= 8
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(decimal)
    return decimal

def octalToBinary(octal_str):
    binary_str = ""
    table_data = []

    headers = ["Octal Group", "Binary"]
    for digit in octal_str:
        octal_digit = int(digit)
        binary_group = format(octal_digit, '03b')  # Convert each octal digit to 3-bit binary
        table_data.append([digit, binary_group])
        binary_str += binary_group

    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(binary_str)
    return binary_str


def octalToHex(octal_str):
    hex_str = ""
    table_data = []

    headers = ["Octal Group", "Hexadecimal"]
    for i in range(0, len(octal_str), 3):
        octal_group = octal_str[i:i + 3]
        hex_digit = hex(int(octal_group, 8))[2:]
        table_data.append([octal_group, hex_digit])
        hex_str += hex_digit

    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(hex_str)
    return hex_str

# Example usage:
if __name__ == '__main__':
    octal_str = "7532"
    print("Octal to Decimal:")
    decimal_result = octalToDec(octal_str)
    print(f"Decimal Result: {decimal_result}")

    print("\nOctal to Binary:")
    binary_result = octalToBinary(octal_str)
    print(f"Binary Result: {binary_result}")

    print("\nOctal to Hexadecimal:")
    hexadecimal_result = octalToHex(octal_str)
    print(f"Hexadecimal Result: {hexadecimal_result}")
