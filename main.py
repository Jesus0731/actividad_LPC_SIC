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

# Clase Color para imprimir mensajes con colores
class Color:
    rojo = '\033[31m'
    verde = '\033[32m'
    negrita = '\033[1m' # Resaltador
    fin = '\033[0m'     # Debe colorcarse al final del texto que se quiere colorear
    cyan_brillante = '\033[1;36m'

################# Algorimo a desarrollar abajo #################

# Conjuntos para controlar la cantidad de ids en el programa
id_almacen= set()   #IDs en la Pila
id_camiones= set()  #IDs en la Cola

#funcion para mostrar el menu principal de opciones
def menu_principal():
    print(f"\n{Color.cyan_brillante}==================================================================================")
    print(f"------------{Color.fin}Bienvendio Al Sistema De Despacho Y Almacen De la Empresa {Color.cyan_brillante}-------------")
    print(f"===================================================================================={Color.fin}")
    print("1. [PILA] Apilar caja  \n2. [PILA] Retirar caja de la cima  \n3. [COLA] Llega camión a la fila  ")
    print("4. [COLA] Despachar primer camión \n5. Ver estado del almacén y camiones\n6. Salir del programa\n")

#funcion para mostrar el estado del almacen (recibe una pila y una cola como parametro )
def mostrar_estado(s: Stack , q: Queue):
    print(f"\n{Color.cyan_brillante}====={Color.fin}Mostrando Estado Actual{Color.cyan_brillante}======={Color.fin}")
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
                case 1:  # caso 1: almacenar una caja
                    identificador_alm = input("\nIngrese el identificador de la caja a almacenar: ")
                    if identificador_alm in id_almacen:
                        print(f"{Color.rojo}[!] Error{Color.fin}: Una caja con esa ID ya existe. Ingrese una ID Valida\n")

                    else:
                        id_almacen.add(identificador_alm)
                        almacen.push(identificador_alm)
                        print(f"{Color.verde}-> Caja [{identificador_alm}] apilada con exito.\n{Color.fin}")

                case 2: #caso 2: retirando caja del almacen 
                    print(f"\n{Color.cyan_brillante}-----{Color.fin}Procesando Solicitud{Color.cyan_brillante}------{Color.fin}")
                    if almacen.is_empty():
                        print(f"{Color.rojo}[!] Error{Color.fin}: El almacén está vacío (no hay cajas que retirar).")

                    else:
                        victima= almacen.pop()      # elemento eliminado de la pila y su conjunto
                        id_almacen.discard(victima)
                        print(f"{Color.verde}La caja {victima} ha sido retirada con exito.{Color.fin}")

                case 3:
                    identificador_cam = input("\nIngrese el identificador del vehiculo que desea enviar a recepcion: ")
                    if identificador_cam in id_camiones:
                        print(f"{Color.rojo}[!] Error{Color.fin}: Una Camion con esa ID ya existe. Ingrese una ID Valida\n")
                    else:
                        id_camiones.add(identificador_cam)
                        bahia_camiones.enqueue(identificador_cam)
                        print(f"{Color.verde}-> Camion [{identificador_cam}] formado en la fila. {Color.fin}\n")

                case 4:
                    print(f"\n{Color.cyan_brillante}------{Color.fin}Despacho En Proceso{Color.cyan_brillante}-----------{Color.fin}")
                    if bahia_camiones.is_empty():
                        print(f"{Color.rojo}[!] Error{Color.fin}: No hay camiones esperando turno.")

                    else:
                        victima=bahia_camiones.dequeue()    # elemento eliminado de la cola y su conjunto
                        id_camiones.discard(victima)
                        print(f"{Color.verde}Camion {victima} despachado con exito. {Color.fin}")

                case 5:
                    mostrar_estado(almacen, bahia_camiones)
                    control_borrado = False   # el mensaje que informa sobre el estado del almacen y bahia permanecera en pantalla hasta la segunda consulta
                
                case 6:
                    print("!Sistema finalizado, gracias por su tiempo!")
                    break
                case _: print(f"{Color.rojo}Ingrese una opcion valida{Color.fin}") #default se ingreso un numero fuera de rango   
        else:
            print(f"{Color.rojo}Ingrese solo un valor numerico.{Color.fin}")
        time.sleep(2) # pausar el programa antes de la siguiente iteracion (permite una visualizacion rapida sin sobrecargar la consola)
        if control_borrado: #limpiamos pantalla si no se muestra el estado de los objetos (permite una visualizacion detallada del estado de los objetos)
            os.system('cls ' if os.name=='nt' else 'clear') #uso de la funcion system de os ( si el SO es Windows usa cls sino clear (linux))

if __name__=='__main__': #condicional que llama a la funcion menu como funcion principal
    menu()