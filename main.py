import os #para usar funcion de limpiar terminal
import time # para introducir un sleep
################# Clases #################
class Stack: # Clase Pila
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
    print("\n==================================================================================")
    print("------------Bienvendio Al Sistema De Despacho Y Almacen De la Empresa -------------")
    print("====================================================================================")
    print("1. [PILA] Apilar caja (push) \n2. [PILA] Retirar caja de la cima (pop) \n3. [COLA] Llega camión a la fila (enqueue) ")
    print("4. [COLA] Despachar primer camión (dequeue)\n5. Ver estado del almacén y camiones\n6. Salir del programa\n")

#funcion para mostrar el estado del almacen (recibe una pila y una cola como parametro )
def mostrar_estado(s: Stack , q: Queue):
    print("\n=====Mostrando Estado Actual=======\n")
    print(f"Almacen de carga: {s}")
    print(f"Bahia de camiones: {q}")

#Esta es la funcion principal donde se desarrollara el codigo
def menu():
    almacen = Stack() #creacion del almacen (pila)
    bahia_camiones = Queue() #creacion del bahia_de_camiones (cola)
    while(True): #bucle principal ejecucion indeterminada hasta que sea detenida por el usuario
        #control_borrado inicializado en true es una variable que permite llevar el control de que mensajes seran eliminados de pantalla para
        #garantizar una visualizacion mas efectiva de los mensajes mostrados en pantalla , los mensajes de las opciones del 1 al 4 seran eliminados 
        #pues una vez ejecutado el proceso su mensaje , ya no tiene mayor relevancia
        control_borrado = True 
        menu_principal() #mostrar el menu principal 
        entrada = input("Por Favor, Ingrese una opcion: ") #capturamos la entrada (se guarda como string)
        if entrada.isdigit(): #se comprueba de que lo capturado sea realmente un digito numerico , esto ya que el menu trabaja con opciones que van
            #en rangos numericos , lo que facilita la verificacion de opciones fuera de 
            opcion = int(entrada)
            match opcion:
                case 1:
                    identificador_alm = input("\nIngrese el identificador de la caja a almacenar: ")

                    if len(identificador_alm) > 20:
                        print("[!] Error: El identificador no puede superar los 20 caracteres.")

                    elif identificador_alm in almacen.stack:
                        print("[!] Error: Ya existe una caja con ese identificador.")

                    else:
                        almacen.push(identificador_alm)
                        print(f"-> Caja [{identificador_alm}] apilada con exito. \n")
                case 2: #caso 2: retirando caja del almacen 
                    print("\n-----Procesando Solicitud------")
                    if almacen.is_empty():
                        print("[!] Error: El almacén está vacío (no hay cajas que retirar.")
                    else:
                        print(f"La caja {almacen.pop()} ha sido retirada con exito.")
                case 3:
                    identificador_cam = input("\nIngrese el identificador del vehiculo que desea enviar a recepcion: ")

                    if len(identificador_cam) > 20:
                        print("[!] Error: El identificador no puede superar los 20 caracteres.")

                elif identificador_cam in bahia_camiones.queue:
                    print("[!] Error: Ya existe un camion con ese identificador.")

                else:
                    bahia_camiones.enqueue(identificador_cam)
                    print(f"-> Camion [{identificador_cam}] formado en la fila. \n")
                case 4:
                    print("\n------Despacho En Proceso-----------")
                    if bahia_camiones.is_empty():
                        print("[!] Error: No hay camiones esperando turno.")
                    else:
                        print(f"Camion {bahia_camiones.dequeue()} despachado con exito. ")
                case 5:
                    mostrar_estado(almacen, bahia_camiones)
                    control_borrado = False   # el mensaje que informa sobre el estado del almacen y bahia permanecera en pantalla hasta la segunda consulta
                case 6:
                    print("!Sistema finalizado, gracias por su tiempo!")
                    break
                case _: print("Ingrese una opcion valida") #default se ingreso un numero fuera de rango   
        else:
            print("Ingrese solo un valor numerico.")
        time.sleep(2) # pausar el programa 1.5 antes de la siguiente iteracion (permite una visualizacion rapida sin sobrecargar la consola)
        if control_borrado: #limpiamos pantalla si no se muestra el estado de los objetos (permite una visualizacion detallada del estado de los objetos)
            os.system('cls ' if os.name=='nt' else 'clear') #uso de la funcion system de os ( si el SO es Windows usa cls sino clear (linux))

if __name__=='__main__': #condicional que llama a la funcion menu como funcion principal
    menu()
