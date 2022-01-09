number = int(input("Please enter a number:\t"))

num_check = number%2

if(num_check == 0):
    print(number," is an even number")
else:
    print(number," is an odd number")

input("Press Enter to exit")