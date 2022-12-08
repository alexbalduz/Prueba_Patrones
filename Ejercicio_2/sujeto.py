from abc import ABC, abstractmethod

class Sujeto(ABC):
    @abstractmethod
    def suscribir(self, observador):
        pass
    @abstractmethod
    def desuscribir(self, observador):
        pass
    @abstractmethod
    def notificar(self):
        pass

class SujetoConcreto(Sujeto):
    def __init__(self):
        self.observadores = []
        self.estado = None

    def suscribir(self, observador):
        self.observadores.append(observador)

    def desuscribir(self, observador):
        self.observadores.remove(observador)

    def notificar(self):
        for observador in self.observadores:
            observador.actualizar(self)