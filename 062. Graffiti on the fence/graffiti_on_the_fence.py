import sys
import math

#Instanciation des variables
l = int(input())
n = int(input())
painted_sections_temp = list()
painted_sections = list()
unpainted_sections = list()

#On ajoute les sections peintes à notre liste de sections peintes
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    painted_sections_temp.append({"st" : st, "ed" : ed})

painted_sections_temp = sorted(painted_sections_temp, key = lambda x : x["st"])

#On fusionne les sections peintes qui se chevauchent
for i, section in enumerate(painted_sections_temp, 0):
    if i == 0 or i > 0 and section["st"] > painted_sections[-1]["ed"]:
        painted_sections.append(section)
    elif i>0 and section["st"] <= painted_sections[-1]["ed"] and section["ed"] > painted_sections[-1]["ed"]:
        painted_sections[-1]["ed"] = section["ed"]

#SI tout a été peint, on affiche "All painted"
if len(painted_sections) == 1 and painted_sections[0]["st"] == 0 and painted_sections[-1]["ed"] == l:
    print("All painted")
   
#Si tout n'a pas été peint, on regarde quelles portions non peintes à afficher
else:

    i = 0
    while(i < l):
        #Si il reste des sections peintes à consulter et que i est inférieur ou égal au début de la section peinte suivant
        if len(painted_sections) > 0 and i <= painted_sections[0]["st"]:
            if i < painted_sections[0]["st"]:
                print(str(i)+" "+str(painted_sections[0]["st"]))
            i = painted_sections[0]["ed"]
            painted_sections = painted_sections[1:]
           
        #Si on arrive à la fin des sections peintes et que i est inférieur à la longueur de la clôture
        elif len(painted_sections) == 0 and i < l:
            print(str(i)+" "+str(l))
            break
       
        else:
            break

