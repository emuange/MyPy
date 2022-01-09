num1 = int(input("Enter the first number: \t"))
num2 = int(input("Enter the second number: \t"))
num3 = int(input("Enter the third number: \t"))

if((num1 > num2) & (num1 > num3)):
    print(num1,"is the largest number")
elif((num2 > num1) & (num2 > num3)):
    print(num2,"is the largest number")
else:
    print(num3,"is the largest number")
    