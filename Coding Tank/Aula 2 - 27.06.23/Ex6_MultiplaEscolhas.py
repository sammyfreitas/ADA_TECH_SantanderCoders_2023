#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 2 - 27/06/23
#If-Else
#6) Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e).
#Sabendo a resposta certa, o programa deve receber a opção do usuário e informar a letra que o usuário marcou e se a resposta está certa ou errada.

print("Qual é o melhor time e mais querido do Brasil?")
opcao = input("a) Flamengo\nb) Corinthians\nc) Bahia\nd) Grêmio\ne) Atlético Mineiro\n")
resposta = "a"

if opcao == resposta:
    print("Você acertou! O melhor e mais querido time do Brasil é o Flamengo.")
elif opcao in ['b', 'c', 'd', 'e', 'B', 'C','D', 'E']:
    print("Você errou! A resposta correta é a letra (", resposta + " ) Flamengo.")
else:
    print("Opção inválida.")