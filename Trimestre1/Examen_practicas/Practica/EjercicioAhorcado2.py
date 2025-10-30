frase=input("Introduce una frase: ")
letra=input("Letra a mantener: ")
nuevaLetra=input("Introduce una letra")
contador=0
for i in frase:
    if i==letra or i==nuevaLetra:
        print(i, end="")
        if i==nuevaLetra:
            contador+=1
    else:
        if i==" ":
            print(" ",end="")
        else:
            print("*",end="")
print("\nla letra ",nuevaLetra," aparece en ",contador," ocasiones")