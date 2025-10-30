#Idem al anterior pero ordenando ahora en orden descendente
cadena1=input("introduce cadena1")
cadena2=input("introduce cadena2")
cadena3=input("introduce cadena3")
primeraPalabra=max(cadena1,cadena2)
ultimaPalabra=min(cadena1,cadena2)
if cadena3<ultimaPalabra:
    print(primeraPalabra," ",ultimaPalabra," ",cadena3)
elif cadena3>ultimaPalabra and cadena3<primeraPalabra:
    print(primeraPalabra, " ",cadena3," ", ultimaPalabra)
else:
    print(cadena3," ",primeraPalabra, " ", ultimaPalabra)