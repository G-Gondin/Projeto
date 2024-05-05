from random import randint, choice
from time import sleep
cl = [{"classe": "Guerreiro", "vitalidade": 11, "força": 13, "destreza": 13, "resistencia": 11},
      {"classe": "Cavaleiro", "vitalidade": 14, "força": 11, "destreza": 11, "resistencia": 10},
      {"classe": "Andarilho", "vitalidade": 10, "força": 10, "destreza": 14, "resistencia": 12}]
mobs = [{"mob": "Guerreiro zombi", "vitalidade": 12, "força": 15, "destreza": 10, "resistencia": 9},
        {"mob": "Zombi", "vitalidade": 8, "força": 7, "destreza": 5, "resistencia": 5},
        {"mob": "Esqueleto", "vitalidade": 7, "força": 5, "destreza": 6, "resistencia": 3}]
def sorteio():
    global d
    while True:
        ds = randint(1,5)
        dsj = randint(1,5)
        if ds > dsj:
            print("Você tenta fugir e recebeu um ataque covarde nas costas e morreu.")
            d += 1
            break
        if dsj > dsj:
            print("Você se vira e consegue fugir dele, porém no meio do caminho encontra com outro monstro")
            break
#lutas do inicio
while True:
    #seleção da classe do pl
    while True:
        sc = str(input("""[1] guerreiro
[2] cavaleiro
[3] andarilho
Selecione sua classe: """))
        if sc not in "123":
            while sc not in "123":
                sc = str(input("Erro, digite novamente: "))
        if sc == "1":
            sleep(0.8)
            for k, v in cl[0].items():
                print(f"A {k} é {v}")
            sleep(0.8)
            n1 = str(input("Tem certeza? [S/N] ")).strip().upper()
            if n1 not in "SN":
                while n1 not in "SN":
                    n1 = str(input("Erro, digite novamente: ")).strip().upper()
            if n1 == "S":
                cjg = cl[0]
                break
        if sc == "2":
            sleep(0.8)
            for k, v in cl[1].items():
                print(f"A {k} é {v}")
            sleep(0.8)
            n1 = str(input("Tem certeza? [S/N] ")).strip().upper()
            if n1 not in "SN":
                while n1 not in "SN":
                    n1 = str(input("Erro, digite novamente: ")).strip().upper()
            if n1 == "S":
                cjg = cl[1]
                break
        if sc == "3":
            sleep(0.8)
            for k, v in cl[2].items():
                print(f"A {k} é {v}")
            sleep(0.8)
            n1 = str(input("Tem certeza? [S/N] ")).strip().upper()
            if n1 not in "SN":
                while n1 not in "SN":
                    n1 = str(input("Erro, digite novamente: ")).strip().upper()
            if n1 == "S":
                cjg = cl[2]
                break 
    atkm = fatkm = fdfm = 0
    atkp = fatkp = fdfp = 0

    forçp = cjg['força']
    dexp = cjg['destreza']


    mobu = choice(mobs)
    forçm = mobu['força']
    dexm = mobu['destreza']


    hpj = cjg["vitalidade"] * 5
    dfj = cjg["resistencia"] + ((cjg["resistencia"]/2) * (cjg["vitalidade"]/4))


    hpm = mobu["vitalidade"] * 5
    dfm = mobu["resistencia"] + ((mobu["resistencia"]/2) * (mobu["vitalidade"]/4))
    c = d =0

    #luta em si
    while True:
        if c == 0:
            print(f"""analise da batalha, você escolheu a classe: {cjg['classe']}, seus statos são:
            vitalidade: {cjg['vitalidade']};
            força: {cjg['força']};
            destreza: {cjg['destreza']};
            resistencia: {cjg['resistencia']}.

            Seu HP é de {hpj} pontos;
            E sua defesa é de {dfj:.2f} pontos
                            """)
            sleep(2)
            print(f"""analise da batalha, o mob selecionado foi: {mobu['mob']}, seus statos são:
            vitalidade: {mobu['vitalidade']};
            força: {mobu['força']};
            destreza: {mobu['destreza']};
            resistencia: {mobu['resistencia']}.

            Seu HP é de {hpm} pontos;
            E sua defesa é de {dfm:.2f} pontos
                        """)
            pb = str(input("Tendo isso em mente, deseja prosseguir com a batalha? [S/N]")).strip().upper()
            if pb not in "SN":
                while pb not in "SN":
                    pb = str(input("Erro, digite novamente: ")).strip().upper()
            if pb == "N":
                sorteio()
                if d >= 1:
                    break
        c += 1
        print(f"Rodada {c}")
        dj = randint(1, 5)
        dc = randint(1, 5)
        dm = randint(1, 5)
        print("Rolando dados")
        sleep(0.5)
        print(f"""Dado do jogador: {dj}
Dado do monstro: {dc}
Dado do mestre: {dm}
""")

        # definição de ataque player
        if dj == dm:
            atkp = forçp + dexp
        else:
            if dj > dm:
                atkp = (forçp / 2) + dexp
            if dj < dm:
                atkp = (forçp / 2) + (dexp / 2)

        # definição da força de ataque player
        if dj == dc:
            fatkp = atkp
        else:
            if dj > dc:
                fatkp = atkp * 1.5
            if dj < dc:
                fatkp = atkp * 0.75

        # definição da força de defesa player
        if dm == dj:
            fdfp = dfj * 0.75
        else:
            if dm > dj:
                fdfp = dfj * 0.5
            if dm < dj:
                fdfp = dfj
        print(f"Seu ataque vale {atkp}")
        print(f"Sua força de ataque vale {fatkp}")
        print(f"Sua defesa vale {dfj}")
        print(f"Sua força de defesa vale {fdfp}")
        print("")

        # definição do ataque monstro
        if dc == dm:
            atkm = forçm + dexm
        else:
            if dc > dm:
                atkm = (forçm / 2) + dexm
            if dc < dm:
                atkm = (forçm / 2) + (dexm / 2)

        # definição da força de ataque monstro
        if dc == dj:
            fatkm = atkm
        else:
            if dc > dj:
                fatkm = atkm * 1.5
            if dc < dj:
                fatkm = atkm * 0.75

        # definição da força de defesa monstro
        if dj == dc:
            fdfm = dfm * 0.75
        else:
            if dj > dm:
                fdfm = dfm * 0.5
            if dj < dm:
                fdfm = dfm

        print(f"O ataque do mob vale {atkm}")
        print(f"A força de ataque do mob vale {fatkm}")
        print(f"A defesa do mob vale {dfm}")
        print(f"A força de defesa do mob vale {fdfm}")

        atkdef = str(input("""[1] atacar
    [2] defender
    qual a sua escolha? """))
        if atkdef not in "12":
            while atkdef not in "12":
                atkdef = str(input("Erro, digite novamente: ")).upper().strip()
        if atkdef == "1":
            if fatkp == fdfm:
                print("Nulo")
            else:
                if fatkp > fdfm:
                    dn = fatkp - fdfm
                    hpm -= dn
                    print(f"Deu dano de {dn} pontos")
                    print(f"O HP do monstro foi de {hpm+dn} para {hpm}.")
                if fatkp < fdfm:
                    dn = fdfm - fatkp
                    hpj -= dn
                    print(f"Tomou dano de {dn} pontos")
                    print(f"O seu HP foi de {hpj + dn} para {hpj}.")
        if atkdef == "2":
            if fatkm == fdfp:
                print("Nulo")
            else:
                if fatkm > fdfp:
                    dn = fatkm - fdfp
                    hpj -= dn
                    print(f"Tomou dano de {dn} pontos")
                    print(f"O seu HP foi de {hpj + dn} para {hpj}.")
                if fatkm < fdfp:
                    dn = fdfp - fatkm
                    hpm -= dn
                    print(f"Deu dano de {dn} pontos")
                    print(f"O HP do monstro foi de {hpm+dn} para {hpm}.")
        if hpj < 0:
            print("Você morreu")
            print(f"Restou um total de {hpm} de HP do mob.")
            print(f"Total de {c} rodadas")
            d += 1
            break
        if hpm < 0:
            print("Monstro derrotado")
            print(f"Te restou um total de {hpj} de HP.")
            print(f"Total de {c} rodadas")
            break
    if d >= 1:
        break
    print("Fim")
