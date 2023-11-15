import sqlite3

def crear_tabla_puntajes():
    with sqlite3.connect("bd_btf.db") as conexion:
        try:
            sentencia = '''CREATE TABLE tabla_puntajes
            (
            id PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre TEXT NOT NULL,
            puntaje TEXT NOT NULL
            )
            '''
            conexion.execute(sentencia)
        except sqlite3.OperationalError:
            pass

def crear_tabla_niveles():
    with sqlite3.connect("bd_btf.db") as conexion:
        try:
            sentencia = '''CREATE TABLE tabla_niveles
            (
            id PRIMARY KEY AUTOINCREMENT NOT NULL,
            nivel_alcanzado INTEGER NOT NULL
            )
            '''
            conexion.execute(sentencia)
        except sqlite3.OperationalError:
            pass

# INSERT:
def insertar_datos(nombre: str, puntaje: int):
    with sqlite3.connect("bd_btf.db") as conexion:
        conexion.execute("INSERT INTO tabla_puntajes(nombre, puntaje AS: INTEGER) VALUES (?, ?)", (nombre, str(puntaje)))
        conexion.commit()  # Actualiza los datos realmente en la tabla

# INSERT:
def insertar_datos_niveles(nivel_alcanzado:int):
    with sqlite3.connect("bd_btf.db") as conexion:
        conexion.execute("INSERT INTO tabla_niveles (nivel_alcanzado) VALUES (?)", (nivel_alcanzado))
        conexion.commit()  # Actualiza los datos realmente en la tabla

def listar_datos_buscados(cantidad_datos_buscados: int) -> list:
    lista_datos = []
    # SELECT con ORDER BY y LIMIT:
    with sqlite3.connect("bd_btf.db") as conexion:
        cursor = conexion.execute("SELECT * FROM tabla_puntajes ORDER BY ABS(puntaje) DESC LIMIT ?", (cantidad_datos_buscados,))
        for fila in cursor:
            lista_datos.append(fila)
    lista_datos_string = crear_strings_datos_lista(lista_datos)
    return lista_datos_string

def obtener_ultimo_dato() -> int:
    ultimo_dato = 0
    with sqlite3.connect("bd_btf.db") as conexion:
        cursor = conexion.execute("SELECT COUNT(*) FROM tabla_niveles")
        cantidad_filas = cursor.fetchone()[0]
    if cantidad_filas > 0:
    # SELECT con ORDER BY y LIMIT:
        with sqlite3.connect("bd_btf.db") as conexion:
            cursor = conexion.execute("SELECT * FROM tabla_niveles ORDER BY ABS(id) DESC LIMIT 1")
            ultimo_dato = cursor.fetchone()
    return ultimo_dato

def crear_strings_datos_lista (lista_datos:list)->list:
    nueva_lista = []
    i = 1
    for dato in lista_datos:
        dato = str(dato)
        dato = dato.replace("(","")
        dato = dato.replace(")","")
        dato = dato.replace("'","")
        dato = dato.replace(",","")
        dato = dato.replace(" ","    ")
        dato = dato.replace(dato[:1],f"{i}")
        nueva_lista.append(dato)
        i += 1
    return nueva_lista




