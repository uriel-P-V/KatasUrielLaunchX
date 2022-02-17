
planet={
    "name": "Mars",
    "moons": 2    
}
print("las lunas que tiene el planeta",planet.get("name"),"son:",planet["moons"])

planet["circumference (km)"] = {
    'polar': 6752,
    'equatorial': 6792
}
print("el planeta",planet["name"],"tiene una circuferencia polar de",planet["circumference (km)"]["polar"],"km")

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons=planet_moons.values()
planets=len(planet_moons.keys())
total_moons = 0

for moon in moons:
    total_moons=total_moons+moon
    pro=total_moons/planets

    print("promedio",pro)

#intente de agregar el nombre que correspondia a cada promedio, pero no puede crear un bucle 
# para ello o algo similar. print(f"{planet_moons.get(moon)}:{pro}")
            