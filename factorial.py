""" Factorial using for loop"""
factorial = 1
number = int(input("Enter a number to find its factorial:\t"))

for i in range(1,(number + 1)):
    factorial = factorial * i
    i = i + 1

print(factorial,"is the factorial of ",number)

"""Factorial using while loop"""
factorial = 1
i = 1
while(i <= number):
# ^-> could have also written while(i < number + 1)
    factorial = factorial * i
    i = i + 1
print("The factorial of ",number,"is ",factorial)

input("Press ENTER to exit")