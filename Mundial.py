from Partido import Partido

class Mundial:
  def __init__(self):
    self.grupos= []
    self.estadios= []

  def registrar_grupo(self, grupo):
    self.grupos.append(grupo)

  def registrar_estadio(self, estadio):
    self.estadios.append(estadio)

  def generar_fixture(self):
    info = ""
    for grupo in self.grupos:
        equipos_grupo = grupo.equipos
        for i in range(len(equipos_grupo)):
            for j in range(i + 1, len(equipos_grupo)):
                partido = Partido(equipos_grupo[i], equipos_grupo[j])
                partido.jugar_partido()
                info += partido.mostrar_resultado() + "\n"
    return info