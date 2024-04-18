menu = """
------------------------------------------------------
Escolha uma opção para continuar ou [0] para finalizar:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
------------------------------------------------------

=> """

confirmacao = """
Deseja continuar? [s] sim, [n] não
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito: "))
        print("\n")

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: "))
        print("\n")

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

        continuar = input(confirmacao)
        if continuar == "s":
            continue
        else:
            print("Finalizando...".center(40, "-"))
            break

    elif opcao == "0":
        print("Finalizando...".center(40, "-"))
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")