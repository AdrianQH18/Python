#Escribir un programa que nos pida tres palabras por teclado en cualquier orden y nos las
#muestre en pantalla ordenadas alfabeticamente en orden ascendente
cadena1=str(input("introduce cadena1"))
cadena2=str(input("introduce cadena2"))
cadena3=str(input("introduce cadena3"))
primeraPalabra=min(cadena1,cadena2)
ultimaPalabra=max(cadena1,cadena2)
if cadena3<primeraPalabra:
    print(cadena3," ",primeraPalabra," ",ultimaPalabra)
elif cadena3>primeraPalabra and cadena3<ultimaPalabra:
    print(primeraPalabra, " ",cadena3," ", ultimaPalabra)
else:
    print(primeraPalabra, " ", ultimaPalabra," ",cadena3)