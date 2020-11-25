import sys
import math

class Node:
    def __init__(self, num):
        self.num = num
        self.wall = False
        self.connected_to = list()
        self.status = 0
        self.distance_from_start_point = 0
        self.pere = None
        
    def set_connected_to(self, other_node):
        self.connected_to.append(other_node)
        other_node.connected_to.append(self)
        
    def about_me(self):
        print("Node num : "+str(self.num), file=sys.stderr)
        print("I'm a wall : "+str(self.wall), file=sys.stderr)
        print("Distance from start point : "+str(self.distance_from_start_point), file=sys.stderr)



def parcours_en_largeur(skynet, list_of_nodes):
    """Algorithme de parcours en largeur indiquant les distances de chaque noeud par rapport à la position de l'enfant"""
    queue = [skynet]
    skynet.status = 1
    skynet.distance_from_start_point = 0
    
    while(len(queue) > 0):
        node_to_analyze = queue[0]
        for node in node_to_analyze.connected_to:
            if node.status == 0:
                node.pere = node_to_analyze
                node.distance_from_start_point = queue[0].distance_from_start_point + 1
                node.status = 1
                queue.append(node)
        queue.pop(0)
        node_to_analyze.status = 2



#Instanciation des variables
forest = list()
child_node = tuple()
mom_node = tuple()
list_node = [Node(x) for x in range(100)]

#On récupère les éléments de la forêt
for i in range(10):
    row = input()
    forest.append(row)

    #On parcourt la ligne pour trouver l'enfant, la mère et les murs
    for j, char in enumerate(row):
        if char == "M":
            mom_node = list_node[i*10 + j]

        elif char == "C":
            child_node = list_node[i*10 + j]

        elif char == "#":
            list_node[i*10+j].wall = True


#On parcourt la liste de noeuds pour établir les connexions entre les noeuds
for num, node in enumerate(list_node):

    #Si on est pas sur un mur, on connecte le noeud aux autres noeuds
    if not list_node[num].wall:

        #Si il est pas sur la colonne tout à gauche, on le lie au node à gauche
        if num % 10 != 0 and not list_node[num-1].wall:
            list_node[num].set_connected_to(list_node[num-1])

        #Si il est pas sur la colonne tout à droite, on le lie au node à droite
        if num % 9 != 0 and not list_node[num+1].wall:
            list_node[num].set_connected_to(list_node[num+1])

        #Si il est pas sur la première ligne, on le lie au node au-dessus
        if num > 9 and not list_node[num-10].wall:
            list_node[num].set_connected_to(list_node[num-10])

        #Si il est pas sur la dernière ligne, on le lie au node en-dessous
        if num < 90 and not list_node[num+10].wall:
            list_node[num].set_connected_to(list_node[num+10])
    
parcours_en_largeur(mom_node, list_node)

#Affiche du résultat en km
print(str(child_node.distance_from_start_point * 10)+"km")
