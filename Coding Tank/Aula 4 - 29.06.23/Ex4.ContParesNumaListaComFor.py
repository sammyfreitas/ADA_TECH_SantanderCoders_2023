#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#4. Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares. 

numeros = [13, 6, 78, 45, 2023, 29, 6]
contador_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1
print(numeros)
print("Quantidade de números pares:", contador_pares)

