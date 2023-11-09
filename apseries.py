initialNumber = int(input("enter the initial number"))
commonDiiference = int(input("enter the common difference"))
nthTerm = int(input("Enter the nth term til which ap to be found"))

print(initialNumber)
for i in range(1,nthTerm):
    initialNumber = initialNumber+commonDiiference
    print(initialNumber)
