# Validar una tarjeta de crédito: cuatro grupos de cuatro números cada uno separados por
# un espacio. A continuación un espacio y la fecha de caducidad en formato MM/YY. El
# mes tiene que ser válido (entre 01 y 12)
# Ejemplo: 1234 5678 9012 3456 03/25

import re
def validar_tarjeta(tarjeta):
    return bool(re.fullmatch(r"(\d{4} ){3}\d{4} (0[1-9]|1[0-2])/\d{2}", tarjeta))

print(validar_tarjeta("1234 5678 9012 3456 03/25"))
