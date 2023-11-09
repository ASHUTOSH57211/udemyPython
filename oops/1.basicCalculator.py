class Calculator:
    def __init__(self,num1,num2):
        self.number1 = num1
        self.number2 = num2

    def add(self):
        return self.number1 +self.number2
    
    def subtract(self):
        return self.number1 -self.number2
    
    def multiply(self):
        return self.number1 *self.number2
    
    def divide(self):
        return self.number1 //self.number2

n = Calculator(20,10)
print(n.add())
print(n.subtract())
print(n.multiply())
print(n.divide())


