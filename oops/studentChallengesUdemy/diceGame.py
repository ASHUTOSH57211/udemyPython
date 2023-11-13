#QUESTION -> Given a dice. create a class dice with attribte sides and a function roll dice which creates a random number everytime it is called

from random import randint

class Dice:
    def __init__(self,s):
        self.side = s
    
    def roll_dice(self):
        print(randint(1,self.side))

dice=  int(input("Enter no of dice maximum two"))

if dice==1:
    side = 6
    d = Dice(side)
    d.roll_dice()
elif dice==2:
    side=12
    d = Dice(side)
    d.roll_dice()
else:
    print("enter maximum two dice minimum 1")