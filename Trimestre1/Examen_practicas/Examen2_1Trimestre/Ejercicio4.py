import re
def matriculasValidas(*matriculas):
    matriculasValidas=0
    matriculasNoValidas = 0
    regex =r"^\b[0-9]{4}[- ]{1}[A-Za-z]{3}"
    for matricula in matriculas:
        if re.fullmatch(regex,matricula):
            print("La matricula "+matricula+" es valida")
            matriculasValidas+=1
        else:
            print("La matricula "+matricula+" es valida")
            matriculasNoValidas+=1
    print()
    print("Matriculas validas: ",matriculasValidas)
    print("Matriculas no validas: ", matriculasNoValidas)

matriculasValidas("123MX","7521-MXP","1232 CXC")
