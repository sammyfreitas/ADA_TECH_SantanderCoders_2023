#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 2 - 27/06/23
#If-Else
#5) Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.
#Obs.: O aluno irá passar de ano se sua média for maior que 6.

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

if (media > 6):
    print("Aprovado, média = {:,.2f}".format(media))
else:
    print("Reprovado, média = {:,.2f}".format(media))