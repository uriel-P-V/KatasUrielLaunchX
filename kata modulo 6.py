planets=["mercurio","venus""tierra","marte","jupiter","sarturno","nepturno"]

print("la cantidad de planetas que hay es ",len(planets))

planets.append("pluton");
print("la cantidad de planetas que hay es ",len(planets))
print("el ultimo planeta es:",planets[-1])

nom=input("ingresa el nombre de un planet:")
pom=(planets.index(nom.lower()))
print("la posicion de ",nom.upper(), "es ",pom)
print("los planetas mas cercanos al sol en comparacion de",pom,"son:",planets[0:pom])
print("los planetas mas lejanos al sol en comparacion de",pom,"son:",planets[pom+1:])
