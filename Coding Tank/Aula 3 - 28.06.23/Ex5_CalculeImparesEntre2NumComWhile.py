#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While / For
#5. Pergunte o usuário 2 números inteiros, calcule a soma de todos os números ímpares inteiros entre esses números. Exemplo: se ele digitar 1 e 9, tem 5 números ímpares entre esses números 1,3,5,7,9, e a soma é 25 .

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

inicio = min(num1, num2)
fim = max(num1, num2)

contador = inicio
soma_impares = 0

while contador <= fim:
    if contador % 2 != 0:
        soma_impares += contador
    contador += 1

print("Soma dos números ímpares entre {} e {}: {}".format(inicio, fim, soma_impares))
