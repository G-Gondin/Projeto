import lut, time
level = 1
classes = [{"classe": "Guerreiro", "vitalidade": 11, "força": 13, "destreza": 13, "resistencia": 11},
        {"classe": "Cavaleiro", "vitalidade": 14, "força": 11, "destreza": 11, "resistencia": 10},
        {"classe": "Andarilho", "vitalidade": 10, "força": 10, "destreza": 14, "resistencia": 12}]
weapons = [{"elmo de aço": 2, "peitoral de aço": 4, "calça de aço": 3, "bota de aço": 2, "escudo de madeira": 3, "espada larga": 7},
        {"elmo nobre": 3, "peitoral nobre": 5, "calça nobre": 4, "bota nobre": 3, "escudo nobre": 4, "espada reta": 6},
        {"elmo de couro": 1, "casaco negro": 3, "calça negra": 2, "bota de couro": 1, "escudo de pele": 2, "espada curva": 5}]

lut.titulo("Selecione sua classe")
while True:
    print("""[1] Guerreiro
[2] Cavaleiro
[3] Andarilho""")
    n1 = str(input("Selecione a sua classe: ")).strip()
    if n1 not in "123" or n1 == "":
        while n1 not in "123" or n1 == "":
            n1 = str(input(lut.cor("Erro, digite novamente: ", "vermelho")))
    if n1 == "1":
        for k, v in (classes[0]).items():
            print(f"A {k} vale {v}.")
        confirmation = str(input("Deseja continuar com essa classe? [S/N]")).upper().strip()
        if confirmation not in "SN" or confirmation == "":
            while confirmation not in "SN" or confirmation == "":
                confirmation = str(input(lut.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
        if confirmation == "S":
            player_class = classes[0]
            break
    if n1 == "2":
        for k, v in (classes[1]).items():
            print(f"A {k} vale {v}.")
        confirmation = str(input("Deseja continuar com essa classe? [S/N]")).upper().strip()
        if confirmation not in "SN" or confirmation == "":
            while confirmation not in "SN" or confirmation == "":
                confirmation = str(input(lut.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
        if confirmation == "S":
            player_class = classes[1]
            break
    if n1 == "3":
        for k, v in (classes[2]).items():
            print(f"A {k} vale {v}.")
        confirmation = str(input("Deseja continuar com essa classe? [S/N]")).upper().strip()            
        if confirmation not in "SN" or confirmation == "":
            while confirmation not in "SN" or confirmation == "":
                confirmation = str(input(lut.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
        if confirmation == "S":
            player_class = classes[2]
            break




while True:
    print("""[1] Conjunto 1
[2] Conjunto 2
[3] Conjunto 3""")
    n2 = str(input("Selecione seu conjunto de equipamentos: ")).strip()
    if n2 not in "123" or n2 == "":
        while n2 not in "123" or n2 == "":
            n2 = str(input(lut.cor("Erro, digite novamente: ", "vermelho")))
    if n2 == "1":
        for k, v in weapons[0].items():
            print(f"O {k} vale {v}.")
        wconfirmation = str(input("Deseja continuar com essa classe? [S/N]")).upper().strip()
        if wconfirmation not in "SN" or wconfirmation == "":
            while wconfirmation not in "SN" or wconfirmation == "":
                wconfirmation = str(input(lut.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
        if wconfirmation == "S":
            player_weapons = weapons[0]
            break
    if n2 == "2":
        for k, v in weapons[1].items():
            print(f"O {k} vale {v}.")
        wconfirmation = str(input("Deseja continuar com essa classe? [S/N]")).upper().strip()
        if wconfirmation not in "SN" or wconfirmation == "":
            while wconfirmation not in "SN" or wconfirmation == "":
                wconfirmation = str(input(lut.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
        if wconfirmation == "S":
            player_weapons = weapons[1]
            break
    if n2 == "3":
        for k, v in weapons[2].items():
            print(f"O {k} vale {v}.")
        wconfirmation = str(input("Deseja continuar com essa classe? [S/N]")).upper().strip()
        if wconfirmation not in "SN" or wconfirmation == "":
            while wconfirmation not in "SN" or wconfirmation == "":
                wconfirmation = str(input(lut.cor("Erro, digite novamente: ", "vermelho"))).upper().strip()
        if wconfirmation == "S":
            player_weapons = weapons[2]
            break

print("Fim")
print("O seu set ficou da seguinte maneira:")
for k, v in player_class.items():
    print(f"A {k} vale {v}.")
print("Seus equipamentos são: ")
for k, v in player_weapons.items():
    print(f"O {k} vale {v}.")
