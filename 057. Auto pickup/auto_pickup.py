import sys
import math

#Instanciation des variables
n = int(input())
packet = input()
list_drops = []

while(len(packet) > 0):
    item_id_length = int("0b"+packet[3:7], 2)
    if packet[0:3] == "101":
        list_drops.append((packet[3:7], packet[7:7+item_id_length]))
    packet = packet[7+item_id_length:]


for drop in list_drops:
    print("001"+drop[0]+drop[1], end="")