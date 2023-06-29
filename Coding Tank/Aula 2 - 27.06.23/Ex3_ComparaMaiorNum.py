#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 2 - 27/06/23
#If-Else
#3) Faça um programa que peça dois números e mostre o maior deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
  print(f"Os números {num1} e {num2} são iguais")