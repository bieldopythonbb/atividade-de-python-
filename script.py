def somar(a, b):

    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):

    if b == 0:
        return "Erro: Divisão por zero não é permitida"
    return a / b

while True:
    print("\n" + "=" * 30)
    print("      Calculadora interativa")
    print("=" * 30)
    print("[1] somar")
    print("[2] subtrair")
    print("[3] multiplicar")
    print("[4] dividir")
    print("[5] sair")
    print("=" * 30)

    opcao = input("Escolha uma opção (1-5): ").strip()

    if opcao == "5":
        print("Obrigado por usar a calculadora")
        break
    elif opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("\nErro: Por favor, digite apenas valores numéricos válidos.")
            continue

        if opcao == "1":
            resultado = somar(num1, num2)
            print(f"\nResultado: {num1} + {num2} = {resultado}")

        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print(f"\nResultado: {num1} - {num2} = {resultado}")

        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            print(f"\nResultado: {num1} * {num2} = {resultado}")

        elif opcao == "4":
            resultado = dividir(num1, num2)
            if isinstance(resultado, str):
                print(f"\n{resultado}")
            else:
                print(f"\nResultado: {num1} / {num2} = {resultado}")

    else:
        print("\nOpção inválida! Escolha um número de 1 a 5.")