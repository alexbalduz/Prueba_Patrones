from Ejercicio_2.sujeto import SujetoConcreto
from Ejercicio_2.observador import Elemento

def main():
    # Creamos una instancia de la clase Sujeto, que representa al sistema
    # de alarma
    sistema = SujetoConcreto()

    # Creamos dos elementos del sistema, con diferentes umbrales y medidas
    elemento1 = Elemento(conectado=True, medida=10, umbral=11)
    elemento2 = Elemento(conectado=True, medida=20, umbral=15)

    # Suscribimos los elementos al sistema de alarma
    sistema.suscribir(elemento1)
    sistema.suscribir(elemento2)

    # Cambiamos el estado del sistema a "cambio_estado"
    sistema.estado = "cambio_estado"

    # Notificamos a los elementos para que se actualicen
    sistema.notificar()

if __name__ == "__main__":
    main()