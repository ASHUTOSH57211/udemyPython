class rectangle:
    #class variables
    count = 0

    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        rectangle.count += 1 
    
    def area(self):
        return(self.length*self.breadth)

    @classmethod
    def rectCount(cls):
        print(cls.count)


rect = rectangle(5,10)
rect2 = rectangle(10,20)

#calling a classmethod
rectangle.rectCount()

print(rect.area())
    

