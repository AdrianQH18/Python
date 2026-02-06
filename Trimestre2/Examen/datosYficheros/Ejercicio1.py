class Pokemon:
    def __init__(self, linea):
        partes=linea.strip("\n").split(", ")
        self.codigo = partes[0]
        self.nombre=partes[1]
        self.peso=partes[2]
        self.altura=partes[3]
        self.tipo=partes[4]

    def mostrar(self):
        print(f"#{self.codigo} – {self.nombre}\nPeso: {self.peso}\nAltura: {self.altura}m\nTipo: {self.tipo}")

try:
    with open("pokemon.txt", "r") as fichero:
        pokemones= []
        erroneas=[]
        for linea in fichero.readlines():
            partes=linea.strip().split(", ")
            linea=linea.strip()
            try:
                if not partes[0].isdigit():
                    erroneas.append(linea)
                elif len(partes) < 5:
                    erroneas.append(linea.strip())
                else:
                    pokemon = Pokemon(linea)
                    pokemones.append(pokemon)
            except Exception as e:
                print(e)
        for i in pokemones:
            i.mostrar()
            print()
        print(f"{len(erroneas)} lineas Erroneas en el fichero")
        for error in erroneas:
            print(error)
except Exception as e:
    print(e)
