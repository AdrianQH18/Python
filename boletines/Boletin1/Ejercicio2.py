#Escribir un programa donde se muestren los 50 primeros números pares
for i in range(101):
    if i%2==0:
        print(i,end=",")
print("\b")