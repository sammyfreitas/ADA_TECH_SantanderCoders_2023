#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 1 - 26/06/23
#2. Crie um algoritmo que calcule o IMC (índice de massa corporal). O IMC é calculado com a formula PESO/(ALTURA ^ 2). Para isso, coloque as informações nas variáveis e ao final apresente o resultado como no exemplo: "O IMC é 18"

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)
print("O IMC é {:.2f}".format(imc))