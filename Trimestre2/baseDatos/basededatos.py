import mysql.connector
try:
    #conector hacia la base de datos
    connect=mysql.connector.connect(user='dam2',password='asdf.1234',host='localhost',database='adat8')
    #cursor
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM Album")
    for fila in cursor:
        print(fila)

    #cierre
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)