import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#lon_a : longitude utilisateur, lon_b : longitude défibrillateur
#lat_a : latitude utilisateur, lat_b : latitude défibrillateur
lon_a = float(input().replace(",", "."))
lat_a = float(input().replace(",", "."))
n = int(input())

for i in range(n):
    defib = input().split(";")
    
    #On récupère la latitude et la longitude du défibrillateur
    lon_b = float(defib[4].replace(",", "."))
    lat_b = float(defib[5].replace(",", "."))
    
    #On calcule la distance entre l'utilisateur et le défibrillateur
    x = (lon_b - lon_a) * math.cos((lat_a+lat_b)/2)
    y = lat_b - lat_a
    d = math.sqrt(x**2 + y**2)*6371

    #Si c'est le premier défibrillateur qui nous est donné    
    if i==0 or d < d_min:
        d_min = d
        defibrillateur_le_plus_proche = defib[1]
        

    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(defibrillateur_le_plus_proche)