
# 4. Escribir un programa que nos pida una cadena por teclado y luego cuente cuantas
# palabras hay en ella con cuatro o más vocales diferentes. Por ejemplo, si introducimos
# la frase “Crisis constitucional por culpa del murcielago guineoecuatorial” Nos debería
# de decir que 3. Tendrías que tener en cuenta que las vocales pueden ir en mayúsculas
# o no y son la misma letra. Presupón que ninguna vocal va acentuada de ninguna
# forma.

frase = input("Ejercicio 4: Introduce una frase: ")
countVocales = 0

for palabra in frase.split():
    vocales_en_palabra = ""  # Guardamos las vocales diferentes encontradas
    for letra in palabra:
        if letra in "aeiouAEIOU" and letra.lower() not in vocales_en_palabra:
            vocales_en_palabra += letra.lower()  # Comprobamos las vocales que esten nuestra frase
    # Si hay 4 o más vocales diferentes, sumamos 1
    if len(vocales_en_palabra) >= 4:
        countVocales += 1

print(f"Número de palabras con 4 o más vocales diferentes: {countVocales}")
