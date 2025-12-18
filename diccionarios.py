#Diccionario básico (clave → valor)
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

print(persona["nombre"])
print(persona["edad"])


#2️⃣ Diccionario con distintos tipos de datos
producto = {
    "nombre": "Portátil",
    "precio": 899.99,
    "stock": True,
    "unidades": 12
}

#3️⃣ Acceder con .get() (evita errores)
print(persona.get("telefono", "No existe"))

#4️⃣ Modificar valores
persona["edad"] = 26
persona["email"] = "ana@email.com"

#5️⃣ Recorrer un diccionario
for clave, valor in persona.items():
    print(clave, "->", valor)

#6️⃣ Diccionario de notas (ejemplo típico)
notas = {
    "Juan": 7,
    "Ana": 9,
    "Luis": 5
}

for alumno, nota in notas.items():
    print(alumno, nota)

#7️⃣ Diccionario con listas como valores
agenda = {
    "Juan": ["666123123", "juan@email.com"],
    "Ana": ["611222333", "ana@email.com"]
}

#8️⃣ Diccionario con diccionarios (2D)
alumnos = {
    "A001": {"nombre": "Lucía", "nota": 8},
    "A002": {"nombre": "Pedro", "nota": 6}
}

print(alumnos["A001"]["nombre"])

#9️⃣ Contar palabras (uso MUY típico)
texto = "hola hola mundo mundo mundo"
contador = {}

for palabra in texto.split():
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)


#🔟 Diccionario + match
operaciones = {
    "S": lambda a, b: a + b,
    "R": lambda a, b: a - b
}

op = "S"
print(operaciones[op](5, 3))

#