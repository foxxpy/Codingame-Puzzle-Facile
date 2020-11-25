import sys
import math

#Instanciation des variables
n = int(input())
list_score = list()
i, j, k = 0, 0, 0

#Pour chaque i, j, k tant qu'ils sont inférieurs au score n
while(i*5 <= n):
    j = 0
    while(j <=i and (i*5+j*2) <= n):
        k = 0
        while(i*5+j*2+k*3 <= n):
            if i*5+j*2+k*3 == n:
                list_score.append([i, j, k])
            k = k +1
        j = j + 1
    i = i + 1

#On affiche tous les essais, transformations, pénalties possibles
for score in list_score:
    print(str(score[0]), str(score[1]), str(score[2]))