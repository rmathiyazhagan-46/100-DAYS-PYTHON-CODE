n = int(input("Enter the value of N: "))
a = 0
b = 1

if n == 1:
    print("Nth Fibonacci Term =", a)

elif n == 2:
    print("Nth Fibonacci Term =", b)

else:
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    print("Nth Fibonacci Term =", b)
