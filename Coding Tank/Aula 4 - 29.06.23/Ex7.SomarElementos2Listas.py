#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#7. Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual a soma dos elementos da lista 1 com os da lista 2, na mesma posição.

lista1 = [0, 2, 4, 6, 8]
lista2 = [1, 3, 5, 7, 9]

nova_lista = []

for i in range(len(lista1)):
    soma = lista1[i] + lista2[i]
    nova_lista.append(soma)

print("Nova lista:", nova_lista)





