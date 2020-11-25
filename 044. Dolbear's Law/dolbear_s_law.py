import sys
import math

#Instanciation des variables
m = int(input())
m_measures = []
tcs_n60 = []

#On récupère les mesures et on effectue le calcul N60
for i in range(m):
    line = [int(x) for x in input().split(" ")]
    m_measures.append(line)
    N60 = sum(line)
    TC = 10 + (N60 - 40) / 7
    tcs_n60.append(TC)

#On calcule la moyenne avec la formule N60
avg = round(sum(tcs_n60) / len(tcs_n60), 1)
print(avg)

#Si la moyenne de la formule n60 est comprise entre 5 et 30, on calcule la moyenne des N8
if 5 <= avg <= 30:
    total_measure = []
    #On créé une liste avec la totalité des mesures
    for measure in m_measures:
        total_measure += measure
        
    tcs_n8 = []
    #On ne parcourt pas le même nombre de valeurs suivant si le nombre total de mesures est pair ou impair
    max_range = len(total_measure) - 1 if len(total_measure) % 2 == 0 else len(total_measure) - 2
    for i in range(0, max_range, 2):
        tcs_n8.append(total_measure[i]+total_measure[i+1]+5)
            
    #On calcule la moyenne des mesures N8
    avg_tc8 = round(sum(tcs_n8)/len(tcs_n8), 1)
    print(avg_tc8)
