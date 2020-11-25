import sys
import math

def define_list_num_characters(message):
    sum_j, j = 1, 1
    list_j = list()

    while sum_j <= len(message):
        list_j.append(j)
        j = j + 1
        sum_j += j
    list_j.append(len(message) - sum(list_j))
    
    return list_j

def encode(message, n):
    """Encode le message selon les critères de l'énoncé"""
    list_j = define_list_num_characters(message)

    for i in range(n):
        final_message = ""
        begin = False
        for j in list_j:
            if begin:
                final_message = message[:j] + final_message
            else:
                final_message = final_message + message[:j]
            message = message[j:]
            begin = True if begin == False else False    

        message = final_message
    
    return message
    
def decode(message, n):
    """Décode le message selon les critères de l'énoncé"""
    list_j = define_list_num_characters(message)

    for i in range(n):
        begin = True if len(list_j) % 2 == 0 else False
        final_message = ""
        for j in list_j[::-1]:
            if begin:
                final_message = message[:j]+final_message
                message = message[j:]
            else:
                final_message = message[len(message) - j:] + final_message
                message = message[:len(message)-j]
            begin = True if begin == False else False    
        message = final_message
    
    return message

#Instanciation des variables
n = int(input())
message = input()

final_message = decode(message, n) if n > 0 else encode (message, abs(n))

#Affichage du message final
print(final_message)

