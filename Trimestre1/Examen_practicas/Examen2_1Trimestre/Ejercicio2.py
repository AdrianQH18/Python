def toDecimal(binario):
    decimal =0
    binarioReal=binario.isdigit()
    if binarioReal is True:
        for i in range(len(binario)):
            bit=binario[-(i+1)]
            if bit=="1":
                decimal+=2**i
        return decimal

print(toDecimal("10110"))
print(toDecimal("345"))
print(toDecimal("hola"))
"""
def toDecimal(binario):
    decimal =1
    binarioReal=binario.isdigit()
    if binarioReal is True:
        for i in range(len(binario)-1):
            if binario[i]=="1":
                decimal+=int(binario[i])+len(binario)-1+2
        return decimal
    else:
        return "-1"

print(toDecimal("10110"))
print(toDecimal("345"))
print(toDecimal("hola"))"""