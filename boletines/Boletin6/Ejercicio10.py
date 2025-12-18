# Una dirección IP pública de clase C. Cuatro bytes en formato decimal separados por un
# punto. Los dos primeros tienen que ser siempre 192.168.
# Ejemplo: 192.168.30.30

import re

def validar_ip(ip):
    return bool(re.fullmatch(r"192\.168\.(\d{1,3})\.(\d{1,3})", ip))

print(validar_ip("192.168.30.30"))
