from nivel import Nivel

def cargar_niveles(nivel:int):
    match nivel:
        case 1:
            nivel_uno = Nivel(30000,200,[[3,4],[6,4],[4,6],[5,6]],[],[])
            nivel_completado = nivel_uno.correr_nivel()
    return nivel_completado