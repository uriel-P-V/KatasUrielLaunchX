def fu(tanque1,tanque2,tanque3):
    prom=(tanque1+tanque2+tanque3)/3
    return"""reporte
    promedio: {}%
    tanque 1: {}%
    tanque 2: {}%
    tanque 3: {}%
    """.format(prom,tanque1,tanque2,tanque3)
    

print(fu(10, 15, 20))

def promedio(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items
def fu(tanque1,tanque2,tanque3):
    prom=(tanque1+tanque2+tanque3)/3
    return"""reporte
    promedio: {}%
    tanque 1: {}%
    tanque 2: {}%
    tanque 3: {}%
    """.format(prom,tanque1,tanque2,tanque3)
print(fu(25, 30, 35))


def cohete(hora,minutes,destino,externo,interno):
    return f"""cohete:
    hora de prelanzamiento: {hora} horas
    tiempo de vuelo: {minutes} minutos
    destino: {destino}
    tanque externo: {externo} galones
    tanque interno: {interno} galones
    """ 
print(cohete(2, 30000, "marte", 15000, 20000))
def cohete(destino,*minutes, **fuel_reservoirs):
    return f"""cohete:
    tiempo total del viaje: {sum(minutes)} minutos
    destino: {destino}
    total de gasolina: {sum(fuel_reservoirs.values())} galones
    """ 
print(cohete("marte",120,30000, externo=15000, interno=20000 ))  
def cohete(destino,*minutes, **fuel_reservoirs):
    
    tanquee = f"""
    cohete:
    tiempo total del viaje: {sum(minutes)} minutos
    destino: {destino}
    
    """
    for tanque, galones in fuel_reservoirs.items():
        tanquee +=f"""tanque {tanque}: {galones} galones \n"""
    return tanquee

print(cohete("marte",120,30000, externo=15000, interno=20000 ))  


