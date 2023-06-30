#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#3. Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1.

n = int(input("Digite um número: "))
numeros = []

for contador in range(n):
    numeros.append(contador)

print("Lista de números:", numeros)
