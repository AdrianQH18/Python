from prueba4Pokemon import Pokemon, PokemonLegendari,Equipo
#import prueba4Pokemon
#p1=prueba4Pokemon.Pokemon("Bulbasaur")
#p2=prueba4Pokemon.Pokemon("Venasaur")

p1=Pokemon("Bulbasaur")
p2=Pokemon("Venasaur")
p1.mostrar()
p2.mostrar()
print()

p1.setEvolucion(p2)
p2=p2.evoluciona()
p1=p1.evoluciona()
print()

p1.mostrar()
p2.mostrar()