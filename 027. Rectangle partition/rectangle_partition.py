import sys
import math

def calculate_total_squares(main_list, second_list):
    """On calcule le nombre total de carrés dans le grand rectangle"""
    total_squares = 0
    for i in main_list:
        print(i, file=sys.stderr)
        total_squares += second_list.count(i)
        if len(second_list) == 0:
            return total_squares 
    return total_squares

def add_to_list(list_axis, num):
    """On calcule les segments représentants les distances entre chaque ligne/column dans le rectangle"""
    final_list = []
    for i in list_axis:
        axis_size = i - num
        if axis_size < 0:
            axis_size = abs(axis_size)
        final_list.append(axis_size)
    return final_list

#Instanciation des variables
w, h, count_x, count_y = [int(i) for i in input().split()]
list_x, list_y = [0, w], [0, h]
final_list_x, final_list_y = [w], [h]

for i in input().split():
    x = int(i)
    final_list_x += add_to_list(list_x, x)
    list_x.append(x)
    
for i in input().split():
    y = int(i)
    final_list_y += add_to_list(list_y, y)
    list_y.append(y)

#On choisit une liste principale qui sera la liste la plus petite entre final_list_x, final_list_y pour optimiser le 
#processus
main_list = final_list_y if len(final_list_y) <= len(final_list_y) else final_list_x
other_list = final_list_x if main_list == final_list_y else final_list_y
total_squares = calculate_total_squares(main_list, other_list)
    
print(total_squares)