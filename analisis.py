dataset = [10,5,8,12,15,20]

def calcular_promedio(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    return mediana  

promedio = calcular_promedio(dataset)
mediana = calcular_mediana(dataset)
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")

print("Estoy mofificando este archivo para probar el control de versiones")