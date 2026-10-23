def calcular_area(base, altura):
    resultado = (base * altura) / 2
    return resultado

# Validar la primera base y altura (deben ser mayores que 0)
base_1 = float(input("Ingrese la primera base (mayor a 0): "))
altura_1 = float(input("Ingrese la primera altura (mayor a 0): "))

while base_1 <= 0 or altura_1 <= 0:
    print("Error: Los valores deben ser positivos. Intente nuevamente.")
    base_1 = float(input("Ingrese la primera base (mayor a 0): "))
    altura_1 = float(input("Ingrese la primera altura (mayor a 0): "))

# Validar la segunda base y altura
base_2 = float(input("Ingrese la segunda base (mayor a 0): "))
altura_2 = float(input("Ingrese la segunda altura (mayor a 0): "))

while base_2 <= 0 or altura_2 <= 0:
    print("Error: Los valores deben ser positivos. Intente nuevamente.")
    base_2 = float(input("Ingrese la segunda base (mayor a 0): "))
    altura_2 = float(input("Ingrese la segunda altura (mayor a 0): "))

# Llamadas a la función
area_1 = calcular_area(base_1, altura_1)
area_2 = calcular_area(base_2, altura_2)

suma_areas = area_1 + area_2

# Salida
print("Áreas:", area_1, "y", area_2, "cm²; suma:", suma_areas, "cm²")