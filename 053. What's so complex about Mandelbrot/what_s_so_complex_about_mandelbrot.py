import sys
import math
import cmath

def split_c(c):
    """Split the string c to give the real and imaginary part of the complex number"""
    for i, char in enumerate(c):
        if char in ["+", "-"] and i > 0:
            return float(c[0:i]), float(c[i:-1])


#Instanciation des variables
c = input()
m = int(input())
re, im = split_c(c)
c = complex(re, im)

#Boucle parcourant les itérations en testant les valeurs absolues de f(n)
step = 0
for i in range(1,m+1):
    step = step**2 + c
    print(abs(step), file=sys.stderr)
    if abs(step) > 2:
        break

print(i)
