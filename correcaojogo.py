import random

tent = 0
jogar = "s"
while jogar == "s":
  print("\033c", end=" ")
  dif = int(input("""--- JOGO DA ADIVINHAÇÃO ---
1. Médio (1 à 10)
2. Difícil (1 à 20)
3. Muito Difícil (1 à 30)

Escolha uma dificuldade (1/2/3): """))

  if dif == 1:
    limite = 10
  elif dif == 2:
    limite = 20
  elif dif == 3:
    limite = 30
  else:
    input("Opção inválida! ENTER para voltar ao menu de seleção...")
    continue

  print("--- JOGO DA ADIVINHAÇÃO ---")
  
  al_num = random.randint(1,limite)
  while tent < 3:
    num = int(input(f"Digite um número entre 1 e {limite}: "))
    tent += 1
    if num == al_num:
      print("Parabéns! Você acertou.")
      break
    elif tent == 3:
      print("Você perdeu! Fim de jogo")
      print(f"O número sorteado era: {al_num}")
      
    elif num > al_num:
      print(f"Você errou! Tente um número menor")
    elif num < al_num:
      print("Você errou! Tente um número maior")
    
  jogar = input("Deseja jogar novamente? (s/n):  "). lower()