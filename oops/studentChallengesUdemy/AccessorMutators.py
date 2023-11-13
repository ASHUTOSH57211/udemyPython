class Customer:
    def __init__(self,name,phno):
        self.name = name
        self.phno = phno
    
    def getName(self):
        return self.name

    def getphNo(self):
        return self.phno
    
    def setPhno(self,phno):
        self.phno = phno

c1  =Customer("Ashu",8763667430)

print(c1.getName())
print(c1.getphNo())
c1.setPhno(7008628506)
print(c1.getphNo())
        