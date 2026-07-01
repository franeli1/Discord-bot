import random 
class partida_Bingo:
    def __init__(self):
        self.activa = False
        self.jugadores = []
        self.bombo = []
        self.numeros_salidos = []

    def CrearBingo(self):
        self.bombo = list(range(1, 91))
        random.shuffle(self.bombo)
        self.numeros_salidos.clear()
        self.activa = True

    def TerminarBingo(self):
        self.bombo.clear()
        self.jugadores.clear()
        self.numeros_salidos.clear()
        self.activa = False

    def comprobarBingo(self):
        if len(self.bombo) == 0 and self.activa:
            return False
        else: 
            return True
        
    def jugadores(self):
        return self.jugadores

class jugador:
    def __init__(self, jugador):
        if not self.carton:
            self.id = jugador.id
            self.nombre = jugador.name
            self.carton = pedirCarta()
            self.linea = False
            self.Bingo = False

def pedirCarta():
    cartaJugador = random.sample(list(range(90), 25))
    return cartaJugador





