import sys
import math

#Instanciation des variables
n = int(input())
liste_des_chevaux = list()
plus_faible_ecart_de_puissance = 10000000

for i in range(n):
    pi = int(input())
    
    #Si on nous donne la puissance du premier cheval
    if i==0:
        liste_des_chevaux.append(pi)
        
    else:
        #On parcourt la liste des chevaux déjà établie pour l'insérer au bon emplacement : on trie le tableau au-fur-et-à-mesure
        
        for j in range(i):
            if pi < liste_des_chevaux[j]:
                liste_des_chevaux.insert(j, pi)
                break
                
            elif j==i-1:
                liste_des_chevaux.append(pi)
                
#On parcourt la liste des chevaux déjà établie pour l'insérer au bon emplacement : on trie le tableau au-fur-et-à-mesure
for i in range(1, len(liste_des_chevaux)):
    if liste_des_chevaux[i] - liste_des_chevaux[i-1] < plus_faible_ecart_de_puissance:
        plus_faible_ecart_de_puissance = liste_des_chevaux[i] - liste_des_chevaux[i-1]
    

#Affichage du résultat
print(plus_faible_ecart_de_puissance)
