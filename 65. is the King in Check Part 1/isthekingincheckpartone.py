import sys
import math



class Board:

    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        self.liste_pieces = list()



class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y



    def is_valid(self):
        if 0 <= self.x < 8 and 0 <= self.y < 8:
            return True
        else:
            return False



    def __eq__(self, other_position):
        if self.x == other_position.x and self.y == other_position.y:
            return True
        else:
            return False



    def __str__(self):
        return "({},{})".format(self.x, self.y)




class Piece:

    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position
        self.possible_moves = list()
        self.find_possible_moves()

    

    def find_possible_move(self):
        pass



    def rook_range(self, inf, sup, step, horizontal):
        """Permet de calculer les positions possibles de la tour par rapport à ses intervalles de déplacement"""
        for num in range(inf, sup, step):
            pos = Position(num, self.position.y) if horizontal else Position(self.position.x, num)
            if pos.is_valid():
                self.possible_moves.append(pos)



    def knight_range(self, interval_x, interval_y):
        """Permet de calculer les positions possibles du cavalier par rapport à ses intervalles de déplacement"""
        for y in interval_y:
            for x in interval_x:
                pos = Position(self.position.x + x, self.position.y + y)
                if pos.is_valid():
                    self.possible_moves.append(pos)



    def bishop_range(self,x_positive, y_positive):
        """
        Permet de calculer les positions possibles du cavalier par rapport à ses intervalles de déplacement

        x_positive (bool) : indique si on va sur le sens positif en x ou non
        y_positive (bool) : indique si on va sur le sens positif en y ou non
        """

        position_temp = self.position
        first_turn = True
        step_x = 1 if x_positive else -1
        step_y = 1 if y_positive else -1

        while(position_temp.is_valid()):
            if not first_turn:
                self.possible_moves.append(position_temp)

            position_temp = Position(position_temp.x + step_x,  position_temp.y + step_y)
            first_turn = False
            


class Knight(Piece):
    """Le cavalier"""

    def __init__(self, symbol, position):
        Piece.__init__(self, symbol, position)



    def find_possible_moves(self):
        self.knight_range([-1, 1], [-2, 2])
        self.knight_range([-2,2], [-1, 1])

                    

class Rook(Piece):
    """La tour"""

    def __init__(self, symbol, position):
        Piece.__init__(self, symbol, position)


    def find_possible_moves(self):
        #Cherche les cases à droite, à gauche, en bas, en haut
        self.rook_range(self.position.x, 8, 1, True) 
        self.rook_range(self.position.x, -1, -1, True)
        self.rook_range(self.position.y, 8, 1, False)
        self.rook_range(self.position.y, -1, -1, False)



class Bishop(Piece):
    """Le fou"""

    def __init__(self, symbol, position):
        Piece.__init__(self, symbol, position)



    def find_possible_moves(self):

        #Recherche des positions sur les diagonales : bas-droite, bas-gauche, haut-droite, haut-gauche
        self.bishop_range(True, True)
        self.bishop_range(False, True)
        self.bishop_range(True, False)
        self.bishop_range(False, False)



class Queen(Piece):
    """La reine"""

    def __init__(self, symbol, position):
        Piece.__init__(self, symbol, position)



    def find_possible_moves(self):

        #Recherche des positions possibles sur les axes horizontaux ou verticaux
        self.rook_range(self.position.x, 8, 1, True) 
        self.rook_range(self.position.x, -1, -1, True)
        self.rook_range(self.position.y, 8, 1, False)
        self.rook_range(self.position.y, -1, -1, False)

        #Recherche des positions possibles sur les diagonales
        self.bishop_range(True, True)
        self.bishop_range(False, True)
        self.bishop_range(True, False)
        self.bishop_range(False, False)



class King(Piece):
    """Le roi"""
    def __init__(self, symbol, position):
        Piece.__init__(self, symbol, position)

    def find_possible_moves(self):
        pass



#Instanciation des variables
board = Board()
king = None #Piece object
check = False

for y in range(8):
    chess_row = input().split(" ")

    #On récupère les pièces sur l'échiquier
    for x, cell in enumerate(chess_row):
        if cell != "_":
            piece = None
            position = Position(x, y)

            if cell == "K":
                piece = King(cell, position)

            elif cell == "B":
                piece = Bishop(cell, position)

            elif cell == "N":
                piece = Knight(cell, position)

            elif cell == "R":
                piece = Rook(cell, position)

            elif cell == "Q":
                piece = Queen(cell, position)

            #Si ce n'est pas un roi, on l'ajoute à la liste des pions
            if cell != "K":
                board.liste_pieces.append(piece)
            else:
                king = piece


#On cherche si le roi est sur une case attaquable par une pièce sur l'échiquier
for piece in board.liste_pieces:
    #print(piece.position, file=sys.stderr)
    for possible_move in piece.possible_moves:
        if possible_move == king.position:
            check = True
            break


print("Check" if check else "No Check")