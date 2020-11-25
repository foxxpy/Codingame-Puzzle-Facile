import sys
import math

#Instanciation des variables
n = int(input())
cards = []

#On récupère les valeurs des cartes
for i in input().split():
    x = int(i)
    cards.append(x)

total_money = 0

#On fait la somme des cartes aux valeurs les plus faibles (indice 0 et 1) en retriant la liste à chaque tour de boucle
while(len(cards) > 1):
    cards = sorted(cards)
    sum_cards = cards[0] + cards[1]
    total_money += sum_cards
    cards = [sum_cards] + cards[2:]

#Affichage du résultat final
print(total_money)