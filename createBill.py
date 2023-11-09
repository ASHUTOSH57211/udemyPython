#create a menu with 25 space where the space should have dots(.). totla enter 5 items
itemlist = "items"
pricetag = "price"
length =" " * (25 - (len(itemlist)+len(pricetag)))
menu = itemlist+length+pricetag+"\n"
for i in range (0,5): 
    item = input("enter item name")
    price = input("Enter price")
    totlalen = len(item)+len(price)
    dots = "."*(25-totlalen)

    finalitem = item+dots+price
    menu = menu+finalitem+ "\n"

print(menu)