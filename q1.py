p = 1 #p0
result = round((21)**(1/3), 14)

def rec_a(t):
    return ( (20*t + (21/(t**2))) / 21 )

def rec_b(t):
    return ( t - (((t**3) - 21) / (3*(t**2))) )

def rec_c(t):
    return ( t - ( ((t**4) - (21*t)) / ( (t**2) - 21 ) ) )

def rec_d(t):
    return (21/t)**(1/2)

# convergence of a
p = 1
test = 0
print("Convergence of A: ")
print(p)
while(test != result):
    p = rec_a(p)
    test = round(p, 14)
    print(test) 

# convergence of b(newton)
test = 0
p = 1
print("Convergence of B: ")
print(p)
while(test != result):
    p = rec_b(p)
    test = round(p, 14)
    print(test)

#convergence of c
test = 0
p = 1
k = rec_c(p)
print("Convergence of C: ")
print(p)
while(k-p != 0):
    p = k
    k = rec_c(p)
    test = round(p, 14)
    print(test) 

#convergence of d
test = 0
p = 1
print("Convergence of D: ")
print(p)
while(test != result):
    p = rec_d(p)
    test = round(p, 14)
    print(test) 