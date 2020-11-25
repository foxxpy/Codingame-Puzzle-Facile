import sys
import math

def change_message_with_pseudo_random_number(message, pseudo_random_number, alphabet):
    new_message = ""
    for i, letter in enumerate(message):
        i = i if pseudo_random_number > 0 else -i
        index_letter = alphabet.index(letter) + pseudo_random_number + i
        while(not -26 < index_letter < 26):
            if pseudo_random_number > 0:
                index_letter = index_letter - 26
            else:
                index_letter += 26
        new_message += alphabet[index_letter]
    
    return new_message

def encode(message, list_rotor, alphabet):

    for rotor in list_rotor:
        new_message = ""
        for letter in message:
            new_message += rotor[alphabet.index(letter)]    
        message = new_message   
    return message

def decode(message, list_rotor, alphabet):
    for rotor in list_rotor[::-1]:
        new_message = ""
        for letter in message:
            new_message += alphabet[rotor.index(letter)]
        message = new_message
    return message


#Instanciation des variables
operation = input()
pseudo_random_number = int(input())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_rotor = list()

#On ajoute nos rotors à notre liste de rotor
for i in range(3):
    rotor = input()
    list_rotor.append(rotor)
message = input()

if operation == "ENCODE":
    message = change_message_with_pseudo_random_number(message, pseudo_random_number, alphabet)
    final_message = encode(message, list_rotor, alphabet)
else:
    final_message = decode(message, list_rotor, alphabet)
    final_message = change_message_with_pseudo_random_number(final_message, pseudo_random_number*-1, alphabet)
    
print(final_message)