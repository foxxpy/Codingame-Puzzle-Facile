import sys
import math

def game(bet, ball, call, number):
    """Core of the casino game"""
    if call == "EVEN" and ball % 2 == 0 and ball != 0 or\
    call == "ODD" and ball % 2 == 1:
        return bet * 2
    
    elif call == "PLAIN" and number == ball:
        return bet*36

    else:
        return 0



#Instanciation des variables
rounds = int(input())
cash = int(input())

for i in range(rounds):
    #We substract the money from the bet to cash
    bet = math.ceil(0.25*cash)
    cash = cash - bet
    
    #We get the information we need to play the game
    play = input().split(" ")
    ball = int(play[0])
    call = play[1]
    number = int(play[2]) if len(play) == 3 else 0
    
    #We play
    cash += game(bet, ball, call, number)
    
#Answer
print(cash)