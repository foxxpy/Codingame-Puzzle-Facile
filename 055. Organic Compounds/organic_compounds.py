import sys
import math

#Instanciation des variables
n = int(input())
links_needed = 0
total_link = 0

for i in range(n):
    compound = input()
    j = 0
    #On parcourt le composé organique pour déterminer le nombre de liens nécessaires et
    #le nombre de liens véritablement présents
    while(j < len(compound)):
        if compound[j] == "C" and compound[j+1] == "H":
            links_needed += 4 - int(compound[j+2])
            j = j + 3
        elif compound[j] == "(":
            total_link += int(compound[j+1])
            j = j + 3
        else:
            j = j + 1

print("Links needed : "+str(links_needed), file=sys.stderr)
print("total link : "+str(total_link), file=sys.stderr)

if total_link == links_needed / 2:
    print("VALID")
else:
    print("INVALID")