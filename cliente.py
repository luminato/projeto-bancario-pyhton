class Clientes:
    def __init__(self):
        self.lista_clientes = []

    def adicionar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def listar_clientes(self):
        return self.lista_clientes

    def filtrar_usuario(self, cpf):
        for cliente in self.lista_clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def criar_cliente(self, cpf):
        if self.filtrar_usuario(cpf):
            print("CPF já cadastrado.")
            return False

        nome = input("Informe o nome: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        novo_cliente = Cliente(nome, cpf, data_nascimento, endereco)
        self.adicionar_cliente(novo_cliente)

        print("=== Cliente criado com sucesso! ===")
        return True


class Cliente:
    def __init__(self, nome, cpf, idade, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco