class Cliente:
   
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class ContaBancaria:
    
    def __init__(self, cliente, numero_conta):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.limite = 500.0
        self.maximo_saques = 3

    def depositar(self, valor):
       
        
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito concluído com êxito!")
        else:
            print("Erro na operação! O valor inserido é inválido.")

    def sacar(self, valor):
       
        if valor > self.saldo:
            print("Erro na operação! Você não possui saldo suficiente.")
        elif valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif self.saques_realizados >= self.maximo_saques:
            print("Erro na operação! Limite de saques diários atingido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_realizados += 1
            print("Saque efetuado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        
        print("\n------------ EXTRATO -----------------")
        if not self.extrato:
            print("Nenhuma transação foi registrada.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("--------------------------------------")


def cadastrar_cliente():
    
    nome = input("Informe seu nome: ")
    cpf = input("Informe seu CPF: ")
    data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe seu endereço: ")
    return Cliente(nome, cpf, data_nascimento, endereco)


def cadastrar_conta(cliente):
    """
    Função para cadastrar uma nova conta bancária para o cliente.
    """
    numero_conta = input("Informe o número da conta: ")
    return ContaBancaria(cliente, numero_conta)


def mostrar_menu():
    """
    Exibe o menu de opções para o usuário e retorna a opção selecionada.
    """
    print("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    """)
    return input("Selecione uma das opções: ")


def iniciar_sistema():
    """
    inicia o sistema bancário.
    """
    print("Bem-vindo ao sistema bancário!")
    cliente = cadastrar_cliente()
    conta = cadastrar_conta(cliente)

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            valor = float(input("Por favor, insira o valor que deseja depositar: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Por favor, insira o valor que deseja sacar: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.exibir_extrato()
        elif opcao == "4":
            print("Agradecemos por usar nosso sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()