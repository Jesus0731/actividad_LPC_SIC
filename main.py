import os #para usar funcion de limpiar terminal
import time # para introducir un sleep
################# Clases #################
     
# Clase Pila
class Stack:
    def __init__(self):
        self.stack= []

    # Verifica si la Pila esta vacia y Retorna un Booleano (True si esta vacia, False caso contrario)
    def is_empty(self):
        return True if len(self.stack) == 0 else False

    # Apilar elementos (Agrega un elemento en la pila)
    def push(self, elem):
        self.stack.append(elem)

    # Desapilar elementos (Elimina un elemento de la pila)
    def pop(self):
        return None if self.is_empty() else self.stack.pop()
    #funcion para devolver la longitud de la pila
    def length(self):
        return len(self.stack)
    #funcion para printear
    def __str__(self):
        return str(self.stack[::-1])

# Clase Cola
class Queue:
    def __init__(self):
        self.queue= []

     # Verifica si la Cola esta vacia y Retorna un Booleano (True si esta vacia, False caso contrario)
    def is_empty(self):
        return True if len(self.queue) == 0 else False

    # Encolar elementos (Agrega un elemento en la cola)
    def enqueue(self, elem):
        self.queue.append(elem)

    # Desncolar elementos (Elimina un elemento de la cola)
    def dequeue(self):
        return None if self.is_empty() else self.queue.pop(0)
    #metodo para devolver el tamano de la cola
    def length(self):
        return len(self.queue)
    #funcion para printear cola
    def __str__(self):
        return str(self.queue)

################# Algorimo a desarrollar abajo #################

##Testeo de funciones
'''print('Testeo cola:')
cola = Queue() # Inicializamos y declaramos la cola
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print('Cola=',cola.queue)
print('Se elimino el elemento', cola.dequeue(),'Cola actal',cola.queue)

print('Testeo pila:')
pila = Stack() # Inicializamos y declaramos la pila
pila.push(1)
pila.push(2)
pila.push(3)

print('Pila=',pila.stack)

print('Se elimino el elemento', pila.pop(),'Pila actal',pila.stack)'''

#funcion para mostrar el menu principal de opciones
def menu_principal():
    print("======================================================")
    print("------------Sistema De Despacho Y Almacen-------------")
    print("======================================================")
    print("1. [PILA] Apilar caja (push) \n2. [PILA] Retirar caja de la cima (pop) \n3. [COLA] Llega camión a la fila (enqueue) ")
    print("4. [COLA] Despachar primer camión (dequeue)\n5. Ver estado del almacén y camiones\n6. Salir del programa")

#Esta es la funcion principal donde se desarrollara el codigo
def menu():
    
    almacen = Stack()
    bahia_camiones = Queue()

    while(True):
        control_borrado = True # varoable para llevar el control de que mensajes se borraran en pantalla las opciones de 1...4 , su mensaje sera borrado despues de 2 seg
        menu_principal()
        entrada = input("Ingrese una opcion: ")
        if entrada.isdigit():
            opcion = int(entrada)
            if 1<= opcion <=6: 
                match opcion:
                    case 1: 
                        print("Ingrese el identificador de la caja: ")
                        identificador_alm = input()
                        almacen.push(identificador_alm)
                        print(f"-> Caja [{identificador_alm}] apilada con exito. ")
                    case 2:
                        print("-----Procesando Solicitud------")
                        if almacen.is_empty():
                            print("[!] Error: El almacén está vacío (no hay cajas que retirar.")
                        else:
                            print(f"La caja {almacen.pop()} ha sido retirada con exito.")
                            print(f"Estado del almacen: {almacen.length()} disponibles.")
                    case 3:
                        print("Ingrese el identificador del vehiculo: ")
                        identificador_cam = input()
                        bahia_camiones.enqueue(identificador_cam)
                        print(f"-> Camion [{identificador_cam}] formado en la fila. ")
                    case 4:
                        print("------Despacho En Proceso")
                        if bahia_camiones.is_empty():
                            print("[!] Error: No hay camiones esperando turno.")
                        else:
                            print(f"Camion {bahia_camiones.dequeue()} despachado con exito. ")
                            print(f"Estado de la fila: {bahia_camiones.length()}")

                    case 5:
                        print("=====Estado Actual=======")
                        print(f"Almacen de carga: {almacen}")
                        print(f"Bahia de camiones: {bahia_camiones}")
                        control_borrado = False   # el mensaje que informa sobre el estado del almacen y bahia permanecera en pantalla hasta la segunda consulta
                    case 6: break
            else:
                print("Ingrese una opcion valida.")
        else:
            print("Ingrese un valor numerico.")
        time.sleep(2)
        if control_borrado:
            os.system('cls ' if os.name=='nt' else 'clear') 

if __name__=='__main__': #condicional que llama a la funcion menu como funcion principal
    menu()