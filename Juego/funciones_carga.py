from scripts.carga_archivos import cargar_imagenes
from scripts.mesas import Mesa
from scripts.comidas import Comidas
import pygame
from constantes import *

def cargar_imagenes_inicio(categoria_imagenes:str)->dict:
    match categoria_imagenes:
        case "nivel":
            imagenes = {
                "fondo" : cargar_imagenes("archivos\imagenes\\fondo_actualizado.png",1),
                "barra" : cargar_imagenes("archivos\\barra\\barra.png",1),
                "cliente" : cargar_imagenes("archivos\imagenes\clientes\cliente.png",1),
                "mesa" : cargar_imagenes("archivos\imagenes\mesa.png",1),
                "personaje_dcha" : cargar_imagenes("archivos\imagenes\personaje\derecha.png",1),
                "personaje_abajo" : cargar_imagenes("archivos\imagenes\personaje\\frente.png", 1),
                "personaje_izq" : cargar_imagenes("archivos\imagenes\personaje\izquierda.png",1),
                "personaje_arriba" : cargar_imagenes("archivos\imagenes\personaje\\atras.png",1),
                "monedas": cargar_imagenes("archivos\imagenes\dinero\monedas.png",1),
                "pilas_monedas": cargar_imagenes("archivos\imagenes\dinero\pila_monedas.png",1),
                "billetes": cargar_imagenes("archivos\imagenes\dinero\\billetes.png",1),
                "burbuja_dialogo_vacia": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_blanco.png",1),
                "burbuja_esperando": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_puntos_suspensivos.png",1),
                "burbuja_corazon": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_corazon.png",1),
                "burbuja_cruz": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_cruz.png",1),
            }
        case "menu":
            imagenes = {
                "fondo": cargar_imagenes("archivos\imagenes_menu\\fondo.png",1),
            }
        case "menu_niveles":
            imagenes = {
                "fondo": cargar_imagenes("archivos\imagenes_menu_niveles\\fondo.png",1),
                "nivel_uno":cargar_imagenes("archivos\imagenes_menu_niveles\\nivel_uno.png",1),
                "nivel_uno_bloqueado":cargar_imagenes("archivos\imagenes_menu_niveles\\nivel_uno_bloqueado.png",1),
                "nivel_dos":cargar_imagenes("archivos\imagenes_menu_niveles\\nivel_dos.png",1),
                "nivel_dos_bloqueado":cargar_imagenes("archivos\imagenes_menu_niveles\\nivel_dos_bloqueado.png",1),
                "nivel_tres":cargar_imagenes("archivos\imagenes_menu_niveles\\nivel_tres.png",1),
                "nivel_tres_bloqueado":cargar_imagenes("archivos\imagenes_menu_niveles\\nivel_tres_bloqueado.png",1)
            }
        case "final_juego":
            imagenes = {
                    "nivel_superado": cargar_imagenes("archivos\imagenes derrota\\victoria.png",1),
                    "nivel_no_superado":cargar_imagenes("archivos\imagenes derrota\derrota.png",1),}
        case "guardado":
            imagenes = {
                    "fondo": cargar_imagenes("archivos\guardado\guardar puntuacion.png",1),}
        case "ranking":
            imagenes = {
                    "fondo": cargar_imagenes("archivos\\ranking\pantalla ranking.png",1),}
    return imagenes

def cargar_lista_mesas (ubicaciones:list,diccionario_imagenes:dict):
    lista_mesas = []
    for ubicacion in ubicaciones:   
        mesa = Mesa([ubicacion[0],ubicacion[1]],diccionario_imagenes["mesa"])
        lista_mesas.append(mesa)
    return lista_mesas

def cargar_imagenes_comidas_disponibles (comidas_adicionales = [])->list:
    lista_comidas_disponibles = \
    [   
        cargar_imagenes("archivos\imagenes\comida\\bebida_amarilla.png",1),
        cargar_imagenes("archivos\imagenes\comida\\bebida_celeste.png",1),
        #cargar_imagenes("archivos\imagenes\comida\\bebida_naranja.png",1),    
        cargar_imagenes("archivos\imagenes\comida\\bebida_rosa.png",1),
        #cargar_imagenes("archivos\imagenes\comida\\bebida_verde.png",1),  
    ]
    for i in range (len(comidas_adicionales)):
        lista_comidas_disponibles.append(cargar_imagenes(comidas_adicionales[i],1))
    return lista_comidas_disponibles

def cargar_imagenes_clientes_disponibles (clientes_adicionales = [])->list:
    lista_clientes_disponibles = \
    [   
        [cargar_imagenes("archivos\imagenes\clientes\cliente.png",1),cargar_imagenes("archivos\imagenes\clientes\cliente neutro.png",1),cargar_imagenes("archivos\imagenes\clientes\cliente_enojo.png",1)],
        [cargar_imagenes("archivos\imagenes\clientes\cliente_dos.png",1),cargar_imagenes("archivos\imagenes\clientes\cliente_dos_neutro.png",1),cargar_imagenes("archivos\imagenes\clientes\cliente_dos_enojo.png",1)],
        [cargar_imagenes("archivos\imagenes\clientes\cliente_tres.png",1),cargar_imagenes("archivos\imagenes\clientes\cliente_tres_neutro.png",1),cargar_imagenes("archivos\imagenes\clientes\cliente_tres_enojo.png",1)]
    ]
    for i in range (len(clientes_adicionales)):
        lista_clientes_disponibles.append(cargar_imagenes(clientes_adicionales[i],1))
    return lista_clientes_disponibles

def cargar_sonidos(categoria_sonido = "nivel")->dict:
    match categoria_sonido:
        case ("nivel"):
            sonidos = {
                        "sonido_dinero": pygame.mixer.Sound("archivos\sonido\Sonido dinero.mp3"),
                        "sonido_plato": pygame.mixer.Sound("archivos\sonido\Sonido plato.mp3")
                    }
            #Establecemos volumen:
            sonidos["sonido_dinero"].set_volume(VOLUMEN_SONIDO_DINERO)
            sonidos["sonido_plato"].set_volume(VOLUMEN_SONIDOS)
        case("inicio"):
            sonidos = {"musica_fondo": pygame.mixer.Sound("archivos\sonido\Musica fondo.mp3")}
            sonidos["musica_fondo"].set_volume(VOLUMEN_MUSICA_FONDO)

    return sonidos

def cargar_textos(texto:str, tamaño = TAMAÑO_TEXTO_SUBTITULOS, color = COLOR_BORDO):
    letra = pygame.font.SysFont(FUENTE_TEXTO,tamaño)
    texto_pregunta = letra.render((texto),True,(color))
    return texto_pregunta

