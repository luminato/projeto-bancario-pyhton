def inicio():
    boas_vindas = """
------------------------------------------------------------
Bem vindo(a)! acesse sua conta ou digite [0] para finalizar:

[1] Cadastrar usuario
[2] Cadastrar conta
[3] Listar contas
[4] Acessar conta
[0] Sair
------------------------------------------------------------
    => """
    return input(boas_vindas)

def menu():
    menu = """
------------------------------------------------------
Escolha uma opção para continuar ou [0] para finalizar:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Volta para o inicio
[0] finalizar
------------------------------------------------------

=>  """
    return input(menu)

def confirmar():
    confirmacao = """
Aperte qualquer tecla para continuar ou [0] para finalizar.
=>  """
    return input(confirmacao)


def depositar(valor, usuario):
    if valor > 0:
        usuario['saldo'] += valor
        usuario['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDeposito de R$ {valor:.2f} realizado com sucesso!")
        return usuario

    print("Operação falhou! O valor informado é inválido.")


def sacar(valor, numero_saques,limite, LIMITE_SAQUES, usuario):

    if valor > usuario['saldo']:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        usuario['saldo'] -= valor
        usuario['extrato'] += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        return usuario, numero_saques

    print("Operação falhou! O valor informado é inválido.")



def extrair_extrato(*, usuario):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not usuario['extrato'] else usuario['extrato'])
    print(f"\nSaldo: R$ {usuario['saldo']:.2f}")
    print("==========================================")


def criar_usuario(cpf, usuarios):
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\noperação inválida!! usuario Já existe!")
        return False

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    saldo = 0
    extrato = ""

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "saldo" : saldo, "extrato": extrato})

    print("=== Usuário criado com sucesso! ===")
    return True


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios, cpf=""):
    if cpf == "":
        cpf = input("Informe o CPF do usuário: ")
    
    usuario = filtrar_usuario(cpf, usuarios)
    numero_conta+=1

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    if len(contas) > 0:
        for conta in contas:
            linha = f"""\
    Agência:{conta['agencia']}
    C/C:    {conta['numero_conta']}
    Titular:{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(linha)
    else:
        print("nenhuma conta para exibir!")


def acessar_conta(cpf, usuarios):
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        return usuario
    

def atualizar_usuario(usuario, usuarios):
    for usuario_alvo in usuarios:
        if usuario_alvo['cpf'] == usuario['cpf']:
            usuario_alvo['saldo'] = usuario['saldo']
            usuario_alvo['extrato'] = usuario['extrato']


def main():

    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    menu_opcao = False

    usuarios = []
    contas = []
    usuario_logado = []


    while True:

        if menu_opcao:
            opcao = menu()

            if opcao == "1":
                usuario_logado = depositar(float(input("\nInforme o valor do depósito: ")), usuario_logado)
                atualizar_usuario(usuario_logado, usuarios)

            elif opcao == "2":
                usuario_logado, numero_saques = sacar(float(input("\nInforme o valor do saque: ")), numero_saques,limite, LIMITE_SAQUES, usuario_logado)
                atualizar_usuario(usuario_logado, usuarios)

            elif opcao == "3":
                extrair_extrato(usuario=usuario_logado)
                if confirmar() == "0":
                    print("Finalizando...".center(40, "-"))
                    break
                else:
                    continue
                        

            elif opcao == "4":
                usuario_logado = []
                menu_opcao = False

            elif opcao == "0":
                print("Finalizando...".center(40, "-"))
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

        else:
            opcao_inicio = inicio()
            quantidade_conta = len(contas)

            if opcao_inicio == "1":
                cpf = input("Informe o CPF (somente número): ")
                if criar_usuario(cpf, usuarios):
                    conta = criar_conta(AGENCIA, quantidade_conta, usuarios, cpf)
                    contas.append(conta)

            elif opcao_inicio == "2":
                conta = criar_conta(AGENCIA, quantidade_conta, usuarios)
                if conta:
                    contas.append(conta)

            elif opcao_inicio == "3":
                listar_contas(contas)

            elif opcao_inicio == "4":
                cpf = input("Digite o cpf do usuario:")
                usuario_logado = acessar_conta(cpf, usuarios)
                if usuario_logado:
                    menu_opcao = True
                else:
                    print("usuario inválido, tente novamente!")

            else:
                print("Finalizando...".center(40, "-"))
                break
                
main()

