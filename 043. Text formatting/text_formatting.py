import sys
import math

def clean_punctuations(punctuation, intext):
    too_many_punctuations = True
    #On retire les ponctuations en trop
    while(too_many_punctuations):
        if punctuation+punctuation in intext:
            intext = intext.replace(punctuation+punctuation, punctuation)
            
        elif " "+punctuation in intext:
            intext = intext.replace(" "+punctuation, punctuation)   
        else:
            too_many_punctuations = False
    if punctuation != " ":
        intext = intext.replace(punctuation, punctuation+" ")
    return intext


intext = input()

for punctuation in ["!", ".", ",", "?", ";", ":", " "]:
    intext = clean_punctuations(punctuation, intext)

for i in range(len(intext)):
    
    #Si la première lettre n'est pas en majuscule
    if (i == 0 and not intext[i].isupper()) or (i>0 and intext[i-1] == " " and intext[i-2] in [".", "?", "!"] and not intext[i].isupper()):
        intext = intext[0:i]+intext[i].upper()+intext[i+1:]
            
    #Si on est pas sur la première lettre, que le caractère à l'index -2 n'est pas une ponctuation et que la lettre est en majuscule,
    #On la passe en minuscule
    elif i !=0 and not intext[i-2] in [".", "?", "!"] and intext[i].isupper():
        intext = intext[0:i]+intext[i].lower()+intext[i+1:]
        
#Si on a un espace tout à la fin, on l'enlève
if intext[-1] == " ":
    intext = intext[:-1]
    
print(intext)