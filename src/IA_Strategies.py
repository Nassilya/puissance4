import random
from GestionPosition import trouver_ligne_vide
from Position import Position

# --------------------------------------------------
#  Algorithme Negamax avec élagage Alpha-Bêta
# --------------------------------------------------

def negamax(position, alpha, beta, profondeur, table_transposition=None):
    """
    Exécute récursivement l'algorithme Negamax pour trouver le meilleur coup, optimisé avec l’élagage alpha-bêta.

    Paramètres :
    - position : instance de la classe Position représentant l’état du jeu.
    - alpha : score minimum garanti pour le joueur maximisant.
    - beta : score maximum garanti pour le joueur minimisant.
    - profondeur : profondeur maximale de recherche.
    - table_transposition : dictionnaire optionnel pour stocker les évaluations déjà calculées.

    Retour :
    - Le meilleur score atteignable depuis cette position avec un jeu optimal.
    """
    if table_transposition is None:
        table_transposition = {}

    if position.est_terminale() or profondeur == 0:
        return position.evaluer() if position.joueur_courant == 'R' else -position.evaluer()

    cle_position = tuple(map(tuple, position.grille))
    if cle_position in table_transposition:
        return table_transposition[cle_position]

    coups_valides = position.generer_coups()
    coups_valides.sort(key=lambda col: -position.evaluer_position(trouver_ligne_vide(position.grille, col), col))

    for coup in coups_valides:
        enfant = position.jouer(coup)
        score = -negamax(enfant, -beta, -alpha, profondeur - 1, table_transposition)
        alpha = max(alpha, score)
        if score >= beta:
            return beta

    table_transposition[cle_position] = alpha
    return alpha

# --------------------------------------------------
# Niveau facile : stratégie simplifiée + hasard
# --------------------------------------------------

def ia_facile(joueur, grille, table_transposition=None):
    """
    Calcule le coup de l’IA en mode facile.

    Paramètres :
    - joueur : 'R' ou 'J'
    - grille : grille de jeu (liste 2D)
    - table_transposition : dictionnaire pour optimiser les calculs

    Retour :
    - Index de la colonne choisie, ou -2 si aucun coup n’est possible.
    """
    if table_transposition is None:
        table_transposition = {}

    colonnes_valides = [col for col in range(len(grille[0])) if grille[0][col] == ' ']
    if not colonnes_valides:
        return -2

    meilleur_score = float('-inf')
    meilleur_coup = -1
    alpha = float('-inf')
    beta = float('inf')

    for col in colonnes_valides:
        ligne = trouver_ligne_vide(grille, col)
        grille[ligne][col] = joueur

        cle_position = tuple(map(tuple, grille))

        if cle_position in table_transposition:
            score = table_transposition[cle_position]
        else:
            position = Position(grille, 'R' if joueur == 'J' else 'J')
            score = -negamax(position, -beta, -alpha, profondeur=3, table_transposition=table_transposition)
            table_transposition[cle_position] = score

        grille[ligne][col] = ' '

        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = col
        elif score == meilleur_score and random.random() < 0.08:
            meilleur_coup = col

        alpha = max(alpha, score)
        if alpha >= beta:
            break

    return meilleur_coup

# --------------------------------------------------
# Niveau moyen : profondeur plus grande
# --------------------------------------------------

def ia_moyenne(joueur, grille, table_transposition=None):
    """
    Calcule le coup de l’IA en mode moyen.

    Paramètres :
    - joueur : 'R' ou 'J'
    - grille : grille de jeu
    - table_transposition : dictionnaire pour optimiser

    Retour :
    - Index de la colonne choisie, ou -2 si aucun coup possible.
    """
    if table_transposition is None:
        table_transposition = {}

    colonnes_valides = [col for col in range(len(grille[0])) if grille[0][col] == ' ']
    if not colonnes_valides:
        return -2

    meilleur_score = float('-inf')
    meilleur_coup = -1
    alpha = float('-inf')
    beta = float('inf')

    for col in colonnes_valides:
        ligne = trouver_ligne_vide(grille, col)
        grille[ligne][col] = joueur

        cle_position = tuple(map(tuple, grille))

        if cle_position in table_transposition:
            score = table_transposition[cle_position]
        else:
            position = Position(grille, 'R' if joueur == 'J' else 'J')
            score = -negamax(position, -beta, -alpha, profondeur=5, table_transposition=table_transposition)
            table_transposition[cle_position] = score

        grille[ligne][col] = ' '

        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = col

        alpha = max(alpha, score)
        if alpha >= beta:
            break

    return meilleur_coup

# --------------------------------------------------
# Niveau difficile : priorité au centre + profondeur max
# --------------------------------------------------

def ia_difficile(joueur, grille, table_transposition=None):
    """
    Calcule le coup de l’IA en mode difficile.

    Paramètres :
    - joueur : 'R' ou 'J'
    - grille : grille de jeu
    - table_transposition : dictionnaire pour optimiser

    Retour :
    - Index de la colonne choisie, ou -2 si aucun coup possible.
    """
    if table_transposition is None:
        table_transposition = {}

    meilleur_score = float('-inf')
    meilleur_coup = -1
    alpha = float('-inf')
    beta = float('inf')

    # Priorité aux colonnes centrales
    ordre_colonnes = [3, 2, 4, 1, 5, 0, 6]
    colonnes_valides = [col for col in ordre_colonnes if grille[0][col] == ' ']

    for col in colonnes_valides:
        ligne = trouver_ligne_vide(grille, col)
        grille[ligne][col] = joueur

        cle_position = tuple(map(tuple, grille))

        if cle_position in table_transposition:
            score = table_transposition[cle_position]
        else:
            position = Position(grille, 'R' if joueur == 'J' else 'J')
            score = -negamax(position, -beta, -alpha, profondeur=8, table_transposition=table_transposition)
            table_transposition[cle_position] = score

        grille[ligne][col] = ' '

        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = col

        alpha = max(alpha, score)
        if alpha >= beta:
            break

    return meilleur_coup
