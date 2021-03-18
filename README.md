# Modificaciónes de los juegos

Creadores
- Ian Seidman Sorsby
- Javier Alejandro Martinez Noe
- Ricardo Uraga de la Fuente

## Explicación del Proyecto

Este proyecto consiste de modificar las reglas y funcionalidades de juegos clásicos implementados en Python. Nosotros no diseñamos las implementaciones de Python, pero si diseñamos e implementamos las siguientes modificaciones:

### Snake

- Añadimos la funcionalidad de colores aleatorios para la serpiente y la comida al correr el juego, siempre son colores distintos y no pueden ser del mismo color la serpiente y la comida (Esto fue a través de una función adicional que regresa un string de un color aleatorio pero toma otro color como parametro para checar que no se repitan)
- Añadimos la funcionalidad de movimiento aleatorio de la comida paso por paso
- Añadimos la funcionalidad para aumentar el tamaño del tablero

Javier Alejandro Martinez Noe:
    Para el juego de Snake dacidi modificar el sigiente aspecto: La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
    para esto tuve que agregar unos condicionales en la funcion del movimiento para que el movimiento de la comida estubiera sincronizado con el de la serpeinte. De igual manera agerege un randomizador a las cordenadas de la comida en "x" y "y", tomando en consideracion que pasaria si llegara al brode se tubiera que retroceder un paso para continuar con el juago. Por ultimo tuve que modificar la forma en la que se median las restricciones para que a la hora que se juntaran las ramas del git no hubiera conflictos.
    
    def inside(head):
      "Return True if head inside boundaries."
      return -limitex / 2 + 10 < head.x < limitex / 2 - 10 and -limitey / 2 + 10 < head.y < limitey / 2 - 10
    def move():
      (...)
      #makes food move randomly without going out of the canvas
      if food.x < limitex / 2 - 10 and food.x > -limitex / 2 + 10:
          print(food.x)
          food.x += round(randrange(-1, 2)) * 10
      else:
          food.x += food.x / food.x * -10
      if food.y < limitey / 2 - 10 and food.y > -limitey / 2 + 10:
          print(food.y)
          food.y += round(randrange(-1, 2)) * 10
      else:
          food.y += food.y / food.y * -10
      (...)
      

### Pacman

- Añadimos la funcionalidad de incremento de velocidad de los fantasmas del juego (Esto fue a través de un cambio en la llamada de la función move, incrementando que tan seguido y rápido se llama esta)
- Añadimos dos fantasmas adicionales
- Añadimos la funcionalidad para que pacman (el jugador) comienze el juego en una parte distinta del tablero.

Javier Alejandro Martinez Noe:
  Para el juego de packman decidi modificar el apardado de "Change the number of ghosts", para esto tuve que analizar el programa, asi percatandome que el programa estaba automatizado para autogenarar los fantasmas y el movimiento individual de cada uno. Por lo cual, lo unico que necesite modificar fue agregar mas fantasmas en el tensor de fantasmas. Para lograr que esto funcionara de forma exitosa esra neccesario tomar en consideracion las cordenadas de origen de los fantasmas, ya que si colisionaban con las paredes (limites del mundo) rompia el juego y los fantasmas eran incapases de moverse.

    ghosts = [
      [vector(-180, 160), vector(5, 0)],
      [vector(-180, -160), vector(0, 5)],
      [vector(100, 160), vector(0, -5)],
      [vector(100, -160), vector(-5, 0)],
      [vector(-50, -80), vector(-5, 0)],
      [vector(50, 80), vector(-5, 0)],
    ]
### Indice pagina equipo 10 
Javier Alejandro Martinez Noe:
    
    Para ligar nuestras paginas web en el servidor de aws era neccesario programar un indice el cual ligara las paginas de todos los miebros del equipo, para esto estableci una estructura sencilla utilizando div's para seccionar cada apartado del individuo y anchor tag's para ligar los sitios de los usuaios, al ligar los sitios fue imperativo utilizar el directorio raiz del equipo10 mediante ~team10/[rute], esto fue muy importante ya que el servidor contaba con multiples usuarios. por otro lado para agregar el estilo utilice el nuevo modulo de css3 FlexBox el cual me permitio darle este estilo. Por ultimo nos cordianamos en las codificaciones de las ligas mediante el gestor de versiones git. Para mi sitio personal utilize un proyecto el cual hice para un curso de desarrollo web el cual utiliza Bootstrap.

## Como Instalar y Jugar

- Es necesario tener la version más reciente de Python instalada y puesta dentro del PATH.
- Es necesario también tener instalada el módulo Freegames, esto se puede hacer a través de la herramienta PIP [pip install freegames]
- Finalmente puedes correr los archivos snake.py y pacman.py dentro de tu terminal de elección utilizando Python
- para acceder al sitio web ir a: http://ec2-52-1-3-19.compute-1.amazonaws.com/~team10/

