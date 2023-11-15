from nivel import Nivel

def cargar_niveles(nivel:int):
    match nivel:
        case 1:
            nivel_uno = Nivel(40000,200,[[5,4]],[],[],100)
            nivel_completado = nivel_uno.correr_nivel()
        case 2:
            nivel_dos = Nivel(60000,800,[[7,5],[7,2],[3,5],[3,2]],["archivos\imagenes\comida\'bebida_amarilla.png"],[],90)
            nivel_completado = nivel_dos.correr_nivel()
        case 3:
            nivel_tres = Nivel(60000,800,[[2,5],[7,2],[5,5],[8,5],[3,2]],["archivos\imagenes\comida\'bebida_amarilla.png"],[],80)
            nivel_completado = nivel_tres.correr_nivel()
    return nivel_completado
