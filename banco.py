def mostrar_menu():
    print("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    """)
    return input("Selecione uma das opções: ")

def fazer_deposito(saldo, extrato):
    valor = float(input("Por favor, insira o valor que deseja depositar: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito concluído com êxito!")
    else:
        print("Erro na operação! O valor inserido é inválido.")
    return saldo, extrato

def fazer_saque(saldo, extrato, saques_realizados, limite, maximo_saques):
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
    print("\n------------ EXTRATO -----------------")
    if not extrato:
        print("Nenhuma transação foi registrada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("--------------------------------------")

def iniciar_sistema():
    saldo = 0.0
    limite = 500.0
    extrato = []
    saques_realizados = 0
    maximo_saques = 3

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            saldo, extrato = fazer_deposito(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, saques_realizados = fazer_saque(saldo, extrato, saques_realizados, limite, maximo_saques)
        elif opcao == "3":
            mostrar_extrato(saldo, extrato)
        elif opcao == "4":
            print("Agradecemos por usar nosso sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()