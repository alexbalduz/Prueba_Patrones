from Ejercicio_1.base import Base
from Ejercicio_1.base_compuesta import BaseCompuesta
from Ejercicio_1.base_simple import BaseSimple
from Ejercicio_2.sujeto import SujetoConcreto
from Ejercicio_2.observador import Elemento
import helpers

def menu():
    print("========================")
    print(" BIENVENIDO A PRUEBA_PATRONES ")
    print("========================")
    print("[1] Ejercicio 1  ")
    print("[2] Ejercicio 2 ")
    print("[3] Salir ")
    print("========================")

def lanzar():

    # Creamos una instancia de la clase Sujeto, que representa al sistema
    # de alarma
    sistema = SujetoConcreto()

    # Creamos dos elementos del sistema, con diferentes umbrales y medidas
    elemento1 = Elemento(conectado=True, medida=10, umbral=11)
    elemento2 = Elemento(conectado=True, medida=20, umbral=15)

    base_1 = BaseSimple("Base 1", 5, 10)
    base_2 = BaseSimple("Base 2", 10, 15)
    base_3 = BaseCompuesta("Base 3", [base_1, base_2])


    while True:
        menu()
        opcion=int(input("> "))
        helpers.limpiar_pantalla()
        if opcion == 1:
            print(base_1.cantidad_ambulancias())
            print(base_1.tiempo_respuesta_media())
            print(base_2.cantidad_ambulancias())
            print(base_2.tiempo_respuesta_media())
            print(base_3.cantidad_ambulancias())
            print(base_3.tiempo_respuesta_media())

        if opcion == 2:
            # Suscribimos los elementos al sistema de alarma
            sistema.suscribir(elemento1)
            sistema.suscribir(elemento2)

            # Cambiamos el estado del sistema a "cambio_estado"
            sistema.estado = "cambio_estado"

            # Notificamos a los elementos para que se actualicen
            sistema.notificar()

        if opcion == 3:
            print("Saliendo...\n")
            break
