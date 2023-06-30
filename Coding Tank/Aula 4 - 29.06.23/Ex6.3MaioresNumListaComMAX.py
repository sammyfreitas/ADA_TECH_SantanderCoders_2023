#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#6. Agora usando o método max() faça um programa que imprima os três maiores números de uma lista.

numeros = [13, 6, 78, 45, 2023, 29, 6]
print("Lista inicial:", numeros)

maior1 = max(numeros)
numeros.remove(maior1)

maior2 = max(numeros)
numeros.remove(maior2)

maior3 = max(numeros)

tres_maiores = [maior1, maior2, maior3]

print("Os três maiores números são:", tres_maiores)




