import sys
import math
    
def calculate_total_days(month, day, days_in_a_month):
    total_days = 0
    for key, value in days_in_a_month.items():
        if key == month:
            break
        else:
            total_days += value
    total_days += day
    return total_days

#Variables données par codingame
leap_year = int(input())
list_days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
source_day_of_week, source_month, source_day_of_month = input().split()
source_day_of_month = int(source_day_of_month)
target_month, target_day_of_month = input().split()
target_day_of_month = int(target_day_of_month)

#Instanciation des variables
days_of_week = {
    "Monday" : None,
    "Tuesday" : None, 
    "Wednesday" : None, 
    "Thursday" : None, 
    "Friday" : None, 
    "Saturday" : None, 
    "Sunday" : None
}

days_in_a_month = { "Jan" : 31,
"Feb" : 28,
"Mar" : 31,
"Apr" : 30,
"May" : 31,
"Jun" : 30,
"Jul" : 31,
"Aug" : 31,
"Sep" : 30,
"Oct" : 31,
"Nov" : 30,
"Dec" : 31
}

if leap_year:
    days_in_a_month["Feb"] = 29

#On calcule le nombre total de jours dans l'année pour arriver aux dits jours de départ et d'arrivée. Puis on calcule
#la différence
total_days_source = calculate_total_days(source_month, source_day_of_month, days_in_a_month)
total_days_target = calculate_total_days(target_month, target_day_of_month, days_in_a_month)
difference_total_days = total_days_target - total_days_source

difference_total_days %= 7

#On réarrange les jours de la semaine pour qu'ils correspondent à l'ordre partant du jour source
#Si le jour source était un jeudi, alors la liste des jours de la semaine commencera par jeudi puis vendredi etc...
index_source_day_of_week = list_days_of_week.index(source_day_of_week)
list_days_of_week = list_days_of_week[index_source_day_of_week:]+list_days_of_week[:index_source_day_of_week]

print(list_days_of_week[difference_total_days])

