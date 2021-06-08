from Board import Board
from Player import Player

import os
import platform


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

    def clearScreen(self):
        if platform.system() == 'Windows':
            os.system("cls")
        elif platform.system() == 'Linux':
            os.system("clear")

    def juega(self):
        self.clearScreen()
        self.board.dibuja()
        while self.turno < self.MAXPLAYS:
            player = self.player[self.turno % 2]
            self.turno += 1

            jugadasLibres = []
            for fila in self.board.jugadas:
                jugadasLibres += fila

            jugada = player.elige(jugadasLibres)
            self.clearScreen()
            print(self.turno)
            self.board.boardUpdate(jugada, self.turno, self.MARK)
            self.board.dibuja()
        print("El juego ha finalizado.")
