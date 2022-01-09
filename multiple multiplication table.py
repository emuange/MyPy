number_of_tables = int(input("Enter the number of multiplication tables to print: "))
iter = 1

#using while and for 
while (iter <= number_of_tables):
    for i in range(1,11):
        number = iter
        print(number,"x",i,"=",number*i)
    iter = iter + 1

#using nested fors
for i in range(1,(number_of_tables + 1)):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

#using nested while
i=1
while (i <= number_of_tables):
    j=1
    while(j <= 10):
        print(i,"x",j,"=",i*j)
        j = j + 1
    i = i + 1

#using for then while
for i in range(1,(number_of_tables + 1)):
    j=1
    while(j <= 10):
        print(i,"*",j,"=",i*j)
        j = j + 1
  