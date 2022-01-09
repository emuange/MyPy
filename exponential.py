base_num = int(input("Enter the base number: "))
exponent = int(input("Enter the exponenet: "))
answer = 1
for i in range(1,(exponent + 1)):
    answer = answer * base_num

print(answer)

#using while
answer = 1
i = 1
while (i <= exponent):
    answer = answer * base_num
    i = i + 1

print(answer)
