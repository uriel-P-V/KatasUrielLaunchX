new_planet=""
planets = []
while new_planet.lower() != 'done':
    planets.append(new_planet)
    new_planet = input('ingrese un nuevo planeta o escriba done para finalizar')
    

    for planetas in planets:
        print(planetas)
