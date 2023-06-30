#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#8. Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.

lista1 = [0, 2, 4, 6, 8]
lista2 = [1, 3, 5, 7, 9]

produto_escalar = 0

for i in range(len(lista1)):
    produto_escalar += lista1[i] * lista2[i]

print("Produto escalar:", produto_escalar)







