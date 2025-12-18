#Validar un número de teléfono móvil (debe de empezar por 6, 7 u 8)
#Ejemplo: 655776655

import re
def validar_movil(movil):
    return bool(re.fullmatch(r"[678]\d{8}", movil))

print(validar_movil("655776655"))
