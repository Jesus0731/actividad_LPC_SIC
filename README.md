"# Proyecto SIC " 
# Integrantes: 
- Greilys Hernández
- Jesús Herrada
- Jorge Naranjo
- Samuel Reyna

#El siguiente proyecto se basa en la gestión de turnos de atención a camiones, desarrollado para optimizar la gestión de cajas y camiones en un centro de distribución. Se encarga de registrar nuevas cajas en el almacén, registrar cajas, registrar la llegada de los camiones, despachar camiones respetando el orden de llegada y consultar el estado actual de las operaciones que modela el comportamiento de dos estructuras de datos mediante la abstracción de clases (Stack y Queue)

# Sistema de Despacho y Almacén (Simulador CLI)
Sistema interactivo de terminal desarrollado en Python que simula la operativa de un centro logístico mediante la implementación orientada a objetos de dos estructuras de datos fundamentales: *Pila (LIFO)* y *Cola (FIFO)*.

# 📌 Arquitectura y Lógica del Sistema
El programa modela de forma independiente dos flujos de trabajo logísticos:

1. Almacén de Cajas (`Stack` / Pila - LIFO):
   - **Principio:** *Last In, First Out* (El último en entrar es el primero en salir).
   - Las cajas se apilan verticalmente. Solo se puede colocar en la cima (`push`) o retirar la última agregada (`pop`).
   - Al imprimirse (`__str__`), la lista interna se invierte (`[::-1]`) para mostrar visualmente primero el elemento en la cima (el más reciente).

2. **Bahía de Camiones (`Queue` / Cola - FIFO):**
   - **Principio:** *First In, First Out* (El primero en entrar es el primero en salir).
   - Los vehículos hacen fila india. Llegan al final (`enqueue` vía `append`) y se despachan por el frente (`dequeue` vía `pop(0)`).

## ⚙️ Características Técnicas

- **Encapsulación POO:** Clases `Stack` y `Queue` con métodos dedicados (`is_empty`, `push`/`enqueue`, `pop`/`dequeue`, `length`, `__str__`).
- **Control de excepciones y robustez:**
  - Validación numérica con `entrada.isdigit()` para evitar cierres abruptos por texto o caracteres inválidos.
  - Comprobación preventiva de subdesbordamiento (*underflow*) mediante `is_empty()` antes de desapilar o desencolar.
  - Manejo de flujo con sentencia `match/case` y descarte de opciones fuera de rango en el bloque `case _`.
- **Experiencia de usuario en terminal:**
  - Limpieza dinámica de consola multiplataforma (`cls` en Windows, `clear` en Unix/Linux).
  - Variable bandera `control_borrado`: conserva la visualización de la Opción 5 en pantalla para que el usuario pueda consultar el inventario sin que se borre inmediatamente.

## 🚀 Requisitos y Ejecución

- **Requisitos:** Python 3.10 o superior (debido a la sintaxis estructural `match/case`).
- **Dependencias externas:** Ninguna (emplea únicamente módulos nativos `os` y `time`).

### Ejecución:

```bash
python main.py
```

## 📋 Mapeo de Opciones del Menú

```text
==================================================================================
------------Bienvenido Al Sistema De Despacho Y Almacen De la Empresa -------------
==================================================================================
1. [PILA] Apilar caja (push) 
2. [PILA] Retirar caja de la cima (pop) 
3. [COLA] Llega camión a la fila (enqueue) 
4. [COLA] Despachar primer camión (dequeue)
5. Ver estado del almacén y camiones
6. Salir del programa
```

| Opción | Acción | Método Interno | Comportamiento |
| :---: | :--- | :--- | :--- |
| **1** | Apilar caja | `almacen.push(id)` | Agrega el identificador a la cima de la pila. |
| **2** | Retirar caja | `almacen.pop()` | Extrae la última caja ingresada. Notifica si la pila está vacía. |
| **3** | Llegada de camión | `bahia_camiones.enqueue(id)` | Forma el vehículo al final de la cola. |
| **4** | Despachar camión | `bahia_camiones.dequeue()` | Retira y atiende al primer vehículo en espera. Notifica si la cola está vacía. |
| **5** | Ver estado | `mostrar_estado(s, q)` | Muestra la carga actual del almacén y la fila de camiones; congela la limpieza de pantalla. |
| **6** | Salir | `break` | Detiene el bucle `while(True)` y finaliza la sesión limpiamente. |

## Guía de Uso Paso a Paso 
No necesitas saber programar para usar este sistema. Solo sigue estas indicaciones:

# Paso 1: Abrir y ejecutar el programa y asegúrate de tener instalado Python en tu computadora.

## Paso 2: Conociendo el Menú de Opciones

Cada vez que el programa esté listo, te mostrará esta lista numerada del **1 al 6**:

```text
==================================================================================
------------Bienvenido Al Sistema De Despacho Y Almacen De la Empresa -------------
==================================================================================
1. [PILA] Apilar caja (push) 
2. [PILA] Retirar caja de la cima (pop) 
3. [COLA] Llega camión a la fila (enqueue) 
4. [COLA] Despachar primer camión (dequeue)
5. Ver estado del almacén y camiones
6. Salir del programa
```
Para elegir qué hacer, escribe únicamente el número de la opción que necesitas (del 1 al 6) y presiona la tecla `Enter`.

# Paso 3: ¿Qué hace cada opción?

# 📦 Opción 1: Guardar una caja en el almacén
* Escribe `1` y presiona `Enter`.
* El programa te pedirá un nombre o código para la caja (por ejemplo: `Caja-101` o `Zapatos`).
* Escribe el nombre y presiona `Enter`. La caja quedará guardada en la cima del almacén.

# 📤 Opción 2: Retirar la última caja guardada
* Escribe `2` y presiona `Enter`.
* El sistema retirará automáticamente la caja que esté arriba del todo y te mostrará su nombre.
* *Nota:* Si el almacén está vacío, el sistema no fallará ni se cerrará; simplemente te avisará que no hay nada que retirar.

# 🚛 Opción 3: Registrar la llegada de un camión
* Escribe `3` y presiona `Enter`.
* Te pedirá un nombre o placa del vehículo (por ejemplo: `Camion-01` o `Placa-XYZ`).
* El vehículo se colocará al final de la fila de espera.

# 🚦 Opción 4: Atender y despachar un camión
* Escribe `4` y presiona `Enter`.
* El sistema despachará al camión que lleve más tiempo esperando (el primero de la fila).
* *Nota:* Si no hay camiones en fila, te informará amablemente en pantalla sin colapsar.

# 👀 Opción 5: Consultar cómo está todo
* Escribe `5` y presiona `Enter`.
* Te mostrará la lista de cajas apiladas (de arriba hacia abajo) y los camiones en fila (del primero al último).
* **Importante:** Esta información se mantendrá visible en pantalla para que la revises con calma hasta tu siguiente consulta.

#### 🚪 Opción 6: Salir
* Escribe `6` y presiona `Enter`.
* El programa mostrará un mensaje de despedida y se cerrará de forma segura.


# ¿Qué pasa si te equivocas al escribir?
El sistema está protegido contra errores comunes:
- **Si escribes letras o palabras en lugar de números** (por ejemplo, escribes `uno` o `hola`): el programa te dirá `Ingrese solo un valor numerico` y volverá a mostrarte el menú.
- **Si escribes un número fuera del rango** (como el `8` o el `99`): te avisará `Ingrese una opcion valida` para que intentes de nuevo.

