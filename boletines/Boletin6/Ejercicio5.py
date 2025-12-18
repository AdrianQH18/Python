# Validar dos palabras de cualquier tamaño separadas por un único espacio en blanco.
# Las palabras no pueden contener números y deben de empezar ambas por una letra
# mayúscula.
# Ejemplo: Hola Mundo
import re
def validar_dos_palabras(texto):
    return bool(re.fullmatch(r"[A-Z][a-zA-Z]* [A-Z][a-zA-Z]*", texto))

print(validar_dos_palabras("Hola Mundo"))
