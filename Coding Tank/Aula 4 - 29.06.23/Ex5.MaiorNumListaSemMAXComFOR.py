#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#5. Faça um programa que imprima o maior número de uma lista, sem usar o método max(). 

numeros = [13, 6, 78, 45, 2023, 29, 6]
maior_numero = numeros[0] 

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
print (numeros)
print("Maior número da lista:", maior_numero)



