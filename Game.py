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
            cell = False
            jugada = 0
            # Ajustando el turno del jugador
            player = self.player[self.turno % 2]
            # Tomo los valores de la tabla
            jugadasLibres = [self.board.jugadas]
            while cell != True:
                jugada = player.elige()
                cell = self.board.cellEmpty(jugada)
            
            # actualizo los datos de la tabla del juego
            self.board.boardUpdate(jugada, self.turno, self.MARK)
            # Limpio la pantalla para más comodidad
            self.clearScreen()
            # Actualizo la tabla dibujandola de nuevo
            self.board.dibuja()
            victory = self.board.playerWin()
            # Compruebo si el jugador con el turno actual, ha ganado con el último movimiento
            if victory == True:
                print(f"El jugador {self.MARK[self.turno % 2]} es el ganador!")
                break

            self.turno += 1
        print("El juego ha finalizado.")
