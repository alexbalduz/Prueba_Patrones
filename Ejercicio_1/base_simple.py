from base import Base

class BaseSimple(Base):

    def __init__(self, nombre: str, ambulancias: int, tiempo_respuesta: int):
        self.nombre = nombre
        self.ambulancias = ambulancias
        self.tiempo_respuesta = tiempo_respuesta

    def cantidad_ambulancias(self):
        return self.ambulancias

    def tiempo_respuesta_media(self):
        return self.tiempo_respuesta