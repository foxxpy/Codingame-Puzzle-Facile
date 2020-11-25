import sys
import math

#Instanciation des variables
dict_correct = {"(" : ")", "[" : "]", "{" : "}"}
expression = input()
list_open = list()
correct = True

for c in expression:
    if c in ["(", "{", "["]:
        list_open.append(c)
    elif c in [")", "}", "]"]:
        #Si on a un caractère de fermeture alors que list_open est vide ou que le caractère d'ouverture précédent ne correspond pas
        if len(list_open) == 0 or (len(list_open) > 0 and dict_correct[list_open[len(list_open)-1]] != c):
            correct = False
            break
        #Sinon on retire le dernier caractère d'ouverture de list_open
        else:
            del list_open[-1]

#Pour vérifier qu'on a pas un caractère ouvert sans caractère de fermeture, on procède à un dernier test
if correct:
    correct = False if len(list_open) > 0 else True

print("true" if correct else "false")
