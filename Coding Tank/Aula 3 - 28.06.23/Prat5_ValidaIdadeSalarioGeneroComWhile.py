#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While 
#Praticando
#5) Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.
#a. Idade: entre 0 e 150  
#b. Salário: maior que 0  
#c. Gênero: M, F ou Outro  
#Por último imprima os dados recebidos do usuário.

idade = -1
salario = -1
genero = ""

while idade < 0 or idade > 150 or salario <= 0 or (genero not in ["M", "m", "F", "f", "Outro"]):
    idade = int(input("Digite a idade (entre 0 e 150): "))
    salario = float(input("Digite o salário (maior que 0): "))
    genero = input("Digite o gênero (M, F ou Outro): ")
    if (genero == "m") or (genero == "M"):
        genero = "Masculino"
    elif (genero == "f") or (genero == "F"):
        genero = "Feminino"
    elif (genero == "o") or (genero == "Outro"):
        genero = "Outro"
    else:
        genero=genero
    
    
print("\nDados do usuário:")
print("Idade:", idade)
print("Salário: R${:.2f}".format(salario))
print("Gênero:", genero)

