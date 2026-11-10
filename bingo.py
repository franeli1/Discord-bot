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
        self.jugadores.clear()
        self.activa = True

    def TerminarBingo(self):
        self.bombo.clear()
        self.jugadores.clear()
        self.numeros_salidos.clear()
        self.activa = False

    def comprobarBingo(self):
        return self.activa and len(self.bombo) > 0
        
    def obtener_jugadores(self):
        return self.jugadores
    
    def sacar_Bola(self):
        valor = self.bombo.pop(0)
        self.numeros_salidos.append(valor)
        
        return valor

class jugador:
    def __init__(self, jugador):
        self.id = jugador.id
        self.nombre = jugador.name
        self.carton = list(random.sample(range(1, 91), 25))
        self.linea = False
        self.Bingo = False

    def pedirCarta(self):
        return self.carton






