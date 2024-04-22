

class Contas:
    def __init__(self):
        self.lista_contas = []

    def adicionar_conta(self,/, conta):
        self.lista_contas.append(conta)

    
    def retornar_conta(self, cpf):
        for conta in self.lista_contas:
            if conta['usuario']['cpf'] == cpf:
                return conta
        return None
    
    def quantidade_contas(self):
        return len(self.lista_contas)
    
    def listar_contas(self):
        if self.quantidade_contas() > 0:
            for conta in self.lista_contas:
                linha = f"""\
    Agência:{conta['agencia']}
    C/C:    {conta['numero_conta']}
    Titular:{conta['usuario']['nome']}
            """
                print("=" * 100)
                print(linha)
        else:
            print("nenhuma conta para exibir!")
    


class Conta:
    def __init__(self, clientes, contas):
        self.clientes = clientes
        self.contas = contas
        self.agencia = "0001"
        self.usuario = None
        self.saldo = 0
        self.saques = 0
        self.extrato= ""

    def exibir_info(self):
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Titular: {self.usuario.nome}")

    def criar_conta(self, cpf):
        usuario = self.clientes.filtrar_usuario(cpf)
        numero_conta = self.contas.quantidade_contas()+1

        if usuario:
            print("\n=== Conta criada com sucesso! ===")
            return {"agencia": self.agencia, "numero_conta": numero_conta, "usuario": usuario.__dict__.copy(), "saldo": self.saldo, "saques" : self.saques, "extrato": self.extrato}
        else:
            print("Erro ao criar nova conta. Usuário não encontrado!")
            return None
        
