import random


def jogar():
    imprime_mensagem_abertura()
    arquivo_tema = tema_jogo()

    palavra_secreta = carrega_palavra_secreta(arquivo_tema)
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_chutadas = []

    while not enforcou and not acertou:
        print("Palavra: {}".format(letras_acertadas))
        print("Letras já tentadas: {}".format(letras_chutadas))

        chute = pede_chute(letras_chutadas)
        letras_chutadas.append(chute)

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def tema_jogo():
    print("Qual será o tema do jogo?")
    print("1. Animais")
    print("2. Frutas")
    print("3. Paises")
    tema = int(input("Digite o número: "))
    if tema == 1:
        return "animais.txt"
    if tema == 2:
        return "frutas.txt"
    if tema == 3:
        return "paises.txt"


def carrega_palavra_secreta(arquivo="frutas.txt"):
    with open(arquivo) as arquivo_palavras:
        palavras_secretas = []
        for linha in arquivo_palavras:
            linha = linha.strip()
            palavras_secretas.append(linha)
    posicao = random.randrange(0, len(palavras_secretas))
    palavra_secreta = palavras_secretas[posicao].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # List comprehension


def chute_valido(chute, letras_chutadas):
    tipo_chute_correto = chute.isalpha()  # Retorna True se o chute for uma letra do alfabeto.
    letra_unica = len(chute) == 1
    chute_repetido = chute in letras_chutadas

    if not tipo_chute_correto:
        print("Isso não é um letra, tente novamente:", end=" ")
    elif not letra_unica:
        print("Só é permitido digitar uma letra por vez, tente novamente:", end=" ")
    elif chute_repetido:
        print("Essa letra já foi digitada, tente novamente:", end=" ")

    return tipo_chute_correto and not chute_repetido and letra_unica


def pede_chute(letras_chutadas):
    chute = input("Digite uma letra: ").strip().upper()  # .strip() remove as sujeiras digitadas pelo usuário (como
    # espaços, caracteres especiais e afins)

    while not chute_valido(chute, letras_chutadas):
        chute = input().strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    jogar()
