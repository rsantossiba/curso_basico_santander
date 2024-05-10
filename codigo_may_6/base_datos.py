"""
Conectar con la BD sqlite3. Crear conexiones, cursores, exportar datos
"""

import sqlite3 as db
import sys
from os.path import isfile


def conexion(path, tabla, file=sys.stdout, sep=";"):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")

        con = db.connect(path)
        cur = con.cursor()
        sql = f"select * from {tabla}"
        cur.execute(sql)
        cabs = sep.join([t[0] for t in cur.description])
        print(cabs,file=file)
        for t in cur.fetchall():
            fila = sep.join([str(i) for i in t])
            print(fila, file=file)

    except Exception as e:
        print(e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()

def exportar(path, tabla, sep=";"):
    path_file = f"../ficheros/{tabla}.csv"
    fich = open(path_file, "w")    
    conexion(path, tabla, fich, sep)
    fich.close()

if __name__ == "__main__":
    #conexion("../../bd/empresa3.db", "pedidos")
    exportar("../../bd/empresa3.db", "pedidos")