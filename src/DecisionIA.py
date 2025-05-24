from IA_Strategies import ia_facile, ia_moyenne, ia_difficile

# ---------------------------------------------------
# Gestion du choix de difficulté pour l'intelligence artificielle
# ---------------------------------------------------

def demander_difficulte(prompt):
    """
    Demande à l'utilisateur de choisir un niveau de difficulté valide.
    
    Paramètre :
    - prompt : Message affiché à l'utilisateur.
    
    Retourne :
    - Le niveau de difficulté choisi sous forme de chaîne ('facile', 'moyen' ou 'difficile').
    """
    while True:
        difficulte = input(prompt).lower()
        if difficulte in ['facile', 'moyen', 'difficile']:
            return difficulte
        else:
            print(" Niveau invalide. Choisissez : 'facile', 'moyen' ou 'difficile'.")


# ---------------------------------------------------
# Sélection automatique du coup en fonction du niveau
# ---------------------------------------------------

def jouer_coup_ia(grille, joueur, difficulte, table_transposition=None):
    """
    Détermine le coup joué par l'IA en fonction du niveau de difficulté sélectionné.

    Paramètres :
    - grille : Grille du jeu (liste 2D).
    - joueur : Caractère représentant le joueur IA ('R' ou 'J').
    - difficulte : Niveau de difficulté ('facile', 'moyen', 'difficile').
    - table_transposition : Dictionnaire mémorisant les évaluations d’états (optionnel).

    Retourne :
    - Index de la colonne choisie par l’IA, ou -2 si aucun coup valide.
    """
    if table_transposition is None:
        table_transposition = {}

    colonnes_valides = [col for col in range(len(grille[0])) if grille[0][col] == ' ']
    if not colonnes_valides:
        return -2  # Partie bloquée ou terminée

    # Appel de la fonction IA appropriée selon le niveau
    if difficulte == "facile":
        return ia_facile(joueur, grille, table_transposition)
    elif difficulte == "moyen":
        return ia_moyenne(joueur, grille, table_transposition)
    elif difficulte == "difficile":
        return ia_difficile(joueur, grille, table_transposition)
