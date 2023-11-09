# find prime numbers in a number range

NumberRAnge = int(input("enter range to find prime numbers"))

for i in range (1,NumberRAnge+1):
    count =0
    for j in range (1,i+1):
        if i%j==0:
            count+=1 
    if count==2:
        print(i)