# -*- coding: utf-8 -*-

listado=[["123abc","20152020","1900"],["156abc","20152020","1900"],
         ["198abc","20152020","1600"],["014abc","20152020","1800"],
         ["258abc","20152020","1200"],["369abc","20152020","1000"]]
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=listado

    def asignar(self, Usuario):
        self.items.append(Usuario)
    
    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
      
    def consultar(self):
        aux=len(self.items)
        i=0
        while(i<aux):
            print(self.items[i][0]+", "+self.items[i][1]+", "+self.items[i][2])
            i=i+1
            
parqueadero = Cola()
salir = False
a=0

while not salir:
    
    while(a!=1 and a!=2 and not salir):
        print("Bienvenido, que desea hacer?:")
        print("\t1. Agregar nuevo vehiculo.")
        print("\t2. Buscar un vehiculos.")
        print("\t3. Salir")
        a=input("Digite una opcion: ")
    
        if a==1:
            tempUsuario = []
            placa=  (raw_input("\nIngrese una placa:"))
            codigo=(str) (raw_input("Ingrese código:"))
            hora=(str) (raw_input("Ingrese una hora (ejp: 1800):"))
            
            parqueadero.asignar([placa,codigo,hora])
            print("El usuario a sido asignado")
            a=0
        elif(a==2):            
            parqueadero.consultar()
            a=0
        elif(a==3):
            salir=True
