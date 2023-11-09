class rectangle:

    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    
    def area(self):
        return(self.length*self.breadth)
    
class cuboid(rectangle):

    def __init__(self,h,l,b):
        self.height = h
        super().__init__(l,b)

    def volume(self):
        return self.length*self.breadth*self.height
        
cub = cuboid(10,20,30)
print(cub.area())
print(cub.volume())