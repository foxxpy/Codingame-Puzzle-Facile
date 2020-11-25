import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def decimalToBinary(num):
    """Convertit un nombre décimal en un nombre binaire"""
    return bin(num).replace("0b", "")
    
def messageToBinary(message):
    """Convertit les caractères d'une chaîne de caractères en binaire"""
    binary_message = ""
    
    #On convertit chaque lettre du message en binaire
    for letter in message:
        decimal = ord(letter)
        binary = decimalToBinary(decimal)
        
        #Si la lettre en binaire contient moins de 7 bit, on rajoute des zéros au début
        while (len(binary) < 7):
            binary = "0"+binary

        binary_message += binary
        

        
    return binary_message
    
def binaireToUnaire(binary_message):
    """Convertit un message binaire en un message unaire"""
    unaire = ""
    i = 0    
    
    #Tant qu'on a pas parcouru tout le message binaire pour le convertir
    while(i < len(binary_message)):
        caractere = binary_message[i]
        j = 1
        
        while((i+j) < len(binary_message) and binary_message[i+j] == caractere):
            j += 1
        
        if caractere == "0":
            unaire += "00 "
            
        else:
            unaire += "0 "
            
        i = i + j    
        bloc = "0" * j
        unaire += bloc + " "
        
        
    unaire = unaire[:-1] #On supprime l'espace en trop à la fin
    return unaire

#Main program
message = input()
binary_message = messageToBinary(message)
unaire = binaireToUnaire(binary_message)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


print(unaire)