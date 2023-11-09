number = int(input("Enter the number "))
sum = 0

while number>0:
    remainder = number%10
    sum = sum+remainder
    # sum = (sum*10)+remainder  - for reverse of number
    number= number//10

print("the sum is ", sum)
