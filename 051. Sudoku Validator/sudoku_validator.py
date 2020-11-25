import sys
import math

grid = []

def validator(grid):
    
    for i in range(9):
        column = []

        for j in range(9):

            #On regarde si un nombre est présent plus d'une fois sur une ligne
            if grid[i].count(j+1) > 1:
                return "false"

            #On regarde si un nombre est présent plus d'une fois sur une colonne
            if grid[j][i] in column:
                return "false"
            column.append(grid[j][i])

    #On regarde si les sous-grilles sont correctes
    for y0 in [0,3,6]:
        for x0 in [0,3,6]:
            subgrid = []
            for i in range(0,3):
                for j in range(0,3):
                    if grid[y0+i][x0+j] in subgrid:
                        return "false"
                    subgrid.append(grid[y0+i][x0+j])

    #Si on a trouvé aucune erreur, la grille est correcte et on renvoie "true"
    return "true"


#On récupère les lignes de notre grille de sudoku
for i in range(9):
    grid_line = []
    for j in input().split():
        n = int(j)
        grid_line.append(n)
    grid.append(grid_line)

#On affiche le résultat
answer = validator(grid)
print(answer)