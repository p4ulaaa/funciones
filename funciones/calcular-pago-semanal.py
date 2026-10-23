def calcular_pago_semanal(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
    else:
        pago = (40 * tarifa) + ((horas - 40) * tarifa * 1.5)
    return pago

horas_1 = float(input("Ingrese las horas semanales de la persona 1: "))
tarifa_1 = float(input("Ingrese la tarifa por hora de la persona 1: "))

while horas_1 < 0 or tarifa_1 < 0:
    print("Error: Las horas y la tarifa no pueden ser negativas. Intente nuevamente.")
    horas_1 = float(input("Ingrese las horas semanales de la persona 1: "))
    tarifa_1 = float(input("Ingrese la tarifa por hora de la persona 1: "))

horas_2 = float(input("Ingrese las horas semanales de la persona 2: "))
tarifa_2 = float(input("Ingrese la tarifa por hora de la persona 2: "))

while horas_2 < 0 or tarifa_2 < 0:
    print("Error: Las horas y la tarifa no pueden ser negativas. Intente nuevamente.")
    horas_2 = float(input("Ingrese las horas semanales de la persona 2: "))
    tarifa_2 = float(input("Ingrese la tarifa por hora de la persona 2: "))

pago_1 = calcular_pago_semanal(horas_1, tarifa_1)
pago_2 = calcular_pago_semanal(horas_2, tarifa_2)

total_pagos = pago_1 + pago_2

print("Pagos:", pago_1, "y", pago_2, "pesos; total:", total_pagos)