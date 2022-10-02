import math
#newton's method:
def new_met(t):
    return ( (t) - ( ((math.e) ** ((t**2) - 2) -  3*(math.log(t)) ) / ( (2 * t * (math.e ** (t**2 - 2))) - (3/t) ) ) )

#secant method y = x1, z = xn-1 //x0
def sec_met(y, z):
    return ( 
        (y) -  ( ((math.e) ** ((y**2) - 2) -  3*(math.log(y))) * (y - z))  / ( (((math.e) ** ((y**2) - 2)) -  3*(math.log(y))) - ((math.e) ** ((z**2) - 2) -  3*(math.log(z))) ) 
    )

#part1
test = 0
p = 1.5
print("Newton's method for x0 = 1.5: ")
print(p)
while(abs(p - test) > 0.0000000000000001):
    test = p
    p = new_met(p)
    print(p)

#part2
p = 0.1
test = 0
print("Newton's method for x0 = 0.1: ")
print(p)
while(abs(p - test) > 0.0000000000000001):
    test = p
    p = new_met(p)
    print(p)
    
#part3
z = 1.5
y = 1.4
test = 0
print("Secant method for x0 = 1.5 and x1 = 1.4 : ")
print(z)
print(y)
while(abs(y - test) > 0.00000000001):
    test = z
    z = y 
    y = sec_met(y, test)
    print(y)
