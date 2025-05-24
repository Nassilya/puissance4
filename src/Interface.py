# -----
# Fonctions d'interface : Affichage de la grille
# -----

def afficher_grille(grille):
    """
    Affiche le plateau de jeu dans un format lisible par l'utilisateur

    Paramètre :
    - grille : Liste 2D représentant le plateau de jeu, où chaque case peut être vide ou occupée par un pion
    """
    # Affiche les indices de colonnes
    indices_colonnes = "   ".join(str(i) for i in range(len(grille[0])))
    ligne_horizontale = "+-" + "-+-".join(["-" for _ in range(len(grille[0]))]) + "-+"

    print("  ", indices_colonnes)
    print(ligne_horizontale)

    for ligne in grille:
        print("| " + " | ".join(ligne) + " |")

    print(ligne_horizontale)
