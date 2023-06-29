#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While 
#Praticando
#1) Escreva um programa que solicite um número inteiro e imprima na tela todos os números de 1 até o número digitado, separado por espaços. 
#Exemplo: número digitado: 5  / Resultado esperado: 1 2 3 4 5

num = int(input("Digite um número inteiro: "))
contador = 1

while contador <= num:
    print(contador, end=" ")
    contador += 1

print()  # Imprime uma quebra de linha após todos os números



