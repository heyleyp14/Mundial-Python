class Grupo:
  def __init__(self,nombre, equipos):
    self.nombre= nombre
    self.equipos= equipos

  def mostrar_info(self):
    info_equipos = ", ".join(equipo.mostrar_info() for equipo in self.equipos)
    return f"Grupo: {self.nombre}, Equipos: {info_equipos}"