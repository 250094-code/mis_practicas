def calcular_are_triangulo(base, altura):
    area=(base*altura)/2
    return area
resultado=calcular_are_triangulo(10,5)
print(f"el area del triangulo es: {resultado}")

def saludar_poersona(nombre, edad):
    print(f"Hola {nombre} tienes {edad} años")
saludar_poersona("Carlos",20)