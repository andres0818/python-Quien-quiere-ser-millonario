
'''
se van a tener 20 preguntas en el banco
por juego se seleccionan 5 preguntas de forma aleatoria
cada pregunta tiene 4 posibles respuestas pero solo una es verdadera
al seleccionar la pregunta verdadera se van a acomular 100 puntos
si se responde una pregunta incorrectamente le sale un mensaje "Respuesta incorrecta"
al finalizar las preguntas se muestra el puntaje acomulado y  un premio respectivo a los puntos deacuerdo a la sgt tabla
	pts	premio
	100	licuadora
	200	horno
	300	ventilador
	400	tv
	500	computador
Al finalizar las preguntas se muestra un menu donde da la opcion de jugar de nuevo o terminar el juego
Al reiniciar el juego debe reiniciarse el puntaje
'''


RESPUESTA = 'S'

NUMERO_PREGUNTAS = 5
puntaje = 0

pregunta_actual = {
    "pregunta":"¿Cuantos huesos hay en el cuerpo humano?",
    "respuesta_correcta":"D",
    "opciones":'''
    A) 195
    b) 306
    C) 200
    D) 206'''
    }





def leer_pregunta(pregunta):
    global puntaje
    print(pregunta["pregunta"],pregunta["opciones"])
    respuesta=input("Ingrese la respuesta: ").upper()
    correcto = respuesta==pregunta["respuesta_correcta"]
    
    if correcto:
        print("Respuesta correcta")
        puntaje=puntaje+100
    else:
        print("Respuesta incorrecta\n")




import random



preguntas=[pregunta_actual,{
    "pregunta":"¿Cuando acabo la II guerra mundial?",
    "respuesta_correcta":"C",
    "opciones":'''
    A) 1935
    B) 1845
    C) 1945
    D) 1954'''
    },{
    "pregunta":"¿Quién pintó “la última cena?",
    "respuesta_correcta":"A",
    "opciones":'''
    A) Leonardo DaVinci
    B) Judas
    C) Picaso
    D) Mateo'''
    },{
    "pregunta":"¿Dónde se encuentra la Sagrada Familia?",
    "respuesta_correcta":"B",
    "opciones":'''
    A) En Barcelona
    B) En la iglesia
    C) En la casa
    D) En el corazon'''
    },{
    "pregunta":"¿Cuál es el océano más grande del mundo?",
    "respuesta_correcta":"A",
    "opciones":'''
    A) El océano Pacífico
    B) El océano Atlantico
    C) El océano indigo
    D) El océano Artico'''
    },{
    "pregunta":"¿Cuál es el país más grande del mundo?",
    "respuesta_correcta":"A",
    "opciones":'''
    A) Brasil
    B) Colombia
    C) Europa
    D) Rusia'''
    },{
    "pregunta":"¿Cual es país más poblado de la Tierra?",
    "respuesta_correcta":"A",
    "opciones":'''
    A) China
    B) EEUU
    C) Belgica
    D) Japon'''
    },{
    "pregunta":"¿Cuál es el libro más vendido de la historia?",
    "respuesta_correcta":"B",
    "opciones":'''
    A) El gato negro
    B) La Biblia
    C) Harry potter
    D) El alquimista'''
    },{
    "pregunta":"¿Cómo se llaman las crías de los conejos?",
    "respuesta_correcta":"C",
    "opciones":'''
    A) Caloyo
    B) Pollino
    C) Gazapos
    D) Borrico'''
    },{
    "pregunta":"¿Cuál es la ciudad de los rascacielos?",
    "respuesta_correcta":"D",
    "opciones":'''
    A) Dubai
    B) Japon
    C) California
    D) New York'''
    },{
    "pregunta":"¿Cuántas válvulas tiene el corazón humano?",
    "respuesta_correcta":"A",
    "opciones":'''
    A) 4
    B) 6
    C) 1
    D) Ninguna'''
    },{
    "pregunta":"¿Cuál es el apellido de la reina Isabel II de Inglaterra?",
    "respuesta_correcta":"A",
    "opciones":'''
    A) Windsor
    B) Smith
    C) Williams
    D) Brown'''
    },{
    "pregunta":"¿Cuál es el libro sagrado del Islam?",
    "respuesta_correcta":"B",
    "opciones":'''
    A) La Biblia
    B) El coran
    C) Islam
    D) Rripitaka'''
    },{
    "pregunta":"¿Qué día es la fiesta de la hispanidad?",
    "respuesta_correcta":"C",
    "opciones":'''
    A) El 11 de noviembre
    B) El 13 de agosto
    C) El 12 de octubre
    D) El 14 de abril'''
    },{
    "pregunta":"¿Cómo se llama el proceso por el cual las plantas se alimentan?",
    "respuesta_correcta":"D",
    "opciones":'''
    A) Mitosis
    B) Polinizacion
    C) Simbiosis
    D) Fotosintesis'''
    },{
    "pregunta":"¿Cuál es el músculo más fuerte del cuerpo human?",
    "respuesta_correcta":"A",
    "opciones":'''
    A) Masetero
    B) La lengua
    C) Cuadripces
    D) pectorales'''
    },{
    "pregunta":"¿Dónde está la Casa Blanca?",
    "respuesta_correcta":"B",
    "opciones":'''
    A) Holiwood
    B) Washintong D.C.
    C) Los angeles
    D) CAlifornia'''
    },{
    "pregunta":"¿Cuánto vale el número pi?",
    "respuesta_correcta":"C",
    "opciones":'''
    A) 3,1417
    B) 3.1516
    C) 3,1416
    D) 3,0141'''
    },{
    "pregunta":"¿Qué elemento de la tabla periódica tiene como símbolo He?",
    "respuesta_correcta":"D",
    "opciones":'''
    A) Hierro
    B) Hidrogeno
    C) Holmo
    D) Helio'''
    }]


def juego():
    contador=1
    while contador <= NUMERO_PREGUNTAS:
        print("")
        contador+=1
        aleatorio=random.randint(0,len(preguntas)-1)
        pregunta=preguntas[aleatorio]
        leer_pregunta(pregunta)

def puntos():
    if puntaje == 0:
        print("%d Puntos: no hay premio \n"%(puntaje))
    elif puntaje == 100:
        print("%d Puntos El premio es una licuadora\n"%(puntaje))
    elif puntaje == 200:
        print("%d Puntos: El premio es una Horno\n"%(puntaje))
    elif puntaje == 300:
        print("%d Puntos: El premio es una Ventilador\n"%(puntaje))
    elif puntaje == 400:
        print("%d Puntos: El premio es una Tv\n"%(puntaje))
    else:
        print("%d Puntos: El premio es una Computador\n"%(puntaje))
    
# def puntos2():
#     """
#         Muestra el premio obtenido al jugar.
#     """
#     premios = {
#         0: 'No hay premio',
#         100: 'Licuadora',
#         200: 'Horno',
#         300: 'Ventilador',
#         400: 'TV',
#         500: 'Computador'
#     }
#     print("%d Puntos: El premio es un %s" % (puntaje, premios[puntaje]))

juego()
puntos()
nuevo_juego = input("Jugar de nuevo S/N: \n").upper()

while True:
    if nuevo_juego == 'S':
        juego()
        puntos()
        nuevo_juego = input("Jugar de nuevo S/N: \n").upper()
        puntaje = 0
    else:
        nuevo_juego == 'N'
        print("fin del juego\n")
        break