class Player:

    def __init__(self, mark):
        self.mark = mark
    
    def casillaVacia(self, jugada, libres):
        pass

    def elige(self,jugadasLibres):
        jugadasValidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        jugada = None

        while jugada not in jugadasValidas:
            try:
                jugada = int(input(f" jugador {self.mark} elige pos: "))
            except ValueError:
                jugada = 0
            except TypeError:
                jugada = 0
                
            if jugada not in jugadasValidas:
                print("No es una jugada válida. ")
            casilla = self.casillaVacia(jugada, jugadasLibres)
            if casilla == False:
                print("Casilla llena")
                jugada = None
            

        # print(f"  { self.mark } { jugadasLibres }")

        return jugada
