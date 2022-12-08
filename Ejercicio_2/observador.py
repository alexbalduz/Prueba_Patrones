from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, sujeto):
        pass

class Elemento(Observador):
    def __init__(self, conectado, medida, umbral):
        self.conectado = conectado
        self.medida = medida
        self.umbral = umbral

    def supera_umbral(self):
        return self.medida > self.umbral

    def actualizar(self, sujeto):
        if sujeto.estado == "cambio_estado":
            if self.conectado and self.supera_umbral():
                print("Alarma disparada!")