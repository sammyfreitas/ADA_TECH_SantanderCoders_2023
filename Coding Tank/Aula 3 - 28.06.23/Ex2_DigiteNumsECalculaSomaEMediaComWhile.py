#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While / For
#2. Faça um programa que o usuário digite quantos números quiser, ate que digite sair. Retorne a soma e a média dos números digitados.

soma_numeros = 0
contador = 0

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")

    if entrada == 'sair':
        break

    numero = float(entrada)
    soma_numeros += numero
    contador += 1

if contador > 0:
    media = soma_numeros / contador
    print("A soma dos números é: ", soma_numeros)
    print("A média dos números é: ", media)
else:
    print("Nenhum número foi digitado.")


