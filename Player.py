class Player:

    def __init__(self, mark):
        self.mark = mark
    
    

    def elige(self):
        jugadasValidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        jugada = None

        while jugada not in jugadasValidas:
            try:
                jugada = int(input(f"\t jugador {self.mark} elige pos: "))
            except ValueError:
                print("")
                jugada = 0
            except TypeError:
                jugada = 0
            except:
                jugada = 0
            # comprobamos si el input es válido
            if jugada not in jugadasValidas:
                print("\tNo es una jugada válida. ")
            
        return jugada
