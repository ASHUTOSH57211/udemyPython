class Animal:

    def sound(self):
        print("the above animal is having soung ")


class Dog(Animal):
    def sound(self):
        return "woof"

class cat(Animal):
    def sound(self):
        return "meow"    
        

c = cat()
print(c.sound())