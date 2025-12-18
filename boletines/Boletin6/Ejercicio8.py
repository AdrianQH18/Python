# Un IBAN bancario de España. Las dos letras iniciales siempre tienen que ser ES
# Ejemplo: ES61 1234 3456 42 0456323532

import re
def validar_iban(iban):
    return bool(re.fullmatch(r"ES\d{2}( \d{4}){3} \d{2} \d{10}", iban))

print(validar_iban("ES61 1234 3456 42 0456323532"))
