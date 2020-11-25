import sys
import math


def step(card, num_step):
    card = card.split(" ")
    list_step = list()
    range_start = 0 if num_step == 1 else 1
    
    #We double every second digit for every group of numbers in the card number
    for group_nb in card:
        for i in range(range_start, len(group_nb), 2):
            #If this is the step 1, we calculate the numbers according to the rules given
            if num_step == 1:
                number_calculated = int(group_nb[i])*2 if int(group_nb[i]) * 2 < 10 else int(group_nb[i])*2 - 9
            #If this is the step 2, we just get the numbers in the odd places
            else:
                number_calculated = int(group_nb[i])
            list_step.append(number_calculated)
    
    #Return a list of numbers
    return list_step
        
    
n = int(input())

for i in range(n):
    card = input()
    list_step_1 = step(card, 1)
    list_step_2 = step(card, 2)
    sum_numbers = sum(list_step_1) + sum(list_step_2)
    
    if sum_numbers % 10 == 0:
        print("YES")
    else:
        print("NO")
