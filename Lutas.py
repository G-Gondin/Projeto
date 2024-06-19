import random, time, lut

xp_player = 0
level = 1
x = xp_level = cont = 0
points_level = 10
classes = [{"classe": "Guerreiro", "vitalidade": 11, "força": 13, "destreza": 13, "resistencia": 11},
      {"classe": "Cavaleiro", "vitalidade": 14, "força": 11, "destreza": 11, "resistencia": 10},
      {"classe": "Andarilho", "vitalidade": 10, "força": 10, "destreza": 14, "resistencia": 12}]
mobs = [{"mob": "Guerreiro zombi", "vitalidade": 12, "força": 15, "destreza": 10, "resistencia": 9, "xp": 10},
        {"mob": "Zombi", "vitalidade": 8, "força": 7, "destreza": 5, "resistencia": 5, "xp": 8},
        {"mob": "Esqueleto", "vitalidade": 7, "força": 5, "destreza": 6, "resistencia": 3, "xp": 7}]

#lutas do inicio
while True:
    cont += 1
    if x == 0: 
        #seleção da classe do pl
        while True:
            selection_class = str(input("""[1] guerreiro
[2] cavaleiro
[3] andarilho
Selecione sua classe: """)).strip()
            if selection_class not in "123":
                while selection_class not in "123" or selection_class == "":
                    selection_class = str(input("Erro, digite novamente: ")).strip()
            if selection_class == "1":
                time.sleep(0.8)
                lut.linha()
                print(f"Seu nível é {level}")
                for k, v in classes[0].items():
                    print(f"A {k} é {v}")
                lut.linha()
                time.sleep(0.8)
                confirmation = str(input("Tem certeza? [S/N] ")).strip().upper()
                if confirmation not in "SN":
                    while confirmation not in "SN":
                        confirmation = str(input("Erro, digite novamente: ")).strip().upper()
                if confirmation == "S":
                    class_player = classes[0]
                    break
            if selection_class == "2":
                time.sleep(0.8)
                lut.linha()
                print(f"Seu nível é {level}")
                for k, v in classes[1].items():
                    print(f"A {k} é {v}")
                lut.linha()
                time.sleep(0.8)
                confirmation = str(input("Tem certeza? [S/N] ")).strip().upper()
                if confirmation not in "SN":
                    while confirmation not in "SN":
                        confirmation = str(input("Erro, digite novamente: ")).strip().upper()
                if confirmation == "S":
                    class_player = classes[1]
                    break
            if selection_class == "3":
                time.sleep(0.8)
                lut.linha()
                print(f"Seu nível é {level}")
                for k, v in classes[2].items():
                    print(f"A {k} é {v}")
                lut.linha()
                time.sleep(0.8)
                confirmation = str(input("Tem certeza? [S/N] ")).strip().upper()
                if confirmation not in "SN":
                    while confirmation not in "SN":
                        confirmation = str(input("Erro, digite novamente: ")).strip().upper()
                if confirmation == "S":
                    class_player = classes[2]
                    break 
    
    #subir de nível
    if x >= 1:
        if xp_player >= points_level:
            n2 = str(input("""Subiu de nível!
[1] vitalidade
[2] força
[3] destreza
[4] resistência
Adicionar pontos em qual deles? """)).strip()
            if n2 not in "1234":
                while n2 not in "1234" or n2 == "":
                    n2 = str(input("Erro, digite novamente: ")).strip()
            if n2 == '1':
                class_player["vitalidade"] += 1
                print(class_player["vitalidade"])
                points_level += points_level*0.4
            if n2 == '2':
                class_player["força"] += 1
                print(class_player["força"])
                points_level += points_level*0.4
            if n2 == '3':
                class_player["destreza"] += 1
                print(class_player["destreza"])
                points_level += points_level*0.4
            if n2 == '4':
                class_player["resistencia"] += 1
                print(class_player["resistencia"])
                points_level += points_level*0.4
        else:
            print(f"Falta {points_level-xp_player} pontos de xp para subir de nível.")

    attack_monster = attackforce_monster = defenseforce_monster = 0
    attack_player = attackforce_player = defenseforce_player = 0

    strength_player = class_player['força']
    dexterity_player = class_player['destreza']


    chosen_mob = random.choice(mobs)
    xp_monster = 0
    if cont % 5 == 0:
        xp_level += 3
    xp_monster = chosen_mob["xp"] + xp_level
    
    strength_monster = chosen_mob['força']
    dexterity_monster = chosen_mob['destreza']

    hp_player = class_player["vitalidade"] * 5
    defense_palyer = class_player["resistencia"] + ((class_player["resistencia"]/2) * (class_player["vitalidade"]/4))


    hp_monster = chosen_mob["vitalidade"] * 5
    defense_monster = chosen_mob["resistencia"] + ((chosen_mob["resistencia"]/2) * (chosen_mob["vitalidade"]/4))
    count_round = defeated = 0

    #luta em si
    while True:
        if count_round == 0:
            print(f"""
analise da batalha, você escolheu a classe: {class_player['classe']}, seus statos são:
            vitalidade: {class_player['vitalidade']};
            força: {class_player['força']};
            destreza: {class_player['destreza']};
            resistencia: {class_player['resistencia']}.

            Seu HP é de {hp_player} pontos;
            E sua defesa é de {defense_palyer:.2f} pontos
""")
            time.sleep(2)
            print(f"""analise da batalha, o mob selecionado foi: {chosen_mob['mob']}, seus statos são:
            vitalidade: {chosen_mob['vitalidade']};
            força: {chosen_mob['força']};
            destreza: {chosen_mob['destreza']};
            resistencia: {chosen_mob['resistencia']}.

            Seu HP é de {hp_monster} pontos;
            E sua defesa é de {defense_monster:.2f} pontos
""")
            progress_to_battle = str(input("Tendo isso em mente, deseja prosseguir com a batalha? [S/N]")).strip().upper()
            if progress_to_battle not in "SN":
                while progress_to_battle not in "SN":
                    progress_to_battle = str(input("Erro, digite novamente: ")).strip().upper()
            if progress_to_battle == "N":
                lut.sorteio()
                if defeated >= 1:
                    break
        count_round += 1
        print()
        print(f"Rodada {count_round}")
        dice_player = random.randint(1, 5)
        dice_monster = random.randint(1, 5)
        dice_master = random.randint(1, 5)
        print("Rolando dados")
        time.sleep(0.5)
        print(f"""Dado do jogador: {dice_player}
Dado do monstro: {dice_monster}
Dado do mestre: {dice_master}
""")

        # definição de ataque player
        if dice_player == dice_master:
            attack_player = strength_player + dexterity_player
        else:
            if dice_player > dice_master:
                attack_player = (strength_player / 2) + dexterity_player
            if dice_player < dice_master:
                attack_player = (strength_player / 2) + (dexterity_player / 2)

        # definição da força de ataque player
        if dice_player == dice_monster:
            attackforce_player = attack_player
        else:
            if dice_player > dice_monster:
                attackforce_player = attack_player * 1.5
            if dice_player < dice_monster:
                attackforce_player = attack_player * 0.75

        # definição da força de defesa player
        if dice_master == dice_player:
            defenseforce_player = defense_palyer * 0.75
        else:
            if dice_master > dice_player:
                defenseforce_player = defense_palyer * 0.5
            if dice_master < dice_player:
                defenseforce_player = defense_palyer
        
        lut.linha()
        print(f"Seu ataque vale {attack_player}")
        print(f"Sua força de ataque vale {attackforce_player}")
        print(f"Sua defesa vale {defense_palyer}")
        print(f"Sua força de defesa vale {defenseforce_player}")
        lut.linha()
        print("")

        # definição do ataque monstro
        if dice_monster == dice_master:
            attack_monster = strength_monster + dexterity_monster
        else:
            if dice_monster > dice_master:
                attack_monster = (strength_monster / 2) + dexterity_monster
            if dice_monster < dice_master:
                attack_monster = (strength_monster / 2) + (dexterity_monster / 2)

        # definição da força de ataque monstro
        if dice_monster == dice_player:
            attackforce_monster = attack_monster
        else:
            if dice_monster > dice_player:
                attackforce_monster = attack_monster * 1.5
            if dice_monster < dice_player:
                attackforce_monster = attack_monster * 0.75

        # definição da força de defesa monstro
        if dice_master == dice_monster:
            defenseforce_monster = defense_monster * 0.75
        else:
            if dice_master > dice_monster:
                defenseforce_monster = defense_monster * 0.5
            if dice_master < dice_monster:
                defenseforce_monster = defense_monster
        
        lut.linha()
        print(f"O ataque do mob vale {attack_monster}")
        print(f"A força de ataque do mob vale {attackforce_monster}")
        print(f"A defesa do mob vale {defense_monster}")
        print(f"A força de defesa do mob vale {defenseforce_monster}")
        lut.linha()

        attack_or_defend = str(input("""[1] atacar
[2] defender
qual a sua escolha? """)).strip()
        if attack_or_defend not in "12" or attack_or_defend == "":
            while attack_or_defend not in "12" or attack_or_defend == "":
                attack_or_defend = str(input("Erro, digite novamente: ")).upper().strip()
        if attack_or_defend == "1":
            if attackforce_player == defenseforce_monster:
                print("Nulo")
            else:
                if attackforce_player > defenseforce_monster:
                    damage = attackforce_player - defenseforce_monster
                    hp_monster -= damage
                    lut.linha()
                    print(f"Deu dano de {damage} pontos")
                    print(f"O HP do monstro foi de {hp_monster+damage} para {hp_monster}.")
                    lut.linha()
                    print()
                if attackforce_player < defenseforce_monster:
                    damage = defenseforce_monster - attackforce_player
                    hp_player -= damage
                    lut.linha()
                    print(f"Tomou dano de {damage} pontos")
                    print(f"O seu HP foi de {hp_player + damage} para {hp_player}.")
                    lut.linha()
                    print()
        if attack_or_defend == "2":
            if attackforce_monster == defenseforce_player:
                print("Nulo")
            else:
                if attackforce_monster > defenseforce_player:
                    damage = attackforce_monster - defenseforce_player
                    hp_player -= damage
                    lut.linha()
                    print(f"Tomou dano de {damage} pontos")
                    print(f"O seu HP foi de {hp_player + damage} para {hp_player}.")
                    lut.linha()
                    print()
                if attackforce_monster < defenseforce_player:
                    damage = defenseforce_player - attackforce_monster
                    hp_monster -= damage
                    lut.linha()
                    print(f"Deu dano de {damage} pontos")
                    print(f"O HP do monstro foi de {hp_monster+damage} para {hp_monster}.")
                    lut.linha()
                    print()
        if hp_player < 0:
            time.sleep(2)
            lut.linha()
            print("Você morreu")
            print(f"Restou um total de {hp_monster} de HP do mob.")
            print(f"Total de {count_round} rodadas")
            lut.linha()
            time.sleep(2)
            defeated += 1
            break
        if hp_monster < 0:
            time.sleep(2)
            lut.linha()
            print("Monstro derrotado")
            print(f"Te restou um total de {hp_player} de HP.")
            print(f"Total de {count_round} rodadas")
            lut.linha()
            time.sleep(1)
            x += 1
            xp_player += xp_monster
            print(f"Mais {chosen_mob['xp']} pontos de xp")
            print(f"Xp total de {xp_player}")
            lut.linha()
            time.sleep(2)
            break
    if defeated >= 1:
        break
print("Fim")
