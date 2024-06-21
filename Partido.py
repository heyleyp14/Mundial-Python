import random

class Partido:
  def __init__(self,equipo_local, equipo_visitante, resultado= None):
    self.equipo_local= equipo_local
    self.equipo_visitante= equipo_visitante
    self.equipo_visitante= equipo_visitante

  def jugar_partido(self):
    puntuacion_local = random.randint(0, 5)
    puntuacion_visitante = random.randint(0, 5)

    if puntuacion_local > puntuacion_visitante:
        self.resultado = f"Gana {self.equipo_local.nombre}"
    elif puntuacion_local < puntuacion_visitante:
        self.resultado = f"Gana {self.equipo_visitante.nombre}"
    else:
        self.resultado = "Empate"

  def mostrar_resultado(self):
    if self.resultado is not None:
        return f"Resultado: {self.resultado}, Equipo Local: {self.equipo_local.nombre}, Equipo Visitante: {self.equipo_visitante.nombre}"
    else:
        return "El partido aún no se ha jugado"