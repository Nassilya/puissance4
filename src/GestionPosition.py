# -----
# Gestion du Jeu IA : Fonctions Utilitaires pour Évaluer l'État du Jeu
# -----

def trouver_ligne_vide(grille, col):
    """
    Identifie la première ligne vide dans une colonne donnée (de bas en haut).
    
    Paramètres :
    - grille : Liste 2D représentant le plateau de jeu.
    - col : Entier représentant la colonne à vérifier.
    
    Retourne :
    - L'indice de la première ligne vide, ou -1 si la colonne est pleine.
    """
    for ligne in range(len(grille) - 1, -1, -1):
        if grille[ligne][col] == ' ':
            return ligne
    return -1


def compter_consecutifs_horizontal(grille, joueur, ligne, col):
    """
    Compte le nombre de pièces consécutives horizontalement depuis une position donnée.
    
    Paramètres :
    - grille : Liste 2D représentant le plateau de jeu.
    - joueur : Caractère représentant le joueur dont on compte les jetons.
    - ligne : Index de la ligne de départ.
    - col : Index de la colonne de départ.
    
    Retourne :
    - Le nombre de jetons alignés horizontalement.
    """
    count = 1
    # Vérification à gauche
    for c in range(col - 1, -1, -1):
        if grille[ligne][c] == joueur:
            count += 1
        else:
            break
    # Vérification à droite
    for c in range(col + 1, len(grille[0])):
        if grille[ligne][c] == joueur:
            count += 1
        else:
            break
    return count


def compter_consecutifs_vertical(grille, joueur, ligne, col):
    """
    Compte le nombre de pièces consécutives verticalement depuis une position donnée.
    
    Paramètres :
    - grille : Liste 2D représentant le plateau de jeu.
    - joueur : Caractère représentant le joueur dont on compte les jetons.
    - ligne : Index de la ligne de départ.
    - col : Index de la colonne de départ.
    
    Retourne :
    - Le nombre de jetons alignés verticalement.
    """
    count = 1
    # Vérification vers le haut
    for r in range(ligne - 1, -1, -1):
        if grille[r][col] == joueur:
            count += 1
        else:
            break
    # Vérification vers le bas
    for r in range(ligne + 1, len(grille)):
        if grille[r][col] == joueur:
            count += 1
        else:
            break
    return count


def compter_consecutifs_diagonal_droite(grille, joueur, ligne, col):
    """
    Compte le nombre de pièces consécutives sur la diagonale descendante (↘) depuis une position donnée.
    
    Paramètres :
    - grille : Liste 2D représentant le plateau de jeu.
    - joueur : Caractère représentant le joueur dont on compte les jetons.
    - ligne : Index de la ligne de départ.
    - col : Index de la colonne de départ.
    
    Retourne :
    - Le nombre de jetons alignés sur la diagonale descendante.
    """
    count = 1
    # Vérification en haut à droite (↗)
    r, c = ligne - 1, col + 1
    while r >= 0 and c < len(grille[0]):
        if grille[r][c] == joueur:
            count += 1
        else:
            break
        r -= 1
        c += 1
    # Vérification en bas à gauche (↙)
    r, c = ligne + 1, col - 1
    while r < len(grille) and c >= 0:
        if grille[r][c] == joueur:
            count += 1
        else:
            break
        r += 1
        c -= 1
    return count


def compter_consecutifs_diagonal_gauche(grille, joueur, ligne, col):
    """
    Compte le nombre de pièces consécutives sur la diagonale montante (↖) depuis une position donnée.
    
    Paramètres :
    - grille : Liste 2D représentant le plateau de jeu.
    - joueur : Caractère représentant le joueur dont on compte les jetons.
    - ligne : Index de la ligne de départ.
    - col : Index de la colonne de départ.
    
    Retourne :
    - Le nombre de jetons alignés sur la diagonale montante.
    """
    count = 1
    # Vérification en haut à gauche (↖)
    r, c = ligne - 1, col - 1
    while r >= 0 and c >= 0:
        if grille[r][c] == joueur:
            count += 1
        else:
            break
        r -= 1
        c -= 1
    # Vérification en bas à droite (↘)
    r, c = ligne + 1, col + 1
    while r < len(grille) and c < len(grille[0]):
        if grille[r][c] == joueur:
            count += 1
        else:
            break
        r += 1
        c += 1
    return count

# -----
#  Utilitaire pour la détection d'égalité
# -----

def est_match_nul(grille):
    """
    Vérifie si la partie est un match nul (aucun coup possible).
    
    Paramètres :
    - grille : Liste 2D représentant le plateau de jeu.
    
    Retourne :
    - Booléen : True si la partie est un match nul, sinon False.
    """
    # Vérifier si une colonne a encore de l'espace
    for col in range(0, 6):
        for ligne in range(len(grille) - 1, -1, -1):
            if grille[ligne][col] == ' ':
                return False
    return True
