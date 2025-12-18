# Una clave con el siguiente formato XX00-xxX-00 donde las X deben de ser letras
# mayúsculas, las x letras minúsculas y los 0 d´ígitos.
# Ejemplo: AB12-xyZ-75

import re
def validar_clave(clave):
    return bool(re.fullmatch(r"[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}", clave))

print(validar_clave("AB12-xyZ-75"))
