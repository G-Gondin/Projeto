def titulo(n1):
    print("-" * 30)
    print("{:^30}".format(n1))
    print("-" * 30)

def cor(msg, cor="branco"):
    import colorama
    colorama.init()
    color = {
        "vermelho": colorama.Fore.RED,
        "verde": colorama.Fore.GREEN,
        "amarelo": colorama.Fore.YELLOW,
        "azul": colorama.Fore.BLUE,
        "preto": colorama.Fore.BLACK,
        "ciano": colorama.Fore.CYAN,
        "magenta": colorama.Fore.MAGENTA,
        "branco": colorama.Fore.WHITE,
        "reset": colorama.Fore.RESET}
    n1 = f"{color[f'{cor}']} {msg} {color['reset']}"
    return n1

def sorteio():
    from random import randint
    d = 0
    while True:
        dice_scape = randint(1, 6)
        dice_scape_player = randint(1, 6)
        if dice_scape_player < dice_scape:
            print(f"Dado de saida: {dice_scape}")
            print(f"Seu dado: {dice_scape_player}")
            print("Você tenta fugir e recebeu um ataque covarde nas costas e morreu.")
            d += 1
            break
        if dice_scape_player > dice_scape:
            print(f"Dado de saida: {dice_scape}")
            print(f"Seu dado: {dice_scape_player}")
            print("Você se vira e consegue fugir dele, porém no meio do caminho encontra com outro monstro")
            break
    return d

def linha():
    print("-=-"*10)

