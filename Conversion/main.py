import os
import binaryTo
import calculator
import hexTo
import decTo
import octalTo
import egyptianFraction
import knapsack

conversion = {
    1: binaryTo.binaryToDec,
    2: binaryTo.binaryToHex,
    3: binaryTo.binaryToOctal,
    4: hexTo.hexToBinary,
    5: hexTo.hexToDec,
    6: hexTo.hexToOctal,
    7: octalTo.octalToBinary,
    8: octalTo.octalToDec,
    9: octalTo.octalToHex,
    10: decTo.decToBinary,
    11: decTo.decToHex,
    12: decTo.decToOctal,
    13: calculator.binary_octal_hex_calculator,
    14: egyptianFraction.egyptMain,
    15: knapsack.knapMain,
}

def main():
    while True:
        print("Select an option:")
        print("1. Binary To Decimal")
        print("2. Binary To Hexadecimal")
        print("3. Binary To Octal")
        print("4. Hexadecimal To Binary")
        print("5. Hexadecimal To Decimal")
        print("6. Hexadecimal To Octal")
        print("7. Octal To Binary")
        print("8. Octal To Decimal")
        print("9. Octal To Hexadecimal")
        print("10. Decimal To Binary")
        print("11. Decimal To Hexadecimal")
        print("12. Decimal To Octal")
        print("13. Binary/Octal/Hex Calculator")
        print("14. Egyptian Fraction")
        print("15. Knapsack Problem")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            number =input("Enter number: ")
            conversion[choice](number)
        elif choice in conversion and choice in range(10,13,1):
            number = int(input("Enter number:"))
            conversion[choice](number)
        elif choice in conversion and choice > 12:
            conversion[choice]()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
