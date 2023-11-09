''' A simple code written with the help of getters and setters(Accessors and Mutators)
    Here a class book is defined with attributes like title author and year

    getters(Accessors) - used to get the value that is passed
    setters(Mutators) - used to modify the value 
    thes are very helpful to modify if one object is created
    
    '''


class Book:
    def __init__(self,title,author,year):
        
        self.title = title
        self.author = author
        self.year=year
    
    def gettitle(self):
        print(self.title)

    def settitle(self,title):
        self.title = title
    
    def getauthor(self):
        print(self.author)

    def setauthor(self,author):
        self.author = author

    def getyear(self):
        print(self.year)

    def setyear(self,year):
        self.year=year
    
    
b1 = Book("ABC","Ashu",2002)
b1.getauthor()
b1.setauthor("Rambo")
b1.getauthor()