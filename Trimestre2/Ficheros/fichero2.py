from sympy.conftest import file_clear_cache

fichero=open("quijote.txt","rt")
linea=fichero.readline()
while linea!="":
    print(linea)
    linea=fichero.readline()
linea =fichero.close()