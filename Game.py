from Board import Board
from Player import Player


class Game:

    MAXPLAYS = 9
    MARK = ['X', 'O']

    def __init__(self):
        self.board = Board()
        self.reset()
        self.juega()

    def reset(self):
        self.player = [
            Player(self.MARK[0]),
            Player(self.MARK[1])
        ]
        self.board.reset()
        self.turno = 0

    def juega(self):
        self.board.dibuja()
        while self.turno < self.MAXPLAYS:
            player = self.player[self.turno % 2]
            self.turno += 1

            # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
            # jugadasLibres = [j for i in self.board.jugadas for j in i]

            jugadasLibres = []
            for fila in self.board.jugadas:
                jugadasLibres += fila

            jugada = player.elige(jugadasLibres)

            # self.board.dibuja()