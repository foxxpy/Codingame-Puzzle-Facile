import sys
import math

class Candle: 
    def __init__(self, pos, l):
        self.pos = pos
        self.l = l
        
    def light_room(self, pos, list_lighted_cell, l, n):
        """Allume les lumières dans la salle selon les règles de l'énoncé"""
        i = pos[0]
        j = pos[1]
        
        #Si on est dans les limites de la pièce
        if i>= 0 and j >=0 and j < n and i < n:
            #Si la case n'est pas éclairée, on l'éclaire
            if list_lighted_cell[i][j].l == 0:
                list_lighted_cell[i][j].l = l
                list_lighted_cell[i][j].light_by_candle = self
                
            #Si la case est éclairée mais par une autre bougie
            elif list_lighted_cell[i][j].l > 0 and not self.same_candle(list_lighted_cell[i][j].light_by_candle):
                list_lighted_cell[i][j].l = self.l
    
            #Si la case est éclairée par la même bougie mais plus faiblement
            elif list_lighted_cell[i][j].l < l and self.same_candle(list_lighted_cell[i][j].light_by_candle):
                list_lighted_cell[i][j].l = l
                    
            l = l - 1
            if l > 0:
                for k in [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1, j-1), (i+1,j), (i+1,j+1)]:
                    list_lighted_cell = self.light_room(k, list_lighted_cell, l, n)
            
        return list_lighted_cell
                
                
    def same_candle(self, another_candle):
        """Teste si cette bougie est la même qu'une autre bougie"""
        if self.pos == another_candle.pos:
            return True
        else:
            return False
         
class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.l = 0
        self.light_by_candle = None
        

#Variables instanciation
n = int(input())
l = int(input())
list_candle = list()
list_lighted_cell = list()
nb_dark_spot = 0

#Creation of the room
for i in range(n):
    line_cell = list()
    line = input().split(" ")

    for j in range(n): #We fill Cell in list_lighted_cell with their position
        if "C" == line[j]: #We get the position of the candles into a tuple (line, column)
            list_candle.append(Candle((i,j), l))
        line_cell.append(Cell((i,j)))
    list_lighted_cell.append(line_cell)

#Pour chaque bougie dans notre liste de bougies, on éclaire la zone alentour
for candle in list_candle:
    list_lighted_cell = candle.light_room(candle.pos, list_lighted_cell, l, n)

#On recherche les zones d'ombre
for line_cell in list_lighted_cell:
    for cell in line_cell:
        if cell.l == 0:
            nb_dark_spot += 1
    
#On affiche le résultat
print(nb_dark_spot)
