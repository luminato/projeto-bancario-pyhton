from cliente import Clientes
from menus import Menu
from conta import *
from transacoes import Transacoes

class Banco:
    def __init__(self):
        self.clientes = Clientes()
        self.contas = Contas()
        self.usuario_logado = None
        self.menu_opcao = False

    def criar_conta(self, cpf):
        self.conta = Conta(self.clientes, self.contas) 
        conta_criada = self.conta.criar_conta(cpf=cpf)
        print(conta_criada)
        if conta_criada:
            self.contas.adicionar_conta(conta_criada)

    def listar_contas(self):
        self.contas.listar_contas()

    def acessar_conta(self, cpf):
        return self.contas.retornar_conta(cpf)
    
    def depositar(self, valor, conta):
        self.transacoes = Transacoes(conta)
        self.transacoes.depositar(valor)

    def sacar(self, valor, conta):
        self.transacoes = Transacoes(conta)
        self.transacoes.sacar(valor)

    def extrair_extrato(self, conta):
        self.transacoes = Transacoes(conta)
        self.transacoes.extrair_extrato()
    

    def main(self):
        
        while True:
            
            if self.menu_opcao:
                opcao = Menu.menu()

                if opcao == "1" and self.usuario_logado:
                    self.depositar(float(input("\nInforme o valor do depósito: ")), self.usuario_logado)

                elif opcao == "2" and self.usuario_logado:
                    self.sacar(float(input("\nInforme o valor do saque: ")), self.usuario_logado)

                elif opcao == "3" and self.usuario_logado:
                    self.extrair_extrato(self.usuario_logado)
                    if Menu.confirmar() == "0":
                        print("Finalizando...".center(40, "-"))
                        break
                    else:
                        continue
                            
                elif opcao == "4":
                    usuario_logado = []
                    self.menu_opcao = False

                elif opcao == "0":
                    print("Finalizando...".center(40, "-"))
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

            else:
                opcao_inicio = Menu.inicio()
                
                if opcao_inicio == "1":
                    cpf = input("Informe o CPF (somente número): ")
                    self.clientes.criar_cliente(cpf)
                    self.criar_conta(cpf)

                elif opcao_inicio == "2":
                    cpf = input("Informe o CPF (somente número): ")
                    self.criar_conta(cpf)

                elif opcao_inicio == "3":
                    self.listar_contas()

                elif opcao_inicio == "4":
                    cpf = input("Informe o CPF (somente número): ")
                    self.usuario_logado = self.acessar_conta(cpf)
                    if self.usuario_logado:
                        self.menu_opcao = True
                    else:
                        print("usuario inválido, tente novamente!")

                else:
                    print("Finalizando...".center(40, "-"))
                    break
                    
if __name__ == "__main__":
    banco = Banco()
    banco.main()

