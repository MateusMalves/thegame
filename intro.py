label start:
    p "Você se encontra em um mundo onde suas escolhas determinarão seu destino."

    # Primeira escolha que afeta os pontos de relacionamento
    menu:
        "Passar tempo com a Protagonista Feminina 1":
            $ relationship_points_h1 += 5
            jump after_first_choice

        "Passar tempo com a Protagonista Feminina 2":
            $ relationship_points_h2 += 5
            jump after_first_choice

        "Passar tempo com a Protagonista Feminina 3":
            $ relationship_points_h3 += 5
            jump after_first_choice

        "Passar tempo com a Protagonista Feminina 4":
            $ relationship_points_h4 += 5
            jump after_first_choice

        "Passar tempo com a Protagonista Feminina 5":
            $ relationship_points_h5 += 5
            jump after_first_choice

        "Passar tempo com a Protagonista Feminina 6":
            $ relationship_points_h6 += 5
            jump after_first_choice

label after_first_choice:
    p "Suas escolhas começaram a moldar seu futuro."
    jump event_1
