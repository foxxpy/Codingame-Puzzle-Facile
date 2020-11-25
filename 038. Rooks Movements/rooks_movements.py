import sys
import math



def search_every_move(pieces, rook_position):
    list_possible_move = list()
    
    index_column_rook = "abcdefgh".index(rook_position[0])
    index_line_rook = "12345678".index(rook_position[1])

    #On cherche à gauche et à droite de la tour
    if index_column_rook > 0:
        list_possible_move = searching_possible_move(pieces, rook_position, "abcdefgh"[index_column_rook-1::-1], list_possible_move, True)
    if index_column_rook < 8:
        list_possible_move = searching_possible_move(pieces, rook_position, "abcdefgh"[index_column_rook+1::], list_possible_move, True)
    
    #On cherche au-dessus et en-dessous de la tour
    if index_line_rook > 0:
        list_possible_move = searching_possible_move(pieces, rook_position, "12345678"[index_line_rook-1::-1], list_possible_move, False)
    if index_line_rook < 8:
        list_possible_move = searching_possible_move(pieces, rook_position, "12345678"[index_line_rook+1::], list_possible_move, False)
    
    return list_possible_move



def searching_possible_move(pieces, rook_position, search_line, list_possible_move, line):

    for axis in search_line:
        position = axis+rook_position[line] if line else rook_position[line]+axis
        if position in pieces.keys():
            if pieces[position] == 1:
                list_possible_move.append("R"+rook_position+"x"+position)
            return list_possible_move
        list_possible_move.append("R"+rook_position+"-"+position)
    return list_possible_move
        
#Instanciation des variables
rook_position = input()
nb_pieces = int(input())
pieces = dict()

#On récupère la position des pièces
for i in range(nb_pieces):
    colour, one_piece = input().split()
    colour = int(colour)
    pieces[one_piece] = colour

list_possible_move = search_every_move(pieces, rook_position)

#On affiche le résultat
for move in sorted(list_possible_move):
    print(move)