'''
1. Area of triangle =  0.5 *b*h

2. Area of rhombus =   0.5 *(a+b)*h

3. Displacement = (v**2- u**2)/ 2*a
'''

base = int(input("Enter base of Triangele"))
Height = int(input("Enter height of Triangle"))
a = int(input("Enter a "))
b = int(input("Enter b "))
u = int(input("Enter u "))
v = int(input("Enter v "))

TriangleArea = 0.5*base*Height
RhombusArea = 0.5 *(a+b)*Height
Displacement = (v**2- u**2)/ 2*a
print(TriangleArea)
print(RhombusArea)
print(Displacement)




