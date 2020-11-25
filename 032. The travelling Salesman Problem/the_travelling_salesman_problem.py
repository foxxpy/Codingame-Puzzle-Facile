import sys
import math

def distance(x_a, x_b, y_a, y_b):
    """Calcule la distance entre deux points"""
    return math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2)

def get_coordinates(point_1, point_2):
    """Renvoie les coordonnées de 2 points"""
    x_a = point_1["x"]
    x_b = point_2["x"]
    y_a = point_1["y"]
    y_b = point_2["y"]
    
    return x_a, x_b, y_a, y_b

#Instanciation des variables
n = int(input())
points = list()
distance_min = 10000
total_distance = 0

#On récupère tous les points
for i in range(n):
    x, y = [int(j) for j in input().split()]
    points.append({ "x" : x, "y" : y})

i = 0
points_temp = points[:]

#Tant qu'il reste des points à parcourir
while(len(points) > 1):
    distance_min = 10000
    nearest_point = 0
    
    #On parcourt les points et on cherche le point le plus prôche du point à l'indice i
    for j in range(0, len(points)):
        if i != j:
            x_a, x_b, y_a, y_b = get_coordinates(points[i], points[j])
            distance_i_j = distance(x_a, x_b, y_a, y_b)
            if distance_i_j < distance_min:
                distance_min = distance_i_j
                nearest_point = points[j]

    #On retire le point à l'indice i, et on garde en mémoire le pointle plus prôche que l'on vient de trouver dans i
    points.pop(i)
    i = points.index(nearest_point)
    total_distance += distance_min
    
x_a, x_b, y_a, y_b = get_coordinates(points_temp[0], nearest_point)
total_distance += distance(x_a, x_b, y_a, y_b)

#On arrondit la distance totale et seulement la distance totale
print(round(total_distance))