#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 2 - 27/06/23
#If-Else
#8) Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo. Faça um programa que peça para o usuário digitar o valor do produto de acordo com o preço antigo e escreva uma das mensagens da Tabela 2, de acordo com o preço reajustado:
#    "Tabela 1\n",
#    "\n",
#    "| Preço Antigo         | % de aumento |\n",
#    "|----------------------|--------------|\n",
#    "| Até 50 reais         | 5%           |\n",
#    "| Entre 50 e 100 reais | 10%          |\n",
#    "| De 100 a 150 reais   | 13%          |\n",
#    "| Acima de 150 reais   | 15%          |\n",
#    "\n",
#    "Tabela 2\n",
#    "\n",
#    "| Preço Novo            | Mensagem   |\n",
#    "|-----------------------|------------|\n",
#    "| Até 80 reais          | Barato     |\n",
#    "| Entre 80 e 115 reais  | Razoável   |\n",
#    "| Entre 115 e 150 reais | Normal     |\n",
#    "| Entre 150 e 170 reais | Caro       |\n",
#    "| Acima de 170 reais    | Muito Caro |"
	
print("Tabela 1")
print("| Preço Antigo         | % de aumento |")
print("|----------------------|--------------|")
print("| Até 50 reais         | 5%           |")
print("| Entre 50 e 100 reais | 10%          |")
print("| De 100 a 150 reais   | 13%          |")
print("| Acima de 150 reais   | 15%          |\n")

print("Tabela 2")
print("| Preço Novo            | Mensagem   |")
print("|-----------------------|------------|")
print("| Até 80 reais          | Barato     |")
print("| Entre 80 e 115 reais  | Razoável   |")
print("| Entre 115 e 150 reais | Normal     |")
print("| Entre 150 e 170 reais | Caro       |")
print("| Acima de 170 reais    | Muito Caro |\n")

preco_antigo = float(input("Digite o valor do produto (em reais): "))

if preco_antigo <= 50:
    aumento = 5
elif preco_antigo <= 100:
    aumento = 10
elif preco_antigo <= 150:
    aumento = 13
else:
    aumento = 15

preco_novo = preco_antigo + (preco_antigo * aumento / 100)

print("O preço anterior do produto era de R$", preco_antigo)
print("O preço reajustado do produto é de R$", preco_novo)

print("Mensagem: O preço do produto é ")
if preco_novo <= 80:
    print("Barato")
elif preco_novo <= 115:
    print("Razoável")
elif preco_novo <= 150:
    print("Normal")
elif preco_novo <= 170:
    print("Caro")
else:
    print("Muito Caro")