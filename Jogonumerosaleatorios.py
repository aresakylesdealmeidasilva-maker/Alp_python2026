import random

dif = int(input("""---Jogo da adivinhação---

Escolha uma dificuldade:
1.Normal(1 à 10)
2.Dificil (1 à 20)
3.Muito Dificil (1 à 30)

Digite uma dificuldade (1/2/3): """))

if dif == 1:
  al_num = random.randint(1,10)
  quant = 0
  while quant < 3:
    num = int(input("Digite um número: "))
    quant += 1
    if num == al_num:
       print("Parabéns você acertou!")
       break
    elif quant == 3:
       print("Você perdeu! Fim de jogo.")
    elif num < al_num:
       print("Você errou! Tente um número maior.")
    elif num > al_num:
       print("Você errou! Tente um número menor.")

elif dif == 2:
  al_num = random.randint(1,20)
  quant = 0
  while quant < 5:
    num = int(input("Digite um número: "))
    quant += 1
    if num == al_num:
       print("Parabéns você acertou!")
       break
    elif quant == 5:
       print("Você perdeu! Fim de jogo.")
    elif num < al_num:
       print("Você errou! Tente um número maior.")
    elif num > al_num:
       print("Você errou! Tente um número menor.")

elif dif == 3:
  al_num = random.randit(1,30)
  quant = 0
  while quant < 7:
    num = int(input("Digite um número: "))
    quant += 1
    if num == al_num:
       print("Parabéns você acertou!")
       break
    elif quant == 7:
       print("Você perdeu! Fim de jogo.")
    elif num < al_num:
       print("Você errou. Tente um número maior.")
    elif num > al_num:
       print("Você errou. Tente um número menor.")
else:
   print("Dificuldade inválida")
