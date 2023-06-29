#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 2 - 27/06/23
#If-Else
#4) Faça um programa que leia a validade das informações:
#"a. Idade: entre 0 e 150;
#"b. Salário: maior que 0;
#"c. Sexo: M, F ou Outro;
#O programa deve imprimir uma mensagem de erro para cada informação inválida.
	
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))
sexo = input("Digite o sexo (M, F ou Outro): ")

if idade < 0 or idade > 150:
    print("Erro: Idade inválida.")
else:
    print(f"A idade {idade} é válida.")

if salario <= 0:
    print("Erro: Salário inválido.")
else:
    print(f"O salário {salario} é válido.")

if sexo == 'M':
    print("Sexo: Masculino")
elif sexo == 'F':
    print("Sexo: Feminino")
elif (sexo == 'Outro') or (sexo == 'outro'):
    print("Sexo: Outro")
else:
    print("Erro: Sexo inválido.")