number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(number,"*",i,"=",number*i)

# using while loop
i = 1
while (i <= 10):
    print(number,"x",i,"=",number*i)
    i = i+1
    
input("press ENTER to exit")
