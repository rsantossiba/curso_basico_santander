"""
Conectar con la BD sqlite3.
Crear conexiones y cursores. Ejecutar una consulta.
"""

import sqlite3 as dbapi
from os.path import isfile


def consulta(tabla):
    """
    Lista el contenido de la tabla que recibe
    """
    pass


def testConexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero {path}")
        else:
            # Abrir la conexión:
            con = dbapi.connect(path)
            print("Conexión abierta ...")

    except Exception as e:
        print(e)

    finally:
        if con:
            con.close()


if __name__ == "__main__":
    testConexion('../bd/empresa3.db')
