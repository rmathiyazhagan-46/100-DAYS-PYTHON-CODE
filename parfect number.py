number = int(input("enter the number:"))
sum = 0

for i in range(1, number):
    if number % i == 0:
        sum = sum + i

if sum == number:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")
