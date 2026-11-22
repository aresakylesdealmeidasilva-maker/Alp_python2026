usuarios = []

while True:
    print("\033c", end="")
    print(
        """##########################################
            SISTEMA DE
            CADASTRO DE
            USUÁRIOS
##########################################"""
    )

    print("===LOGIN===")
    usuario = input("Usuário: ").lower()
    senha = int(input("Senha: "))

    if usuario == "admin" and senha == 123:
        print(f"Login realizado com sucesso! Bem-vindo, {usuario}.")
        input("ENTER para continuar...")
        print("\033c", end="")

    else:
        input("Você errou. ENTER para tentar novamente...")
        print("\033c", end="")
        continue

    print(
        """##########################################
            SISTEMA DE
            CADASTRO DE
            USUÁRIOS
##########################################"""
    )

    print("=== MENU PRINCIPAL ===")
    print(f"Usuário logado: {usuario}")
    opcao = int(
        input(
            """1. Inserir usuário
2. Pesquisar usuário
3. Remover usuário
4. Listar todos os usuários
5. Logout
6. Encerrar

Escolha uma opção (1/2/3/4/5/6): """))

    if opcao == 1:
        while True:
            usuario = input("Digite o usuário que você quer inserir: ")
            usuarios.append(usuario)
            pergunta = input("Você deseja inserir mais um usuário?(S/N): ").upper()

            if pergunta == "S":
                continue

            elif pergunta == "N":
                input("Inserção encerrada! ENTER para encerrar o programa...")
                break

    elif opcao == 2:
        procurar = input("Qual usuário você deseja buscar?: ")

        if procurar in usuarios:
            print("Usuário encontrado.")
        else:
            print("Usuário não encontrado")
        input("ENTER para encerrar o programa... ")

    elif opcao == 3:
        remover = input("Qual usuário vc deseja remover?: ")

        if remover in usuarios:
            usuarios.remove(remover)
            print("Usuário removido com sucesso!")

        else:
            print("Este usuário não está cadastrado!")

        input("ENTER para encerrar o programa... ")

    elif opcao == 4:
        input("ENTER para imprimir a lista de usuários...")
        print("\033c", end="")

        for usuario in usuarios:
            print(usuario)

        input("ENTER para encerrar o programa... ")

    elif opcao == 5:
        print("Fazendo logout...")
        input("ENTER para voltar para o login")
        continue

    elif opcao == 6:
        print("Programa encerrado")
        break
