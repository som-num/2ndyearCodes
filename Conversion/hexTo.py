import tabulate

def hexToDec(hex_str):
    hex_str = hex_str[::-1]  # Reverse the hexadecimal string
    decimal = 0
    exp = 1
    count = 0
    table_data = []
    headers = ["Hexa Digit", "Decimal", "Decimal x 16^n"]

    for digit in hex_str:
        if '0' <= digit <= '9':
            decimal_digit = int(digit, 16)
        elif 'A' <= digit <= 'F':
            decimal_digit = ord(digit) - ord('A') + 10
        else:
            raise ValueError("Invalid hexadecimal input")

        decimal += decimal_digit * exp
        table_data.append([digit, decimal_digit, count])
        count += 1
        exp *= 16  # Hexadecimal is base-16

    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    return decimal

def hexToBinary(hex_str):
    binary_str = ""
    table_data = []
    headers = ["Hexadecimal Group", "Binary"]

    for digit in hex_str:
        if '0' <= digit <= '9':
            binary_group = format(int(digit, 16), '04b')  # Convert each hex digit to 4-bit binary
        elif 'A' <= digit <= 'F':
            binary_group = format(ord(digit) - ord('A') + 10, '04b')
        else:
            raise ValueError("Invalid hexadecimal input")

        table_data.append([digit, binary_group])
        binary_str += binary_group

    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(binary_str)
    return binary_str

def hexToOc1tal(hex_str):
    octal_str = ""
    table_data = []
    headers = ["Hexadecimal Group", "Octal"]

    for digit in hex_str:
        if '0' <= digit <= '9':
            octal_digit = format(int(digit, 16), '03o')  # Convert each hexadecimal digit to 3-digit octal
        elif 'A' <= digit <= 'F':
            octal_digit = format(ord(digit) - ord('A') + 10, '03o')
        else:
            raise ValueError("Invalid hexadecimal input")

        table_data.append([digit, octal_digit])
        octal_str += octal_digit

    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    print(octal_str)
    return octal_str
import tabulate

def hexToOctal(hex_str):
    decimal_value = int(hex_str, 16)
    octal_str = oct(decimal_value)[2:]  # Convert decimal to octal and remove the '0o' prefix
    table_data = [[hex_str, octal_str]]

    headers = ["Hexadecimal", "Octal"]
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    
    return octal_str





# Example usage:
if __name__ == "__main__":
    hex_str = "1A3B"
    print("Hexadecimal to Decimal:")
    decimal_result = hexToDec(hex_str)
    print(f"Decimal Result: {decimal_result}")

    print("\nHexadecimal to Binary:")
    binary_result = hexToBinary(hex_str)
    print(f"Binary Result: {binary_result}")

    print("\nHexadecimal to Octal:")
    octal_result = hexToOctal(hex_str)
    print(f"Octal Result: {octal_result}")
