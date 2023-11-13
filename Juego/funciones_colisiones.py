def comprobar_colisiones_objeto(objeto,rect_personaje) -> dict:

    colisiones = {"izquierda":False,"derecha":False,"arriba":False,"abajo":False,"choco_objeto":True} 

    rects_objeto = [objeto.rect_objeto_izquierda,objeto.rect_objeto_derecha,objeto.rect_objeto_arriba,objeto.rect_objeto_abajo]
    if rect_personaje.colliderect(rects_objeto[0]):
        choco_por_izquierda = True
        colisiones["izquierda"] = choco_por_izquierda
    elif rect_personaje.colliderect(rects_objeto[1]):
        choco_por_derecha = True
        colisiones["derecha"] = choco_por_derecha
    elif rect_personaje.colliderect(rects_objeto[2]):
        choco_por_arriba = True
        colisiones["arriba"] = choco_por_arriba
    elif rect_personaje.colliderect(rects_objeto[3]):
        choco_por_abajo = True
        colisiones["abajo"] = choco_por_abajo
    else:
        choco_objeto = False
        colisiones["choco_objeto"] = choco_objeto
    
    return(colisiones)

def comprobar_choque_lista_objetos (lista_objeto_colision:list,rect_personaje) -> dict:
    colisiones_derecha = [False]
    colisiones_izquierda = [False]
    colisiones_arriba = [False]
    colisiones_abajo = [False]
    colisiones_objeto = [True]

    for objeto in lista_objeto_colision:
        colision = comprobar_colisiones_objeto(objeto,rect_personaje)
        colisiones_izquierda.append(colision["izquierda"])
        colisiones_derecha.append(colision["derecha"])
        colisiones_arriba.append(colision["arriba"])
        colisiones_abajo.append(colision["abajo"])
        colisiones_objeto.append(colision["choco_objeto"])

    dic_colisiones = {"izquierda":colisiones_izquierda,"derecha":colisiones_derecha,"arriba":colisiones_arriba,"abajo":colisiones_abajo,"choco_objeto":colisiones_objeto} 

    return(dic_colisiones)

def comprobar_choque_losa(rect_personaje,rect_losa)-> bool:
    if rect_personaje.colliderect(rect_losa):
        piso_losa = True
    else:
        piso_losa = False
    return piso_losa

def comprobar_choque_losa_lista(rect_personaje,lista_objetos):
    lista_colisiones = []
    for objeto in lista_objetos:
        colision = comprobar_choque_losa(rect_personaje,objeto.rect_objeto_izquierda)
        lista_colisiones.append(colision)
    return lista_colisiones
    