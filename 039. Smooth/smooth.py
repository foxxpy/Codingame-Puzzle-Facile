import sys
import math

#Instanciation des variables
n = int(input())

for i in range(n):
    f = int(input())
    
    #Tant que le nombre de fruits est un multiple de 5, un multiple de 3 ou un multiple de 2
    while(f % 5 == 0 or f % 3 == 0 or f % 2 == 0):
        
        if f%5 == 0:
            f = f // 5
            
        elif f%3 == 0:
            f = f // 3
            
        else:
            f = f // 2
    
    #Victoire si on réduit le tout à UNE SEULE pastèque
    if f == 1:
        print("VICTORY")
    else:
        print("DEFEAT")