from IPython.display  import clear_output
#Para funcionar no colab utilizamos essa linha de código#

quant = 0
while True:

  print("""#########################################
       SISTEMA DE CADASTRO DE USUÁRIOS
#########################################""")
  
  print("===LOGIN===")
  usuario = input("Usuário: ")
  senha = int(input("Senha: "))
  quant += 1
  if usuario == "admin" and senha == 123:
     print("Login realizado com sucesso! Bem-vindo, admin.")
     input("ENTER para continuar...")
     clear_output()
     
  
  elif usuario != "admin" and senha != 123:
     print("Você errou. Tente novamente")
  elif quant == 5:
     print("Você atingiu o limite de erros, tente novamente mais tarde")
     break

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
    clear_output()
    continue
  
  elif opcao == 6:
    print("Programa encerrado")
    break
