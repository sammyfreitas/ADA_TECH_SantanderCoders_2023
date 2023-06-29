#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While 
#Praticando
#2) Faça um programa que mostre o fatorial de um número digitado. 

num = int(input("Digite um número inteiro: "))

fatorial = 1
contador = 1

while contador <= num:
    fatorial *= contador
    contador += 1

print("O fatorial de", num, "é", fatorial)
