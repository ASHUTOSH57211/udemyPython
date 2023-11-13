class Currency:
    def __init__(self,country,rate):
        self.country = country
        self.rate = rate
    def get_country(self):
        return self.country
    
    def set_counter(self,country):
        self.country = country
    
    def get_rate(self):
        return self.rate
    
    def set_rate(self,rate):
        self.rate = rate

    def convert(self,amount):
        return amount * self.rate 

curr = Currency("US",70)
print(curr.convert(100))