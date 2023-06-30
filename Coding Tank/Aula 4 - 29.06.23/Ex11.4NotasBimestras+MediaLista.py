#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 4 - 29/06/23
# Listas, Índices, Iterações de listas, Métodos de listas
#11. Faça um Programa que peça as 4 notas bimestrais e mostre a média, usando listas.

notas = []

for i in range(4):
    nota = float(input("Digite a nota do " + str(i+1) + "º bimestre: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Média final: {:.1f}".format(media))









