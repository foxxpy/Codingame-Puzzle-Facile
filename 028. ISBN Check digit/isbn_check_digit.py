import sys
import math

def calculate_remainder(isbn):
    """Calcul le reste de la dernière division selon les consignes de l'énoncé"""
    print(isbn, file=sys.stderr)
    list_multiplier = list()
    modulo = 0
    sum_of_digits = 0
    
    if len(isbn) == 10:
        list_multiplier = [x for x in range(10, 1, -1)]
        modulo = 11
    elif len(isbn) == 13:
        list_multiplier = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
        modulo = 10
    for i, number in enumerate(isbn):
        if i < len(isbn) - 1:
            sum_of_digits += int(number) * list_multiplier[i]
        elif i == len(isbn)-1 and number == "X":
            sum_of_digits += 10
        else:
            sum_of_digits += int(number)
    return sum_of_digits % modulo 

#Instanciation des variables
n = int(input())
y = 0
list_invalid_isbn = list()

for i in range(n):
    isbn = input()
    valid_isbn = True
    
    #Si un numéro isbn donné n'a ni une longueur de 10 ni une longueur de 13, il est invalide.
    #Si on trouve un "X" à un autre emplacement que le dernière caractère également.
    if len(isbn) != 10 and len(isbn) != 13 or "X" in isbn and  0 <= isbn.find("X") < len(isbn) - 1 or \
    "X" in isbn and len(isbn) == 13:
        valid_isbn = False
        
    else:
        remainder = calculate_remainder(isbn)
        #Si le reste est de 0, le dernier nombre supposé du nombre isbn est 0
        #Sinon on calcule le dernier nombre selon les règles de l'énoncé
        if remainder != 0:
            valid_isbn = False

    if not valid_isbn:
        y += 1
        list_invalid_isbn.append(isbn)
    

print(str(y)+" invalid:")
for isbn in list_invalid_isbn:
    print(isbn)