#Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado por
#el usuario (se introducirá por teclado)
numero=int(input("Incerte un numero para saber sus primeros 5 multiplos: "))
for i in range(1,6,1):
    print("Multiplo ",i," :",i*numero)