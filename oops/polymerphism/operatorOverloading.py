# Adding two rational numbers

class Rational:
    def __init__(self,p,q):
        self.p = p
        self.q = q

    def __add__(self,other):
        
        self.a = self.p*other.q + self.q*other.p
        self.b = self.q*other.q
        return self.a,self.b

    
r1 = Rational(2,3)
r2 = Rational(2,5)

print(r1+r2)

        