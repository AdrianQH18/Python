# Validar un número de teléfono con prefijo internacional (empieza por el signo + seguido
# de dos dígitos, luego un espacio y a continuación un número de teléfono.
# Ejemplo +34 912233444
import re
def validar_prefijo_internacional(tel):
    return bool(re.fullmatch(r"\+\d{2} \d{9}", tel))

print(validar_prefijo_internacional("+34 912233444"))
