label event_1:
    p "Um evento importante acontece..."

    menu:
        "Tomar uma decisão a favor da Protagonista Feminina 1":
            $ relationship_points_h1 += 5
            $ story_value += 1
            jump after_event_1

        "Tomar uma decisão a favor da Protagonista Feminina 2":
            $ relationship_points_h2 += 5
            $ story_value += 2
            jump after_event_1

        "Tomar uma decisão a favor da Protagonista Feminina 3":
            $ relationship_points_h3 += 5
            $ story_value += 3
            jump after_event_1

        "Tomar uma decisão a favor da Protagonista Feminina 4":
            $ relationship_points_h4 += 5
            $ story_value += 4
            jump after_event_1

        "Tomar uma decisão a favor da Protagonista Feminina 5":
            $ relationship_points_h5 += 5
            $ story_value += 5
            jump after_event_1

        "Tomar uma decisão a favor da Protagonista Feminina 6":
            $ relationship_points_h6 += 5
            $ story_value += 6
            jump after_event_1

        "Não tomar partido":
            p "Você escolheu não se envolver."
            $ story_value -= 1
            jump after_event_1

label after_event_1:
    p "O evento passou, mas deixou marcas em suas relações."
    # Avance para o próximo evento ou dia
    jump event_2
