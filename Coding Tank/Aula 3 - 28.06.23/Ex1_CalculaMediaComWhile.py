#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While / For
#1. Pergunte um usuário quantas provas ele fez, depois pergunte a nota de todas as provas. Calcule a média e caso seja maior ou igual a 6 informe que ele está aprovado, se não reprovado.

num_provas = int(input("Quantas provas você fez? "))
soma_notas = 0
contador = 0

while contador < num_provas:
    nota = float(input("Digite a nota da prova {}: ".format(contador + 1)))
    soma_notas += nota
    contador += 1

media = soma_notas / num_provas

if media >= 6:
    print("Aprovado com média: {:.2f}".format(media))
else:
    print("Reprovado com média: {:.2f}".format(media))


