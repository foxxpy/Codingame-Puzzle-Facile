import sys
import math

#Instanciation des variables
n = int(input())
list_pi = list()
distance_max = 100000000000

#Calcul des distances
for i in range(n):
    v, e = [int(j) for j in input().split()]
    pi = (v,e)
    
    #On compare la puissance du cheval avec tous les autres chevaux
    for j in range(i):
        v1 = pi[0]
        e1 = pi[1]
        v2 = list_pi[j][0]
        e2 = list_pi[j][1]
        
        distance = abs(v2-v1)+abs(e2-e1)
        if distance < distance_max:
            distance_max = distance
            
    list_pi.append(pi)
        
print(distance_max)