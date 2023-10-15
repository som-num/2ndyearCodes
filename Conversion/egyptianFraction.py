import math
from tabulate import tabulate

def egyptianFraction(nr, dr):
    print("Finding the Egyptian Fraction Representation of {0}/{1}".format(nr, dr))
    mainnr = nr
    maindr = dr
    ef = []
    while nr != 0:
        x = math.ceil(dr / nr)
        ef.append(x)
        nr = x * nr - dr
        dr = dr * x

        # Create a table to show the process
        data = []
        for i in range(len(ef)):
            data.append([i + 1, ef[i]])

        table = tabulate(data, headers=["Step", "Current Term (1/x)"], tablefmt="fancy_grid")
        print(table)

    print("\nEgyptian Fraction Representation:")
    print(f"{mainnr}/{maindr} = ")
    for i in range(len(ef)):
        if i != len(ef) - 1:
            print("1/{0} +".format(ef[i]), end=" ")
        else:
            print("1/{0}".format(ef[i]), end=" ")


def egyptMain ():
    nr = int(input("Enter the numerator: "))
    dr = int(input("Enter the denominator: "))

    egyptianFraction(nr, dr)
    
if __name__ == '__main__':
    nr = int(input("Enter the numerator: "))
    dr = int(input("Enter the denominator: "))

    egyptianFraction(nr, dr)
