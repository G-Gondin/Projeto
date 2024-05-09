from random import randint, choice
from time import sleep
xpj = 0
nv = 1
x = xpn = cont = 0
pn = 10

cl = [{"classe": "Guerreiro", "vitalidade": 11, "força": 13, "destreza": 13, "resistencia": 11},
      {"classe": "Cavaleiro", "vitalidade": 14, "força": 11, "destreza": 11, "resistencia": 10},
      {"classe": "Andarilho", "vitalidade": 10, "força": 10, "destreza": 14, "resistencia": 12}]
mobs = [{"mob": "Guerreiro zombi", "vitalidade": 12, "força": 15, "destreza": 10, "resistencia": 9, "xp": 10},
        {"mob": "Zombi", "vitalidade": 8, "força": 7, "destreza": 5, "resistencia": 5, "xp": 8},
        {"mob": "Esqueleto", "vitalidade": 7, "força": 5, "destreza": 6, "resistencia": 3, "xp": 7}]
def sorteio():
    global d
    while True:
        ds = randint(1, 3)
        dsj = randint(1, 3)
        if dsj < ds:
            print("Você tenta fugir e recebeu um ataque covarde nas costas e morreu.")
            d += 1
            break
        if dsj > ds:
            print("Você se vira e consegue fugir dele, porém no meio do caminho encontra com outro monstro")
            break
def linha():
    print("-=-"*10)
#lutas do inicio
while True:
    cont += 1
    #seleção da classe do pl
    if x == 0: 
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
                linha()
                print(f"Seu nível é {nv}")
                for k, v in cl[0].items():
                    print(f"A {k} é {v}")
                linha()
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
                linha()
                print(f"Seu nível é {nv}")
                for k, v in cl[1].items():
                    print(f"A {k} é {v}")
                linha()
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
                linha()
                print(f"Seu nível é {nv}")
                for k, v in cl[2].items():
                    print(f"A {k} é {v}")
                linha()
                sleep(0.8)
                n1 = str(input("Tem certeza? [S/N] ")).strip().upper()
                if n1 not in "SN":
                    while n1 not in "SN":
                        n1 = str(input("Erro, digite novamente: ")).strip().upper()
                if n1 == "S":
                    cjg = cl[2]
                    break 
    
    #subir de nível
    if x >= 1:
        if xpj >= pn:
            n2 = str(input("""Subiu de nível!
[1] vitalidade
[2] força
[3] destreza
[4] resistência
Adicionar pontos em qual deles? """))
            if n2 not in "1234":
                while n2 not in "1234":
                    n2 = str(input("Erro, digite novamente: "))
            if n2 == '1':
                cjg["vitalidade"] += 1
                print(cjg["vitalidade"])
                pn += pn*0.4
            if n2 == '2':
                cjg["força"] += 1
                print(cjg["força"])
                pn += pn*0.4
            if n2 == '3':
                cjg["destreza"] += 1
                print(cjg["destreza"])
                pn += pn*0.4
            if n2 == '4':
                cjg["resistencia"] += 1
                print(cjg["resistencia"])
                pn += pn*0.4
        else:
            print(f"Falta {pn-xpj} pontos de xp para subir de nível.")

    atkm = fatkm = fdfm = 0
    atkp = fatkp = fdfp = 0

    forçp = cjg['força']
    dexp = cjg['destreza']


    mobu = choice(mobs)
    xpg = 0
    if cont % 5 == 0:
        xpn += 3
    xpg = mobu["xp"] + xpn
    forçm = mobu['força']
    dexm = mobu['destreza']


    hpj = cjg["vitalidade"] * 5
    dfj = cjg["resistencia"] + ((cjg["resistencia"]/2) * (cjg["vitalidade"]/4))


    hpm = mobu["vitalidade"] * 5
    dfm = mobu["resistencia"] + ((mobu["resistencia"]/2) * (mobu["vitalidade"]/4))
    c = d = 0

    #luta em si
    while True:
        if c == 0:
            print(f"""
analise da batalha, você escolheu a classe: {cjg['classe']}, seus statos são:
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
        print()
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
        
        linha()
        print(f"Seu ataque vale {atkp}")
        print(f"Sua força de ataque vale {fatkp}")
        print(f"Sua defesa vale {dfj}")
        print(f"Sua força de defesa vale {fdfp}")
        linha()
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
        if dm == dc:
            fdfm = dfm * 0.75
        else:
            if dm > dc:
                fdfm = dfm * 0.5
            if dm < dc:
                fdfm = dfm
        
        linha()
        print(f"O ataque do mob vale {atkm}")
        print(f"A força de ataque do mob vale {fatkm}")
        print(f"A defesa do mob vale {dfm}")
        print(f"A força de defesa do mob vale {fdfm}")
        linha()

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
                    linha()
                    print(f"Deu dano de {dn} pontos")
                    print(f"O HP do monstro foi de {hpm+dn} para {hpm}.")
                    linha()
                    print()
                if fatkp < fdfm:
                    dn = fdfm - fatkp
                    hpj -= dn
                    linha()
                    print(f"Tomou dano de {dn} pontos")
                    print(f"O seu HP foi de {hpj + dn} para {hpj}.")
                    linha()
                    print()
        if atkdef == "2":
            if fatkm == fdfp:
                print("Nulo")
            else:
                if fatkm > fdfp:
                    dn = fatkm - fdfp
                    hpj -= dn
                    linha()
                    print(f"Tomou dano de {dn} pontos")
                    print(f"O seu HP foi de {hpj + dn} para {hpj}.")
                    linha()
                    print()
                if fatkm < fdfp:
                    dn = fdfp - fatkm
                    hpm -= dn
                    linha()
                    print(f"Deu dano de {dn} pontos")
                    print(f"O HP do monstro foi de {hpm+dn} para {hpm}.")
                    linha()
                    print()
        if hpj < 0:
            sleep(2)
            linha()
            print("Você morreu")
            print(f"Restou um total de {hpm} de HP do mob.")
            print(f"Total de {c} rodadas")
            linha()
            sleep(2)
            d += 1
            break
        if hpm < 0:
            sleep(2)
            linha()
            print("Monstro derrotado")
            print(f"Te restou um total de {hpj} de HP.")
            print(f"Total de {c} rodadas")
            linha()
            sleep(1)
            x += 1
            xpj += xpg
            print(f"Mais {mobu['xp']} pontos de xp")
            print(f"Xp total de {xpj}")
            linha()
            sleep(2)
            break
    if d >= 1:
        break
print("Fim")
