from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        print("Helo parent")
    
    def display(self):
        print("display parent")


class child(Parent):
    def show(self):
        print("hello child")
        
c = child()
c.show()
c.display()

# upon instantiating abstract class

# c = Parent()
# c.display()
# Traceback (most recent call last):
#   File "d:\udemyPython\oops\abstactclass.py", line 17, in <module>
#     c = Parent()
#         ^^^^^^^^
# TypeError: Can't instantiate abstract class Parent with abstract method show

