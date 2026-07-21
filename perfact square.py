from math import sqrt

def isPerfectSquare(x):
    if x >= 0:
        sr = int(sqrt(x))
        return (sr * sr) == x
    return False

number=int(input("enter the number:"))

if isPerfectSquare(number):
    print("True")
else:
    print("False")
