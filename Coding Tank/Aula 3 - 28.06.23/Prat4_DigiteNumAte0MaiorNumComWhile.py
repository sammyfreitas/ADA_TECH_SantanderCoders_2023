#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While 
#Praticando
#4) Faça um programa em que o usuário digite números quaisquer que encerrará no momento em que o valor 0 seja digitado. Ao final diga qual foi o maior número digitado.

numero = float(input("Digite um número (0 para encerrar): "))
maior = numero

while numero != 0:
    numero = float(input("Digite um número (0 para encerrar): "))

    if numero > maior:
        maior = numero

print("O maior número digitado foi:", maior)



