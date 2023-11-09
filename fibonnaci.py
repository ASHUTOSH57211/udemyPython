firstterm  = 0
secondterm = 1
nthTErm= int(input("Enter no of terms needed"))
print("first term is",firstterm)
print("second term is",secondterm)
print("next", nthTErm,"terms are")
for i in range (0,nthTErm):
    c = firstterm+secondterm
    firstterm = secondterm
    secondterm = c
    print(c)

