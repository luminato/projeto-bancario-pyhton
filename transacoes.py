class Transacoes:
    def __init__(self, conta):
        self.conta = conta
        self.limite_saque = 500
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.conta['saldo'] += valor
            self.conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDeposito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
        

    def sacar(self, valor):

        if valor > self.conta['saldo']:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > self.limite_saque:
            print("Operação falhou! O valor do saque excede o limite.")

        elif self.conta['saques'] >= self.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.conta['saldo'] -= valor
            self.conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
            self.conta['saques'] += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")



    def extrair_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.conta['extrato'] else self.conta['extrato'])
        print(f"\nSaldo: R$ {self.conta['saldo']:.2f}")
        print("==========================================")
