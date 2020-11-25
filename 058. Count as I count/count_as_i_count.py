import sys
import math

#Instanciation des variables
n = int(input())
score_to_reach = 50 - n
total_solutions = 0
all_solutions = []

#On cherche toutes les combinaisons possibles
for i in range(1,13):
    if i == score_to_reach:
        all_solutions.append([i])
    if i < score_to_reach:
        for j in range(1,13):
            if i+j == score_to_reach:
                all_solutions.append([i,j])               
            if i+j < score_to_reach:
                for k in range(1,13):
                    if i+j+k == score_to_reach:
                        all_solutions.append([i,j,k])
                    if i+j+k < score_to_reach:
                        for l in range(1,13):
                            if i+j+k+l == score_to_reach:
                                all_solutions.append([i,j,k,l])

#Sachant qu'il existe deux solutions pour chaque score hormis le 1
#On met 2 à la puissance du nombre de points supérieurs à 1 pour chaque combinaison
for s in all_solutions:
    num_sup_1 = 0
    for num in s:
        if num > 1:
            num_sup_1 += 1
    total_solutions += 2**(num_sup_1)

print(total_solutions)
