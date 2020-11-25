import sys
import math

#Instanciation des variables
n = int(input())
fraudulent = False
benford_percentage = {
    1 : [20.1, 40.1],
    2 : [7.6, 27.6],
    3 : [2.5, 22.5],
    4 : [0, 19.7],
    5 : [0, 17.9],
    6 : [0, 16.7],
    7 : [0, 15.8],
    8 : [0, 15.1],
    9 : [0, 14.6]
}

numbers = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0
}

#Pour chaque transaction on regarde le premier chiffre et on incrémente la quantité de ce chiffre
#dans le dictionnaire numbers
for i in range(n):
    transaction = input()
    j = 0
    while(not transaction[j].isnumeric() or transaction[j] == "0"):
        j = j + 1
    numbers[int(transaction[j])] += 1

#On calcule le pourcentage de présence de chaque chiffre en début de transaction et on les compare aux
#pourcentages de la loi de Benford. Si ils ne sont pas dans le range de la loi de Benford, le compte est frauduleux
for i in range(1,10):
    percentage = (numbers[i] / n) * 100

    if (not benford_percentage[i][0] < percentage < benford_percentage[i][1]):
        fraudulent = True
        break

#Affichage du résultat
print(str(fraudulent).lower())
