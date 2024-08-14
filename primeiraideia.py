# Importando a biblioteca Ren'Py
define e = Character("Eileen")

# Variáveis globais para acompanhar o estado do jogo
default story_value = 0
default choices = []
default event_sequence = []
default turning_point_reached = False
default second_turning_point_reached = False
default special_event_triggered = False

# Iniciando o script
label start:
    # Reiniciar o estado do jogo
    $ story_value = 0
    $ choices = []
    $ event_sequence = []
    $ turning_point_reached = False
    $ second_turning_point_reached = False
    $ special_event_triggered = False

    e "Olá, bem-vindo ao nosso jogo!"

    # Primeira escolha
    menu:
        "Escolha 1 (Adiciona 2)":
            $ story_value += 2
            $ choices.append(2)
            $ event_sequence.append("evento_1")
            jump escolha_2

        "Escolha 2 (Adiciona 3)":
            $ story_value += 3
            $ choices.append(3)
            $ event_sequence.append("evento_2")
            jump escolha_2

        "Escolha 3 (Adiciona 5)":
            $ story_value += 5
            $ choices.append(5)
            $ event_sequence.append("evento_3")
            jump escolha_2

        "Escolha 4 (Adiciona 7)":
            $ story_value += 7
            $ choices.append(7)
            $ event_sequence.append("evento_4")
            jump escolha_2

label escolha_2:
    e "Escolha 2"

    # Evento canônico
    e "Um evento importante acontece aqui, independente das escolhas anteriores."
    $ event_sequence.append("evento_canônico")

    # Segunda escolha
    menu:
        "Escolha 5 (Adiciona 11)":
            $ story_value += 11
            $ choices.append(11)
            $ event_sequence.append("evento_5")
            jump escolha_3

        "Escolha 6 (Adiciona 13)":
            $ story_value += 13
            $ choices.append(13)
            $ event_sequence.append("evento_6")
            jump escolha_3

        "Escolha 7 (Adiciona 17)":
            $ story_value += 17
            $ choices.append(17)
            $ event_sequence.append("evento_7")
            jump escolha_3

        "Escolha 8 (Adiciona 19)":
            $ story_value += 19
            $ choices.append(19)
            $ event_sequence.append("evento_8")
            jump escolha_3

label escolha_3:
    e "Escolha 3"

    # Ponto de virada na história
    if story_value >= 20:
        e "Você alcançou um ponto de virada na história!"
        $ turning_point_reached = True
        $ event_sequence.append("ponto_de_virada")

    # Terceira escolha
    menu:
        "Escolha 9 (Adiciona 23)":
            $ story_value += 23
            $ choices.append(23)
            $ event_sequence.append("evento_9")
            jump escolha_4

        "Escolha 10 (Adiciona 29)":
            $ story_value += 29
            $ choices.append(29)
            $ event_sequence.append("evento_10")
            jump escolha_4

        "Escolha 11 (Adiciona 31)":
            $ story_value += 31
            $ choices.append(31)
            $ event_sequence.append("evento_11")
            jump escolha_4

        "Escolha 12 (Adiciona 37)":
            $ story_value += 37
            $ choices.append(37)
            $ event_sequence.append("evento_12")
            jump escolha_4

label escolha_4:
    e "Escolha 4"

    # Evento alterável baseado em múltiplas condições
    if turning_point_reached and not special_event_triggered:
        e "Você desbloqueou um evento especial!"
        $ special_event_triggered = True
        $ event_sequence.append("evento_especial")
    elif not turning_point_reached:
        e "Você ainda não desbloqueou o evento especial."
        $ event_sequence.append("evento_comum")

    # Quarta escolha
    menu:
        "Escolha 13 (Adiciona 41)":
            $ story_value += 41
            $ choices.append(41)
            $ event_sequence.append("evento_13")
            jump escolha_5

        "Escolha 14 (Adiciona 43)":
            $ story_value += 43
            $ choices.append(43)
            $ event_sequence.append("evento_14")
            jump escolha_5

        "Escolha 15 (Adiciona 47)":
            $ story_value += 47
            $ choices.append(47)
            $ event_sequence.append("evento_15")
            jump escolha_5

        "Escolha 16 (Adiciona 53)":
            $ story_value += 53
            $ choices.append(53)
            $ event_sequence.append("evento_16")
            jump escolha_5

label escolha_5:
    e "Escolha 5"

    # Evento canônico
    e "Outro evento importante acontece aqui, independente das escolhas anteriores."
    $ event_sequence.append("evento_canônico_2")

    # Quinta escolha
    menu:
        "Escolha 17 (Adiciona 59)":
            $ story_value += 59
            $ choices.append(59)
            $ event_sequence.append("evento_17")
            jump escolha_6

        "Escolha 18 (Adiciona 61)":
            $ story_value += 61
            $ choices.append(61)
            $ event_sequence.append("evento_18")
            jump escolha_6

        "Escolha 19 (Adiciona 67)":
            $ story_value += 67
            $ choices.append(67)
            $ event_sequence.append("evento_19")
            jump escolha_6

        "Escolha 20 (Adiciona 71)":
            $ story_value += 71
            $ choices.append(71)
            $ event_sequence.append("evento_20")
            jump escolha_6

label escolha_6:
    e "Escolha 6"

    # Ponto de virada na história
    if story_value >= 100:
        e "Você alcançou um segundo ponto de virada na história!"
        $ second_turning_point_reached = True
        $ event_sequence.append("segundo_ponto_de_virada")

    # Sexta escolha
    menu:
        "Escolha 21 (Adiciona 73)":
            $ story_value += 73
            $ choices.append(73)
            $ event_sequence.append("evento_21")
            jump escolha_7

        "Escolha 22 (Adiciona 79)":
            $ story_value += 79
            $ choices.append(79)
            $ event_sequence.append("evento_22")
            jump escolha_7

        "Escolha 23 (Adiciona 83)":
            $ story_value += 83
            $ choices.append(83)
            $ event_sequence.append("evento_23")
            jump escolha_7

        "Escolha 24 (Adiciona 89)":
            $ story_value += 89
            $ choices.append(89)
            $ event_sequence.append("evento_24")
            jump escolha_7

label escolha_7:
    e "Escolha 7"

    # Evento complexo com múltiplas condições
    if second_turning_point_reached and not special_event_triggered:
        e "Você ativou um evento especial por causa do segundo ponto de virada!"
        $ special_event_triggered = True
        $ event_sequence.append("evento_especial_2")
    elif second_turning_point_reached:
        e "Você já ativou o evento especial anteriormente."
        $ event_sequence.append("evento_repetido")
    else:
        e "Um evento comum ocorre aqui."
        $ event_sequence.append("evento_comum_2")

    # Sétima escolha
    menu:
        "Escolha 25 (Adiciona 97)":
            $ story_value += 97
            $ choices.append(97)
            $ event_sequence.append("evento_25")
            jump escolha_8

        "Escolha 26 (Adiciona 101)":
            $ story_value += 101
            $ choices.append(101)
            $ event_sequence.append("evento_26")
            jump escolha_8

        "Escolha 27 (Adiciona 103)":
            $ story_value += 103
            $ choices.append(103)
            $ event_sequence.append("evento_27")
            jump escolha_8

        "Escolha 28 (Adiciona 107)":
            $ story_value += 107
            $ choices.append(107)
            $ event_sequence.append("evento_28")
            jump escolha_8

label escolha_9:
    e "Escolha 9"

    # Evento canônico com impacto adicional
    e "Um evento canônico adicional acontece aqui, impactando a história."
    $ event_sequence.append("evento_canônico_3")

    # Oitava escolha
    menu:
        "Escolha 29 (Adiciona 113)":
            $ story_value += 113
            $ choices.append(113)
            $ event_sequence.append("evento_29")
            jump escolha_10

        "Escolha 30 (Adiciona 127)":
            $ story_value += 127
            $ choices.append(127)
            $ event_sequence.append("evento_30")
            jump escolha_10

        "Escolha 31 (Adiciona 131)":
            $ story_value += 131
            $ choices.append(131)
            $ event_sequence.append("evento_31")
            jump escolha_10

        "Escolha 32 (Adiciona 137)":
            $ story_value += 137
            $ choices.append(137)
            $ event_sequence.append("evento_32")
            jump escolha_10

label escolha_10:
    e "Escolha 10"

    # Evento alterável com base em escolhas anteriores
    if 2 in choices and 7 in choices:
        e "Você desbloqueou um evento especial por ter feito certas escolhas anteriormente!"
        $ event_sequence.append("evento_especial_3")
    else:
        e "Um evento comum ocorre aqui."
        $ event_sequence.append("evento_comum_3")

    # Nona escolha
    menu:
        "Escolha 33 (Adiciona 149)":
            $ story_value += 149
            $ choices.append(149)
            $ event_sequence.append("evento_33")
            jump escolha_11

        "Escolha 34 (Adiciona 151)":
            $ story_value += 151
            $ choices.append(151)
            $ event_sequence.append("evento_34")
            jump escolha_11

        "Escolha 35 (Adiciona 157)":
            $ story_value += 157
            $ choices.append(157)
            $ event_sequence.append("evento_35")
            jump escolha_11

        "Escolha 36 (Adiciona 163)":
            $ story_value += 163
            $ choices.append(163)
            $ event_sequence.append("evento_36")
            jump escolha_11

label escolha_11:
    e "Escolha 11"

    # Segundo ponto de virada com impacto significativo
    if story_value >= 300:
        e "Você alcançou um ponto de virada significativo!"
        $ second_turning_point_reached = True
        $ event_sequence.append("segundo_ponto_de_virada_significativo")

    # Décima escolha
    menu:
        "Escolha 37 (Adiciona 167)":
            $ story_value += 167
            $ choices.append(167)
            $ event_sequence.append("evento_37")
            jump escolha_12

        "Escolha 38 (Adiciona 173)":
            $ story_value += 173
            $ choices.append(173)
            $ event_sequence.append("evento_38")
            jump escolha_12

        "Escolha 39 (Adiciona 179)":
            $ story_value += 179
            $ choices.append(179)
            $ event_sequence.append("evento_39")
            jump escolha_12

        "Escolha 40 (Adiciona 181)":
            $ story_value += 181
            $ choices.append(181)
            $ event_sequence.append("evento_40")
            jump escolha_12

label escolha_12:
    e "Escolha 12"

    # Evento complexo com múltiplas condições e escolhas anteriores
    if 29 in choices and 33 in choices:
        e "Você desbloqueou um evento especial adicional!"
        $ event_sequence.append("evento_especial_4")
    else:
        e "Um evento comum ocorre aqui."
        $ event_sequence.append("evento_comum_4")

    # Décima primeira escolha
    menu:
        "Escolha 41 (Adiciona 191)":
            $ story_value += 191
            $ choices.append(191)
            $ event_sequence.append("evento_41")
            jump escolha_13

        "Escolha 42 (Adiciona 193)":
            $ story_value += 193
            $ choices.append(193)
            $ event_sequence.append("evento_42")
            jump escolha_13

        "Escolha 43 (Adiciona 197)":
            $ story_value += 197
            $ choices.append(197)
            $ event_sequence.append("evento_43")
            jump escolha_13

        "Escolha 44 (Adiciona 199)":
            $ story_value += 199
            $ choices.append(199)
            $ event_sequence.append("evento_44")
            jump escolha_13

label escolha_13:
    e "Escolha 13"

    # Evento canônico com impacto adicional
    e "Um evento canônico final acontece aqui, impactando a conclusão da história."
    $ event_sequence.append("evento_canônico_final")

    # Décima segunda escolha
    menu:
        "Escolha 45 (Adiciona 211)":
            $ story_value += 211
            $ choices.append(211)
            $ event_sequence.append("evento_45")
            jump escolha_14

        "Escolha 46 (Adiciona 223)":
            $ story_value += 223
            $ choices.append(223)
            $ event_sequence.append("evento_46")
            jump escolha_14

        "Escolha 47 (Adiciona 227)":
            $ story_value += 227
            $ choices.append(227)
            $ event_sequence.append("evento_47")
            jump escolha_14

        "Escolha 48 (Adiciona 229)":
            $ story_value += 229
            $ choices.append(229)
            $ event_sequence.append("evento_48")
            jump escolha_14

label escolha_14:
    e "Escolha 14"

    # Determinação final com múltiplas condições e eventos
    if story_value >= 400 and special_event_triggered:
        e "Você alcançou o Final Máximo!"
    elif story_value >= 300:
        e "Você alcançou um Final Grande!"
    elif story_value >= 200:
        e "Você alcançou um Final Médio!"
    else:
        e "Você alcançou um Final Comum!"

    return

