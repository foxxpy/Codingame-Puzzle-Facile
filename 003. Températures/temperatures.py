import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temperature_plus_proche_de_zero = int()
j = 0

for i in input().split():
    
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    
    print("Temperature : "+str(t), file=sys.stderr)

    #Si c'est la première température donnée
    if j == 0:
        distance_de_zero = abs(t)
        temperature_plus_proche_de_zero = t
        
    #Si ce n'est pas la première température donnée
    else:
        #Si la température donnée est plus proche de zéro que la température déjà enregistrée
        if abs(t) < abs(temperature_plus_proche_de_zero):
            distance_de_zero = abs(t)
            temperature_plus_proche_de_zero = t
            
        #Si la température donnée est à la même distance que la température la plus prôche de zéro et que celle-ci est positive
        elif abs(t) == abs(temperature_plus_proche_de_zero) and t > temperature_plus_proche_de_zero:
            temperature_plus_proche_de_zero = t
            
    j = j + 1

            
        

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(temperature_plus_proche_de_zero)