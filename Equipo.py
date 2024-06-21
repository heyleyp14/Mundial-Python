class Equipo:
  def __init__(self,nombre, entrenador, jugadores):
    self.nombre= nombre
    self.entrenador= entrenador
    self.jugadores= jugadores

  def agregar_jugador(self, jugador):
    self.jugadores.append(jugador)

  def mostrar_info(self):
    info_jugadores = ", ".join(jugador.mostrar_info() for jugador in self.jugadores)
    return f"Equipo: {self.nombre}, Entrenador: {self.entrenador}, Jugadores: {info_jugadores}"

