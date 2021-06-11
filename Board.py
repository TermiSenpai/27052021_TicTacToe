# from Player import Player


class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        # creo una lista con 10 valores para facilitar
        self.jugadas = ["*",
                        "*", "*", "*",
                        "*", "*", "*",
                        "*", "*", "*"
                        ]

    def dibuja(self):
        # Dibujando y formateando la tabla del juego
        print(f"""
    
               |          |             
               |          |             
         {self.jugadas[7]}     |     {self.jugadas[8]}    |      {self.jugadas[9]}      
               |          |             
    -----------+----------+-------------
               |          |             
         {self.jugadas[4]}     |     {self.jugadas[5]}    |      {self.jugadas[6]}      
               |          |             
    -----------+----------+-------------
               |          |             
         {self.jugadas[1]}     |     {self.jugadas[2]}    |      {self.jugadas[3]}      
               |          |             
    
""")

    def jugadasLibres(self):
        # https://blog.teamtreehouse.com/python-single-line-loops
        # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
        return [j for i in self.tablero.jugadas for j in i]

    def boardUpdate(self, jugada, turn, mark):

        playerMark = None
        if turn % 2:
            playerMark = mark[1]
        else:
            playerMark = mark[0]

        self.jugadas[jugada] = playerMark

    def playerWin(self):
        winCheck = ""
        victoryLines = [
            (7, 8, 9),
            (4, 5, 6),
            (1, 2, 3),
            (7, 4, 1),
            (8, 5, 2),
            (9, 6, 3),
            (7, 5, 3),
            (1, 5, 9),
        ]


        # ------------- TEMPORAL WIN CHECK ---------------- #
        # Horizontal
        case1 = self.jugadas[7] + self.jugadas[8] + self.jugadas[9]
        case2 = self.jugadas[4] + self.jugadas[5] + self.jugadas[6]
        case3 = self.jugadas[1] + self.jugadas[2] + self.jugadas[3]
        # Vertical
        case4 = self.jugadas[7] + self.jugadas[4] + self.jugadas[1]
        case5 = self.jugadas[8] + self.jugadas[5] + self.jugadas[2]
        case6 = self.jugadas[9] + self.jugadas[6] + self.jugadas[3]
        # Diagonal
        case7 = self.jugadas[7] + self.jugadas[5] + self.jugadas[3]
        case8 = self.jugadas[1] + self.jugadas[5] + self.jugadas[9]
        # Horizontal
        if case1 == "XXX" or case1 == "OOO":
            return True
        elif case2 == "XXX" or case2 == "OOO":
            return True
        elif case3 == "XXX" or case3 == "OOO":
            return True
        # Vertical
        elif case4 == "XXX" or case4 == "OOO":
            return True
        elif case5 == "XXX" or case5 == "OOO":
            return True
        elif case6 == "XXX" or case6 == "OOO":
            return True
        # Diagonal
        elif case7 == "XXX" or case7 == "OOO":
            return True
        elif case8 == "XXX" or case8 == "OOO":
            return True

        return False

    def cellEmpty(self, jugada):
        if self.jugadas[jugada] == "*":
            return True
        print("\tLa casilla está ocupada.")
        return False
