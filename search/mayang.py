import math
A=1
B=4
C=6
D=2
F=1

def getTotalGrades():
    return (A+B+C+D+F)

def getPercentage(num):
    return ((num/getTotalGrades())*100)

def getNumAsterisk(num):
    return (math.ceil(getPercentage(num)/2))
print(" "*4+"10"+" "*3+"20"+" "*3+"30"+" "*3+"40"+" "*3+"50"+" "*3+"60"+" "*3+"70"+" "*3+"80"+" "*3+"90"+" "*3+"100")
print(" "*4+"|"+" "*4+"|"+" "*4+"|"+" "*4+"|"+" "*4+"|"+" "*4+"|"+" "*4+"|"+" "*4+"|"+" "*4+"|"+" "*4+"|")
print("*"*50)
total = getTotalGrades()

print("TotalNumber of grades: ", total)
print(getNumAsterisk(A)*"*", "A")
print(getNumAsterisk(B)*"*","B")
print(getNumAsterisk(C)*"*", "C")
print(getNumAsterisk(D)*"*","D")
print(getNumAsterisk(F)*"*", "F")
