import sys
import math

#Instanciation des variables
w, h, count_x, count_y = [int(i) for i in input().split()]
total_squares = 0
list_x = [0]
list_y = [0]

#Récupération des points sur l'axe x
for i in input().split():
    x = int(i)
    list_x.append(x)

#Récupération des points sur l'axe y
for i in input().split():
    y = int(i)
    list_y.append(y)

#Ajout du point final de chaque axe
list_x.append(w)
list_y.append(h)

#Calcul du nombre total de carrés
for i, _ in enumerate(list_x):
    for ii in range(i+1, len(list_x)):
        if i < len(list_x) - 1:
            x_segment_size = list_x[ii] - list_x[i]
            for j, _ in enumerate(list_y):
                for jj in range(j+1, len(list_y)):
                    if j < len(list_y) - 1:
                        y_segment_size = list_y[jj] - list_y[j]
                        if y_segment_size == x_segment_size:
                            total_squares += 1
print(total_squares)
