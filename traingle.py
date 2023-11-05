a=float(input("enter the first side: "))
b=float(input("enter the second side: "))
c=float(input("enter the third side: "))

#calculating the semi-perimeter if triangle
s=(a+b+c)/2

#calculting the perimeter of the triangle
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print('area of the triangle is %0.2f',area)