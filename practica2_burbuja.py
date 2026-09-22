
#lista con las 15 calificaciones
calificaciones = [8.5, 9.0, 6.5, 10.0, 7.0, 5.5, 8.0, 9.5, 7.5, 6.0, 8.8, 9.2, 7.8, 10.0, 6.8]

# Orden Ascendente
ascendente = calificaciones.copy()
n = len(ascendente)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        #ordenar de menor a mayor
        if ascendente[j] > ascendente[j + 1]:
            ascendente[j], ascendente[j + 1] = ascendente[j + 1], ascendente[j]
            swapped = True
    
    # Si no hubo intercambios en la pasada, la lista ya está ordenada
    if not swapped:
        break

print("Orden Ascendente:", ascendente)

# Orden Descendente
descendente = calificaciones.copy()
n = len(descendente)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        #ordenar de mayor a menor
        if descendente[j] < descendente[j + 1]:
            descendente[j], descendente[j + 1] = descendente[j + 1], descendente[j]
            swapped = True
            
    if not swapped:
        break

print("Orden descendente:", descendente)