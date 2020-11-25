import sys
import math

def operation_on_cell(cell, dict_cell):
    """Fonction de récurrence permettant de calculer les valeurs d'une case même quand elle a des dépendances"""
    if cell["solved"] == False:
        for arg in ["arg_1", "arg_2"]:
            if "$" in cell["operations"][arg]:
                arg_value = cell["operations"][arg].replace("$", "")
                operation_on_cell(dict_cell[int(arg_value)], dict_cell)
                cell["operations"][arg] = dict_cell[int(arg_value)]["value"]
    
        if cell["operations"]["operation"] == "VALUE":
            cell["value"] = cell["operations"]["arg_1"]
            
        elif cell["operations"]["operation"] == "ADD":
            cell["value"] = int(cell["operations"]["arg_1"]) + int(cell["operations"]["arg_2"])
            
        elif cell["operations"]["operation"] == "SUB":
            cell["value"] = int(cell["operations"]["arg_1"]) - int(cell["operations"]["arg_2"])
        else:
            cell["value"] = int(cell["operations"]["arg_1"]) * int(cell["operations"]["arg_2"])
        
        cell["solved"] = True

n = int(input())
dict_cell = {}

#On instancie notre dictionnaire en récupérant toutes les informations
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    dict_cell[i] = {"value" : None,
                    "operations" : {
                                    "operation" : operation, 
                                    "arg_1" : arg_1, 
                                    "arg_2" : arg_2
                                    },
                    "solved" : False
                    }
    print(dict_cell[i], file=sys.stderr)
    
#On parcourt toutes nos cases
for i in range(n):
    operation_on_cell(dict_cell[i], dict_cell)

    print(dict_cell[i]["value"])