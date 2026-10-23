def calcular_valor_absoluto(numero):
    if numero < 0:
        resultado = -numero
    else:
        resultado = numero
    return resultado

def es_aceptable(medicion, objetivo, tolerancia):
    error = calcular_valor_absoluto(medicion - objetivo)
    resultado = error <= tolerancia
    return resultado

objetivo = float(input("Ingrese el valor objetivo: "))
tolerancia = float(input("Ingrese la tolerancia (no negativa): "))

while tolerancia < 0:
    print("Error: La tolerancia no puede ser negativa. Intente nuevamente.")
    tolerancia = float(input("Ingrese la tolerancia (no negativa): "))

medicion_1 = float(input("Ingrese la primera medición: "))
medicion_2 = float(input("Ingrese la segunda medición: "))

resultado_1 = es_aceptable(medicion_1, objetivo, tolerancia)
resultado_2 = es_aceptable(medicion_2, objetivo, tolerancia)

if resultado_1:
    texto_1 = "verdadero"
else:
    texto_1 = "falso"

if resultado_2:
    texto_2 = "verdadero"
else:
    texto_2 = "falso"

print("Aceptables:", texto_1 + ";", texto_2)
