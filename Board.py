# from Player import Player


class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        # creo una lista con 10 valores para facilitar
        self.jugadas = ["*",
                        " ", " ", " ",
                        " ", " ", " ",
                        " ", " ", " "
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

        for victoryLine in victoryLines:
            suma = 0
            for tupla in victoryLine:
                casilla = self.jugadas[tupla]
                if casilla == "X":
                    suma += 1
                elif casilla == "O":
                    suma -= 1
                if suma == 3 or suma == -3:
                    return True
        return False
    
    def cellEmpty(self, jugada):
        if self.jugadas[jugada] == " ":
            return True
        print("\tLa casilla está ocupada.")
        return False
