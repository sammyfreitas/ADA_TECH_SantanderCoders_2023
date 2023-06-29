#ADA TECH - SANTANDER CODERS - CODING TANK
#Aula 3 - 28/06/23
#Laços Repetição - While 
#Praticando
#6) Faça uma calculadora. O usuário deve inserir qual a operação matemática ele deseja realizar e logo em seguida os dois números. O programa deve finalizar apenas quando o usuário digitar a opção \"sair\" no momento de escolha da operação matemática.

while True:
    print("Opções da Calculadora:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "5":
        print("Encerrando a calculadora.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = num1 + num2
    elif opcao == "2":
        resultado = num1 - num2
    elif opcao == "3":
        resultado = num1 * num2
    elif opcao == "4":
        resultado = num1 / num2

    print("Resultado:", resultado)
