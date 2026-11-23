palavra = "PYTHON"

letras_corretas = ["_" for _ in palavra]
letras_utilizadas = []

erros = 0
limite_de_erros = 6


while erros < limite_de_erros and "_" in letras_corretas:

    print("\033c", end="")

    print("=" * 35)
    print("Jogo da Forca")
    print("=" * 35)

    print("\nPalavra:", end ="")

    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")


    print(f"Você ainda tem, {limite_de_erros} tentativas")


    letra = input("Digite uma letra: ").upper()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma única letra.")
        input("ENTER para continuar...")
        continue


    elif letra in letras_utilizadas or letra in letras_corretas:
        print(f"Você já tentou a letra '{letra}'. Tente outra letra!")
        input("ENTER para continuar...")
        continue


    elif letra in palavra:
        print(f"Você acertou uma letra")

        for i, caractere in enumerate(palavra):
            if letra == caractere:
                letras_corretas[i] = letra

    else:
        print("Você errou!")
        letras_utilizadas.append(letra)
        limite_de_erros -= 1


    print("Letras Erradas:", letras_utilizadas)

    input("ENTER para continuar..")


print("\n" + "=" *35)

if "_" not in letras_corretas:
    print("Parabéns! Você venceu!")
else:
    print(f"Fim de jogo! Suas tentativas acabaram.")

print(f"A palavra secreta era: {palavra}")

print("=" * 35)
