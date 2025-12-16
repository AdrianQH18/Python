# Queremos implementar una clase para gestionar nuestra colección de mangas con las
# siguientes características:
# - Por cada manga guardaremos el nombre del mangaka (autor) el título de la colección (en
# japonés, obligatorio y en español, opcional), el género prinicpal (shonen, shojo, seinen, josei,
# kodomo, yuri, spokon, isekai y hentai) y el último número publicado en la colección. Crea
# getters para todos ellos y setter para el título en castellano (por si originalmente no lo
# sabemos y luego lo queremos añadir) y para el número por el que va la colección.
# - Queremos, además, poder actualizar los números que tenemos y saber que números nos
# faltan. Para ello crearemos dos métodos: uno que nos permitirá introducir los números que
# vamos comprando (permitiendo una entrada variable de argumentos para cuando
# compramos mas de uno a la vez) y otro que nos diga que números nos faltan para completar
# la colección.
# - Si cuando introducimos los números que compramos resulta que ya tenemos alguno de
# ellos repetido debería de advertirnos
# - También necesitaremos un metodo que nos permita eliminar un número (lo hemos perdido,
# etc.). Si tratamos de eliminar un número que no tenemos debería de advertírsenos
class Manga:
    GenerosValidos = {"shonen", "shojo", "seinen", "josei", "kodomo", "yuri", "spokon", "isekai", "hentai"}
    def __init__(self,mangaka,titulo_japones,genero,ultimo_publicado,titulo_espanol=None):
        if genero not in self.GenerosValidos:
            raise ValueError("Genero no valido")
        self._mangaka = mangaka
        self._titulo_japones = titulo_japones
        self._titulo_espanol = titulo_espanol
        self._genero = genero
        self._ultimo_publicado = ultimo_publicado
        self._numeros_comprado=set()

    @property
    def mangaka(self):
        return self._mangaka
    @property
    def titulo_japones(self):
        return self._titulo_japones
    @property
    def titulo_espanol(self):
        return self._titulo_espanol
    @property
    def genero(self):
        return self._genero
    @property
    def ultimo_publicado(self):
        return self._ultimo_publicado

    @titulo_espanol.setter
    def titulo_espanol(self, titulo_espanol):
        self._titulo_espanol = titulo_espanol

    @ultimo_publicado.setter
    def ultimo_publicado(self, ultimo_publicado):
        self._ultimo_publicado = ultimo_publicado


    def comprar_numeros(self,*numeros):
        for numero in numeros:
            if numero in self._numeros_comprado:
                print("ya tienes el numero")
            else:
                self._numeros_comprado.add(numero)

    def eliminar_numeros(self,numero):
        if numero not in self._numeros_comprado:
            print("el numero no existe, no lo puedes borrar")
        else:
            self._numeros_comprado.remove(numero)

    def numeros_faltantes(self):
        return sorted(
            set(range(1, self._ultimo_publicado + 1)) - self._numeros_comprado
        )

m = Manga("Eiichiro Oda", "ワンピース", "shonen", 109)

m.comprar_numeros(1, 2, 3, 5, 5)
m.eliminar_numeros(5)
m.eliminar_numeros(2)

print("Faltan:", m.numeros_faltantes())
