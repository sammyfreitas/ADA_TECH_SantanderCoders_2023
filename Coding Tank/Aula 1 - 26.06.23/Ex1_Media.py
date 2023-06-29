#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 1 - 26/06/23
#1. Imagine que você está implementando um sistema para verificar se os alunos de uma turma estudantil passaram na disciplina ou não. Para isso solicite que o usuário insira as notas das 4 provas realizadas por um estudante e calcule a média. Após isso, emita uma resposta booleana (True ou False) se o estudante passou na disciplina pensando que a média mínima para aprovação é que seja pelo menos 5.

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
nota4 = float(input("Digite a nota da quarta prova: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
resp = media >= 5
print(resp)