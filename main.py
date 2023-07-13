"Resolução de exercícios sobre instruções de controle com paradigma procidemental."
"By: Douglas"

def main():

    codigo = int(input("Digite o código do cliente:"))

    while codigo > 0:

        if codigo > 0:

            saldo = float(input("Digite o saldo inicial:"))

            cobrancas = float(input("Digite o total de cobranças:"))

            credito = float(input("Digite o total de créditos:"))

            limiteCredito = float(input("Digite o limite de crédito desse cliente:"))

            novoSaldo = saldo + cobrancas - credito

            if novoSaldo < limiteCredito:
                print(f"Conta: {codigo}\nLimite de crédito excedido!\n")
            else:
                print(f"Conta: {codigo}\nCrédito regular!\n")

        codigo = int(input("Digite o código do cliente:"))


if __name__:
    main()


