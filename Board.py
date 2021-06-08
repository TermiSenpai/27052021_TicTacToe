from Player import Player


class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.jugadas = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def dibuja(self):
        print(f"""
    |------------------------------------|
    |           |          |             |
    |     {self.jugadas[2][0]}     |     {self.jugadas[2][1]}    |      {self.jugadas[2][2]}      |
    |           |          |             |
    |-----------+----------+-------------|
    |           |          |             |
    |     {self.jugadas[1][0]}     |     {self.jugadas[1][1]}    |      {self.jugadas[1][2]}      |
    |           |          |             |
    |-----------+----------+-------------|
    |           |          |             |
    |     {self.jugadas[0][0]}     |     {self.jugadas[0][1]}    |      {self.jugadas[0][2]}      |
    |           |          |             |
    |------------------------------------|
""")

    def jugadasLibres(self):
        # https://blog.teamtreehouse.com/python-single-line-loops
        # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
        return [j for i in self.tablero.jugadas for j in i]

    def boardUpdate(self, jugada, turn, mark):
        playerMark = None
        if turn % 2:
            playerMark = mark[0]
        else:
            playerMark = mark[1]
        
        if jugada <= 3 and jugada >= 1:
            self.jugadas[0][jugada-1] = playerMark
        if jugada > 3 and jugada <= 6:
            self.jugadas[1][jugada - 4] = playerMark
        if jugada > 6 and jugada <= 9:
            self.jugadas[2][jugada - 7] = playerMark
            
    def Victory(self):
        posibleWins = []

