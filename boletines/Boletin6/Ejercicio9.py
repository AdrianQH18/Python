# Un número de 4 cifras mínimo y 8 cifras máximo
# Ejemplo: 12345

import re
def validar_numero(num):
    return bool(re.fullmatch(r"\d{4,8}", num))

print(validar_numero("12345"))
