import sys
import math

def sum_pow(nb, power):
    """Renvoie la somme des puissances d'un nombre"""
    total = 0
    for i in range(power+1):
        total += nb**i
    return total

#Instanciation des variables
n = int(input())

    
def ternary(n):
    results = str()
    if n == 0:
        results = "0"
    
    else:
        i = 0
        #We are looking for the range of sum of power of 3 where the number n is
        while (not sum_pow(3, i) <= abs(n) < sum_pow(3, i+1)):
            i = i + 1
            
        index_n = abs(n) - sum_pow(3, i)
    
        for j in range(0, i+1):
            
            if ( (index_n % 3**(j+1)) / (3 ** (j+1)) == 0 or \
            (index_n % 3**(j+1)) / (3 ** (j+1)) > (2/3) ):
                if n < 0:
                    results = "T"+results[:]
                else:
                    results = "1"+results[:]
            
            elif ( (index_n % 3**(j+1)) / (3 ** (j+1)) <= (1/3)):
                if n < 0:
                    results = "1" + results[:]
                else:
                    results = "T" + results[:]
            
            else:
                results = "0" + results[:]
            
        if n > 0 and index_n % 3**(i+1) != 0:
            results = "1" + results[:]
        elif n < 0 and index_n % 3**(i+1) != 0:
            results = "T" + results[:]
            
    return results

#Print result
print(ternary(n))