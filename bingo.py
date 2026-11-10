import random 

class partida_Bingo:
    def __init__(self):
        self.activa = False
        self.jugadores = {}
        self.bombo = []
        self.numeros_salidos = []
        self.linea_cantada = False

    def CrearBingo(self):
        self.bombo = list(range(1, 91))
        random.shuffle(self.bombo)
        self.numeros_salidos.clear()
        self.jugadores.clear()
        self.linea_cantada = False
        self.activa = True

    def TerminarBingo(self):
        self.bombo.clear()
        self.jugadores.clear()
        self.numeros_salidos.clear()
        self.linea_cantada = False
        self.activa = False

    def comprobarBingo(self):
        return self.activa and len(self.bombo) > 0
        
    def obtener_jugadores(self):
        return list(self.jugadores.values())

    def unirse(self, usuario):
        if usuario.id in self.jugadores:
            return None
        nuevo = jugador(usuario)
        self.jugadores[usuario.id] = nuevo
        return nuevo
    
    def sacar_Bola(self):
        if not self.bombo:
            return None
        valor = self.bombo.pop(0)
        self.numeros_salidos.append(valor)
        
        return valor

class jugador:
    def __init__(self, jugador):
        self.id = jugador.id
        self.nombre = jugador.name
        numeros = random.sample(range(1,91), 15)
        self.carton = [sorted(numeros[i:i + 5]) for i in range(0, 15, 5)]
 
    def pedirCarta(self, salidos=()):
        filas = []
        for fila in self.carton:
            celdas = [f"{n:2d}*" if n in salidos else f"{n:2d} " for n in fila]
            filas.append(" | ".join(celdas))
        return "```\n" + "\n".join(filas) + "\n```"
 
    def tiene_linea(self, salidos):
        return any(all(n in salidos for n in fila) for fila in self.carton)
 
    def tiene_bingo(self, salidos):
        return all(n in salidos for fila in self.carton for n in fila)





