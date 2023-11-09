Amount = int(input("The selling price is Rs.")) 

if Amount <=1000:
    discount = 0.10*Amount
    

elif 1000 < Amount <= 5000:
    discount = 0.20*Amount
   

elif 5000 < Amount <= 10000:
    discount = 0.30*Amount
  

else:
    discount = 0.50*Amount

    
discount_Amnt = Amount-discount
print("the amount is Rs.",Amount,"And discounted price is Rs.",discount_Amnt)