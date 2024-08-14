label event_2:
    p "Um novo dia, novas decisões a serem feitas."

    # Evento que é necessário para o desenvolvimento da história, como um evento canônico
    if story_value >= 10:
        p "Um evento crucial ocorre!"
        jump canonical_event

    else:
        p "As coisas continuam normalmente."
        jump normal_day

label canonical_event:
    p "Este evento é inevitável e moldará seu caminho."
    # Este evento não pode ser alterado pelas escolhas, mas afeta a narrativa.
    jump branching_paths

label normal_day:
    p "Um dia tranquilo, mas suas escolhas ainda importam."
    # Leva a eventos baseados em escolhas anteriores
    jump branching_paths
