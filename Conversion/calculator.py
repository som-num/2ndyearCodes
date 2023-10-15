import tabulate

def binaryToDec(binary_str):
    return int(binary_str, 2)

def octalToDec(octal_str):
    return int(octal_str, 8)

def hexToDec(hex_str):
    return int(hex_str, 16)

def decToBinary(decimal_num):
    return bin(decimal_num)[2:]

def decToOctal(decimal_num):
    return oct(decimal_num)[2:]

def decToHex(decimal_num):
    return hex(decimal_num)[2:]

def add_binary(a, b, base):
    dec_a = binaryToDec(a) if base == 2 else octalToDec(a) if base == 8 else hexToDec(a)
    dec_b = binaryToDec(b) if base == 2 else octalToDec(b) if base == 8 else hexToDec(b)
    result = dec_a + dec_b
    return decToBinary(result) if base == 2 else decToOctal(result) if base == 8 else decToHex(result)

def subtract_binary(a, b, base):
    dec_a = binaryToDec(a) if base == 2 else octalToDec(a) if base == 8 else hexToDec(a)
    dec_b = binaryToDec(b) if base == 2 else octalToDec(b) if base == 8 else hexToDec(b)
    result = dec_a - dec_b
    return decToBinary(result) if base == 2 else decToOctal(result) if base == 8 else decToHex(result)

def multiply_binary(a, b, base):
    dec_a = binaryToDec(a) if base == 2 else octalToDec(a) if base == 8 else hexToDec(a)
    dec_b = binaryToDec(b) if base == 2 else octalToDec(b) if base == 8 else hexToDec(b)
    result = dec_a * dec_b
    return decToBinary(result) if base == 2 else decToOctal(result) if base == 8 else decToHex(result)

def divide_binary(a, b, base):
    dec_a = binaryToDec(a) if base == 2 else octalToDec(a) if base == 8 else hexToDec(a)
    dec_b = binaryToDec(b) if base == 2 else octalToDec(b) if base == 8 else hexToDec(b)
    if dec_b == 0:
        return "Division by zero error"
    result = dec_a // dec_b
    return decToBinary(result) if base == 2 else decToOctal(result) if base == 8 else decToHex(result)

def binary_octal_hex_calculator():
    while True:
        print("Binary, Octal, Hexadecimal Calculator")
        print("1. Binary")
        print("2. Octal")
        print("3. Hexadecimal")
        print("0. Exit")
        
        choice = input("Select number base (1/2/3/0 to exit): ")
        
        if choice == '0':
            break
        elif choice not in ('1', '2', '3'):
            print("Invalid choice. Please select a valid option.")
            continue
        
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation")
            continue
        
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        
        base = 2 if choice == '1' else 8 if choice == '2' else 16
        
        result = ""
        if operation == '+':
            result = add_binary(num1, num2, base)
        elif operation == '-':
            result = subtract_binary(num1, num2, base)
        elif operation == '*':
            result = multiply_binary(num1, num2, base)
        elif operation == '/':
            result = divide_binary(num1, num2, base)
        
        print("Result:")
        print("Base:", base)
        if base == 2:
            print("Binary:", result)
        elif base == 8:
            print("Octal:", result)
        elif base == 16:
            print("Hexadecimal:", result)

# Example usage:
if __name__=='__main__':
    binary_octal_hex_calculator()
