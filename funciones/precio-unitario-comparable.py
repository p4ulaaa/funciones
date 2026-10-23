def calcular_precio_gramo(precio_total, cantidad_gramos):
    resultado = precio_total / cantidad_gramos
    return resultado

precio_1 = float(input("Ingrese el precio total del paquete 1: "))
gramos_1 = float(input("Ingrese la cantidad en gramos del paquete 1: "))

while precio_1 < 0 or gramos_1 <= 0:
    print("Error: El precio no puede ser negativo y los gramos deben ser mayores que cero.")
    precio_1 = float(input("Ingrese el precio total del paquete 1: "))
    gramos_1 = float(input("Ingrese la cantidad en gramos del paquete 1: "))

precio_2 = float(input("Ingrese el precio total del paquete 2: "))
gramos_2 = float(input("Ingrese la cantidad en gramos del paquete 2: "))

while precio_2 < 0 or gramos_2 <= 0:
    print("Error: El precio no puede ser negativo y los gramos deben ser mayores que cero.")
    precio_2 = float(input("Ingrese el precio total del paquete 2: "))
    gramos_2 = float(input("Ingrese la cantidad en gramos del paquete 2: "))

precio_por_gramo_1 = calcular_precio_gramo(precio_1, gramos_1)
precio_por_gramo_2 = calcular_precio_gramo(precio_2, gramos_2)

print("Precios por gramo:", precio_por_gramo_1, "y", precio_por_gramo_2, "pesos")

if precio_por_gramo_1 < precio_por_gramo_2:
    print("Conviene paquete 1")
elif precio_por_gramo_2 < precio_por_gramo_1:
    print("Conviene paquete 2")
else:
    print("Hay igualdad en los precios")
