"""
Listar el contenido de un fichero que se indica
por la línea de comandos
"""


def leerFichero(path):
    """
    Imprimir el contenido en consola
    """
    fich = None
    try:
        # Abrir el fichero en modo lectura
        fich = open(path, "r")
        for linea in fich:
            # Limpia el carácter fin de línea (EOL)
            linea = linea.strip()
            print(linea)

    except Exception as e:
        print(e)
    finally:
        if fich != None:
            fich.close()


if __name__ == "__main__":
    pass
