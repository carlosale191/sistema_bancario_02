from time import strftime, localtime

data_hora = strftime("%Y-%m-%d %H:%M:%S", localtime())

def consulta_saldo(saldo):
    print(f"Saldo atual de R${saldo:.2f}")

def depositar(saldo,extrato,/):
    deposito = float(input("Digite o valor do depósito: "))
    if deposito <= 0:
        print("Depósito inválido")
    else:
        saldo += deposito
        extrato.append(f"Depósito no valor de R${deposito:.2f} " + data_hora)
        print(f"Depósito de R${deposito:.2f} feito com sucesso. Saldo atual de R${saldo:.2f}")
    
    return saldo, extrato

def sacar(*,saldo, limite_saques, limite, extrato):
    if limite_saques <= 0:
        print("Limite de saques diário atingido")
        return saldo,limite_saques,limite,extrato

    saque = float(input("Digite o valor a ser sacado: "))

    if saldo < saque:
        if saque > limite:
            print("Saldo e limite insuficientes")
        else:
            limite -= saque
            limite_saques -= 1
            extrato.append(f"Saque no valor de R${saque:.2f} " + data_hora)
            print(f"Saque realizado no valor de R${saque:.2f}. Saldo atual de R${saldo:.2f} e limite atual de R${limite:.2f}")
    else:
        saldo -= saque
        limite_saques -= 1
        extrato.append(f"Saque no valor de R${saque:.2f} " + data_hora)
        print(f"Saque realizado no valor de R${saque:.2f}. Saldo atual de R${saldo:.2f}")

    return saldo,limite_saques,limite,extrato

def gerar_extrato(extrato):
    print("#### EXTRATO ####")
    if not extrato:
        print("Nenhuma movimentação registrada")
    else:
        for registro in extrato:
            print(registro)

def criar_usuario(usuarios):
    cpf = int(input("Informe seu CPF (somente números) "))
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("CPF já cadastrado!")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filt = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filt[0] if usuarios_filt else None
    #retorna o primeiro user encontrado caso operação dê certo

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)
    #verifica existência do usuário p/ poder criar conta
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado!")

def main():
    saldo = 0.0
    limite = 500.00
    limite_saques = 3
    extrato = []
    usuarios = []
    AGENCIA = "0001"
    MENU = """
        Bem vindo(a)! Selecione o comando de sua ação:

        [1] Consultar Saldo
        [2] Sacar
        [3] Depositar
        [4] Gerar extrato
        [5] Sair
    """

    while True:
        print(MENU)
        opc = int(input("Digite ação desejada: "))

        if opc == 1:
            consulta_saldo(saldo)
        elif opc == 2:
            saldo,limite_saques,limite,extrato = sacar(saldo=saldo,
                  limite_saques = limite_saques,
                  limite=limite,
                  extrato=extrato)
        elif opc == 3:
            saldo, extrato = depositar(saldo,extrato)
        elif opc == 4:
            gerar_extrato(extrato=extrato)
        elif opc == 5:
            print("Saindo...")
            break
        else:
            print("Comando inválido")

main()