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

#Esta es la funcion principal donde se desarrollara el codigo
def menu():
    
    print('Hola mundo')
    
    while(True):
        break

if __name__=='__main__': #condicional que llama a la funcion menu como funcion principal
    menu()