import re

def validar_cp_madrid(cp):
    return bool(re.fullmatch(r"28\d{3}", cp))

print(validar_cp_madrid("28032"))
