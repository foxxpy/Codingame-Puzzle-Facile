import sys
import math

#Instanciation des variables
#b : Bitstring
b = input()
liste_des_chaines_de_un = list()
longest_sequence = int()

liste_des_chaines_de_un = b.split("0")

#Si il n'y a aucun "1" dans b (bistring)
if not "1" in b:
    print("1")
   
#Si il n'y a aucun "0" dans b (bitstring)
elif not "0" in b:
    print(str(len(b)))

#Si il y'a des "0" et des "1"
else:
    #On parcourt notre liste contenant les chaînes de "1", et on additionne la longueur de chaque séquence avec la séquence suivante
    #Ce qui représente la taille de la séquence de 1 si on y transformait le 0 entre les deux en 1
    for i in range(0, len(liste_des_chaines_de_un) - 1):
        length_sequence = len(liste_des_chaines_de_un[i]) + len(liste_des_chaines_de_un[i+1]) + 1
        if length_sequence > longest_sequence:
            longest_sequence = length_sequence
           

    print(str(longest_sequence))