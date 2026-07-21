number = int(input("fibonacci series:"))
a, b = 0, 1
print("Fibonacci Series:", a, b, end=" ")
for i in range(2, number):
    c = a + b
    a = b
    b = c
    print(c, end=" ")

print()
