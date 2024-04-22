class Menu:
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