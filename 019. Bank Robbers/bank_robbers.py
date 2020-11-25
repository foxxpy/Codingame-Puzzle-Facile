import sys
import math

class Robber:
    def __init__(self, id_robber, vault=None):
        self.id_robber = id_robber
        self.vault = vault
        self.num_combination_left_to_try = int()
    
    def set_vault(self, vault):
        self.vault = vault
        self.num_combination_left_to_try = vault.num_combination

        
class Vault:
    def __init__(self, id_vault, c, n):
        self.id_vault = id_vault
        self.c = c
        self.n = n
        self.num_combination = self.set_num_combination()
        
    def set_num_combination(self):
        return 10**self.n * 5**(self.c-self.n)

#Instanciation des variables
r = int(input())
v = int(input())
list_robber = list()
list_vault = list()
heist_is_over = False
total_time_heist = 0
number_of_vault_being_robbed = 0

#Instanciation des coffres
for i in range(v):
    c, n = [int(j) for j in input().split()]
    list_vault.append(Vault(i, c, n))
    
#Instanciation des voleurs
for i in range(r):
    list_robber.append(Robber(i))
    if i < v:
        list_robber[i].set_vault(list_vault[i])
        number_of_vault_being_robbed += 1

#On retire les coffres en train d'être vidés de la liste des coffres       
for i in range(number_of_vault_being_robbed):
    list_vault.pop(0)

while(not heist_is_over):
    #On trouve le voleur qui finit en premier, et on l'affecte à un autre coffre si il en reste
    first_robber = min(list_robber, key=lambda x: x.num_combination_left_to_try)
    num_combination_tried = first_robber.num_combination_left_to_try
    total_time_heist += first_robber.num_combination_left_to_try

    #Si on trouve un seul voleur pour lequel il reste des combinaisons à essayer, le casse n'est pas fini
    heist_is_over = True
    for robber in list_robber:
        robber.num_combination_left_to_try -= num_combination_tried
        if robber.num_combination_left_to_try > 0:
            heist_is_over = False
    
    #Si il reste des coffres à braquer
    if len(list_vault) > 0:
        first_robber.set_vault(list_vault[0])
        list_vault.remove(first_robber.vault)
        
    #Sinon on retire le voleur de la liste des voleurs
    else:
        list_robber.remove(first_robber)
        


print(total_time_heist)

#On trouve le voleur qui finit en premier, et on l'affecte à un autre coffre si il en reste

#Si on trouve un seul voleur pour lequel il reste des combinaisons à essayer, le casse n'est pas fini

#Si il reste des coffres à braquer

#Sinon on retire le voleur de la liste des voleurs
