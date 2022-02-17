text1="""Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth.""" 
text="""On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
def e():
    part= text.split(".");
    palabras = ["average", "temperature", "distance"];

    for auxiliar in part:
        for palabra in palabras:
            if palabra in auxiliar:
                print(auxiliar)
                break

    for auxiliar in part:
        for palabra in palabras:
            if palabra in auxiliar:
                print(auxiliar.replace(' C', ' Celsius'))
                break


name = "Moon"
gravity = 0.00162 # in kms
planet = "Tierra"


titulo="la gravedad de la {}".format( name)
o=titulo.title();
metros="{:.3f}".format (gravity*1000);
union=f"{o}\nla graveda de la {name} es: {metros} m/s2 \nNombre del planeta: {planet}"
print(union)


planet = 'Marte '
gravity  = 0.00143
nombre = 'Ganímedes'

union2="la graveda de la {name} es: {metros} m/s2 \nNombre del planeta: {planet}"
print(union2.format(name=nombre,metros="{:.3f}".format (gravity*1000),planet=planet))



