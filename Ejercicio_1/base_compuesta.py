from base import Base

class BaseCompuesta(Base):

    def __init__(self, nombre: str, bases: list[Base]):
        self.nombre = nombre
        self.bases = bases

    def cantidad_ambulancias(self):
        ambulancias = 0
        for base in self.bases:
            ambulancias += base.cantidad_ambulancias()
            return ambulancias

    def tiempo_respuesta_media(self):
        tiempo_respuesta = 0
        for base in self.bases:
            tiempo_respuesta += base.tiempo_respuesta_media()
            return tiempo_respuesta / len(self.bases)