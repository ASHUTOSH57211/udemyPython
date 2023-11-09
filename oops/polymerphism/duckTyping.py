class Duck:
    def walk(self):
        print("duck in walking")
    def talk(self):
        print("duck in talking")

class Dog:
    def walk(self):
        print("dog in walking")
    def talk(self):
        print("dog in talking")

for obj in Duck(),Dog():
    obj.walk()
    obj.talk()


# Also ,
# def pet (animal):
#     animal.talk()
#     animal.walk()

# d = duck()
# pet(d)

# do = dog()
# pet(do)
    
