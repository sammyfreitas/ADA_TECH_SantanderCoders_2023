#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#9. Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 números digitados pelo usuário (sem converter os números para int ou float).

numeros = []

for i in range(5):
    numero = input("Digite um número: ")
    numeros.append(numero)
    
    if i == 0:
        print("Você digitou o primeiro número")
    elif i == 1:
        print("Você digitou o segundo número")
    elif i == 2:
        print("Você digitou o terceiro número")
    elif i == 3:
        print("Você digitou o quarto número")
    elif i == 4:
        print("Você digitou o quinto número")

print("Lista de números digitados:", numeros)








