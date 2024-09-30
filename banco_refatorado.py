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

def fazer_deposito(saldo, extrato):
    """
    Função para realizar depósito na conta do usuário.
    """
    valor = float(input("Por favor, insira o valor que deseja depositar: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito concluído com êxito!")
    else:
        print("Erro na operação! O valor inserido é inválido.")
    return saldo, extrato

def fazer_saque(saldo, extrato, saques_realizados, limite, maximo_saques):
    """
    Função para realizar saque, validando saldo, limite e número de saques.
    """
    valor = float(input("Por favor, insira o valor que deseja sacar: "))

    if valor > saldo:
        print("Erro na operação! Você não possui saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif saques_realizados >= maximo_saques:
        print("Erro na operação! Limite de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_realizados += 1
        print("Saque efetuado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, saques_realizados

def mostrar_extrato(saldo, extrato):
    """
    Função para exibir o extrato da conta do usuário.
    """
    print("\n------------ EXTRATO -----------------")
    if not extrato:
        print("Nenhuma transação foi registrada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("--------------------------------------")

def cadastrar_usuario():
    """
    Função para cadastrar um novo usuário (cliente).
    """
    nome = input("Informe seu nome: ")
    cpf = input("Informe seu CPF: ")
    data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe seu endereço: ")
    return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}

def cadastrar_conta(usuario):
    """
    Função para cadastrar uma nova conta bancária para o usuário.
    """
    numero_conta = input("Informe o número da conta: ")
    return {"numero_conta": numero_conta, "usuario": usuario, "saldo": 0.0, "extrato": [], "saques_realizados": 0}

def iniciar_sistema():
    """
    Função principal que inicia o sistema bancário.
    """
    print("Bem-vindo ao sistema bancário!")
    cliente = cadastrar_usuario()
    conta = cadastrar_conta(cliente)

    limite = 500.0
    maximo_saques = 3

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            conta['saldo'], conta['extrato'] = fazer_deposito(conta['saldo'], conta['extrato'])
        elif opcao == "2":
            conta['saldo'], conta['extrato'], conta['saques_realizados'] = fazer_saque(
                conta['saldo'], conta['extrato'], conta['saques_realizados'], limite, maximo_saques
            )
        elif opcao == "3":
            mostrar_extrato(conta['saldo'], conta['extrato'])
        elif opcao == "4":
            print("Agradecemos por usar nosso sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()