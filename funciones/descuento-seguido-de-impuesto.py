def calcular_subtotal(base, descuento):
    resultado = base * (1 - (descuento / 100))
    return resultado

def calcular_total(subtotal, impuesto):
    resultado = subtotal * (1 + (impuesto / 100))
    return resultado

base = float(input("Ingrese la base en pesos: "))
descuento = float(input("Ingrese el porcentaje de descuento (0 a 100): "))

while base < 0 or descuento < 0 or descuento > 100:
    print("Error: La base no puede ser negativa y el descuento debe estar entre 0 y 100. Intente nuevamente.")
    base = float(input("Ingrese la base en pesos: "))
    descuento = float(input("Ingrese el porcentaje de descuento (0 a 100): "))

impuesto = float(input("Ingrese el porcentaje de impuesto (no negativo): "))

while impuesto < 0:
    print("Error: El impuesto no puede ser negativo. Intente nuevamente.")
    impuesto = float(input("Ingrese el porcentaje de impuesto (no negativo): "))

subtotal = calcular_subtotal(base, descuento)
total = calcular_total(subtotal, impuesto)

print("Subtotal:", subtotal, "; total:", total, "pesos")
