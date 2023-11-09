class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
    def circumference(self):
        return 2*3.14*self.radius
    
cir = circle(21)
print(cir.area())
print(cir.circumference())