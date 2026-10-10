while True:
  print("\033c", end=" ")
  print("""#########################################
       SISTEMA DE CADASTRO DE USUÁRIOS
#########################################""")

  print("===LOGIN===")
  usuario = input("Usuário: ")
  senha = int(input("Senha: "))
  if usuario == "admin" and senha == 123:
     print(f"Login realizado com sucesso! Bem-vindo, {usuario}.")
     input("ENTER para continuar...")
     print("\33c", end=" ")

  else:
     input("Você errou. ENTER para tentar novamente...")
     continue
     

  print("""#########################################
       SISTEMA DE CADASTRO DE USUÁRIOS
#########################################""")

  print("=== MENU PRINCIPAL ===")
  print(f"Usuário logado: {usuario}")
  opcao = int(input("""1. Inserir usuário 
2. Pesquisar usuário 
3. Remover usuário
4. Listar todos os usuários
5. Logout
6. Encerrar

Escolha uma opção (1/2/3/4/5/6): """))

  if opcao == 5:
    print("Fazendo logout...")
    input("ENTER para voltar para o login")
    continue

  elif opcao == 6:
    print("Programa encerrado")
    break