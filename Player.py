class Player:
    def __init__(self, mark):
        self.mark = mark

    def elige(self, jugadasLibres):

        jugada = input(f" jugador {self.mark} elige pos: ")


        print(f"  { self.mark } { jugadasLibres }")