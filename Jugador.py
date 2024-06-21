class Jugador:
  def __init__(self,nombre, edad, posicion):
    self.nombre= nombre
    self.edad= edad
    self.posicion= posicion

  def mostrar_info(self):
    return f"Jugador: {self.nombre}, Edad: {self.edad}, Posición: {self.posicion}"