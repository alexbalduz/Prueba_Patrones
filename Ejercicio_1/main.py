from base import Base
from base_compuesta import BaseCompuesta
from base_simple import BaseSimple

def main():
    base_1 = BaseSimple("Base 1", 5, 10)
    base_2 = BaseSimple("Base 2", 10, 15)
    base_3 = BaseCompuesta("Base 3", [base_1, base_2])
    print(base_1.cantidad_ambulancias())
    print(base_1.tiempo_respuesta_media())
    print(base_2.cantidad_ambulancias())
    print(base_2.tiempo_respuesta_media())
    print(base_3.cantidad_ambulancias())
    print(base_3.tiempo_respuesta_media())

if __name__ == "__main__":
    main()