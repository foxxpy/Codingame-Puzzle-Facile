import sys
import math

#Instanciation des variables
n = input()
total_clumps = 0
normal = True
last_mod = 0

#On cherche si le nombre de clumps est croissant quand la base croît elle aussi
for b in range(1, 10):
    nb_clumps = 0
    for j, num in enumerate(n):
        if j == 0 or j > 0 and int(num) % b != last_mod:
            last_mod = int(num) % b
            nb_clumps += 1

    if nb_clumps < total_clumps:
        normal = False
        break

    else:
        total_clumps = nb_clumps

if normal:
    print("Normal")
else:
    print(b)