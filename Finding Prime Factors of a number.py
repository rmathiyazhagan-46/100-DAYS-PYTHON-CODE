num = int(input("Enter a Number: "))

print("Prime Factors are:")

i = 2

while i <= num:
    while num % i == 0:
        print(i)
        num = num // i
    i = i + 1
