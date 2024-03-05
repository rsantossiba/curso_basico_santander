"""
Ejemplos de funciones
"""

import os


def filtroFicheros(path, *extensiones):
    L = os.listdir(path)
    for fich in L:
        ext = fich.partition(".")[2]
        if ext in extensiones:
            print(fich)


if __name__ == "__main__":
    # filtroFicheros('../ficheros_curso')
    filtroFicheros(".", "py")
    filtroFicheros(".", "py", "pdf")
    filtroFicheros(".", "py", "docx", "xslx")
