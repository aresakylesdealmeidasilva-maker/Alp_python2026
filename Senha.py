tentativa = 0

while tentativa < 3:
  tentativa += 1
  usuario = input("Digite a usuário: ")
  senha = int(input("Digite a senha: "))
  if tentativa == 3:
     print("Você foi bloqueado! Vá até o caixa mais próximo para desbloquear o seu cadastro.")
  
  elif usuario == "Ares" and senha == 12345:
     print(f"Seja bem-vindo! {usuario}")
     break
  else:
     print("Senha ou Usuário incorretos! tente novamente.")