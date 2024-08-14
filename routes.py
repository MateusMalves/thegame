label branching_paths:
    # Aqui o jogador é direcionado para diferentes rotas baseadas nas pontuações acumuladas
    if relationship_points_h1 >= 20:
        jump h1_path

    elif relationship_points_h2 >= 20:
        jump h2_path

    elif relationship_points_h3 >= 20:
        jump h3_path

    elif relationship_points_h4 >= 20:
        jump h4_path

    elif relationship_points_h5 >= 20:
        jump h5_path

    elif relationship_points_h6 >= 20:
        jump h6_path

    elif story_value >= 15 and all([relationship_points_h1 >= 10, relationship_points_h2 >= 10, relationship_points_h3 >= 10, relationship_points_h4 >= 10, relationship_points_h5 >= 10, relationship_points_h6 >= 10]):
        jump harem_path

    else:
        jump bad_ending_path
