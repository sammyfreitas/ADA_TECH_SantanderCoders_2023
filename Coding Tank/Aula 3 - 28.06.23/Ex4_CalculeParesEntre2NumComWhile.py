#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While / For
#4. Pergunte o usuário 2 números inteiros, calcule quantos números pares existem entre os 2 número informados. Exemplo: se ele digitar 1 e 9, tem 4 números pares entre esses números 2,4,6,8.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

inicio = min(num1, num2)
fim = max(num1, num2)

contador = inicio
quantidade_pares = 0

while contador <= fim:
    if contador % 2 == 0:
        quantidade_pares += 1
    contador += 1

print("Quantidade de números pares entre {} e {}: {}".format(inicio, fim, quantidade_pares))
