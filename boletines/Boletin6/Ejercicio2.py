#Validar un número de teléfono
#Ejemplo: 91345566

import re
def validar_telefono_fijo(tel):
    return bool(re.fullmatch(r"\d{8}", tel))

print(validar_telefono_fijo("91345566"))
