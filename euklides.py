def Euklides(a, b):
    while a!= b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(Euklides(10, 25))