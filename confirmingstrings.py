p1 = input("Enter a string")
p2 = input("Enter another string")

if p1==p2:
    print("confirmed")
elif p1.casefold() == p2.casefold():
    print("Check cases")
else:
    print("not confirmed")