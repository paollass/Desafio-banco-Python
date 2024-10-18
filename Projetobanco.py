Nome_Cliente = input("Informe seu nome:")
print(f"Seja bem-vindo(a) ao nosso banco, {Nome_Cliente}!")
      

print(f"Escolha uma das opções abaixo:") 
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(f"{Nome_Cliente} , Esse valor de saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(f"\n{Nome_Cliente}, seu extrato atual é de:\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n{Nome_Cliente}, seu saldo atual é de R$ {saldo:.2f}")  # <-- Nova linha
        print("==========================================")
    
    elif opcao == "q":
        print(f"\n{Nome_Cliente}, Obrigada por usar nossos serviços, Até Mais!\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")