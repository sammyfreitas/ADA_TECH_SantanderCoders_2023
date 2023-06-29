#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While / For
#3. Usando laço, pergunte um usuário a nota de 3 provas. Remova a menor nota e calcule a média das notas que ele atingiu.

contador = 0
notas = []

while contador < 3:
    nota = float(input("Digite a nota da prova {}: ".format(contador + 1)))
    notas.append(nota)
    contador += 1

# Remover a menor nota
min_nota = min(notas)
notas.remove(min_nota)

# Calcular a média das notas restantes
media = sum(notas) / len(notas)

print("Média das notas: {:.2f}".format(media))


