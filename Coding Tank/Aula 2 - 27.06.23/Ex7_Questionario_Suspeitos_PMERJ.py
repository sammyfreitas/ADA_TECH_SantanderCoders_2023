#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 2 - 27/06/23
#If-Else
#7) Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:
#1. Mora perto da vítima?\n",
#2. Já trabalhou com a vítima?\n",
#3. Telefonou para a vítima?\n",
#4. Esteve no local do crime?\n",
#5. Devia para a vítima?\n",
#Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores iguais ou abaixo de 1 são liberados.

print("-----------------------")
print(" PMERJ - QUESTIONÁRIO")
print("-----------------------")
pontos = 0
resp1 = input("1. Mora perto da vítima? (s/n): ")
if resp1 == "s" or resp1 == "S":
    pontos += 1
elif resp1 != "n" and resp1 != "N":
    print("Resposta inválida!")

resp2 = input("2. Já trabalhou com a vítima? (s/n): ")
if resp2 == "s" or resp2 == "S":
    pontos += 1
elif resp2 != "n" and resp2 != "N":
    print("Resposta inválida!")

resp3 = input("3. Telefonou para a vítima? (s/n): ")
if resp3 == "s" or resp3 == "S":
    pontos += 1
elif resp3 != "n" and resp3 != "N":
    print("Resposta inválida!")

resp4 = input("4. Esteve no local do crime? (s/n): ")
if resp4 == "s" or resp4 == "S":
    pontos += 1
elif resp4 != "n" and resp4 != "N":
    print("Resposta inválida!")

resp5 = input("5. Devia para a vítima? (s/n): ")
if resp5 == "s" or resp5 == "S":
    pontos += 1
elif resp5 != "n" and resp5 != "N":
    print("Resposta inválida!")

if pontos == 5:
    print("O suspeito é considerado o assassino.")
elif pontos >= 3:
    print("O suspeito é considerado cúmplice.")
elif pontos == 2:
    print("O suspeito é apenas suspeito e necessita de outras investigações.")
else:
    print("O suspeito está liberado.")