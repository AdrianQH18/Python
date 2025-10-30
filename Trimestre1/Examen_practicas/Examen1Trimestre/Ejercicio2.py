import random
lista=[]
contadorPar=0
contadorImpar=0
print("10 numeros entre el 1 y el 1000")
for i in range(10):
    numeroRandom=random.randint(1,1000)
    lista.append(numeroRandom)
    print(numeroRandom,end=", ")
print("\b\b")
for i in range(len(lista)):
    if lista[i]%2==0:
        contadorPar+=1
    else:
        contadorImpar+=1
print("He generado ", contadorPar," numeros pares y ",contadorImpar," impares")
print("El numero mayor ha sido el ",max(lista)," el menor el ",min(lista))