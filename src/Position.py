from GestionPosition import trouver_ligne_vide, compter_consecutifs_horizontal, compter_consecutifs_vertical, compter_consecutifs_diagonal_droite, compter_consecutifs_diagonal_gauche, est_match_nul
class Position:
    """
    Représente l'état actuel du jeu
    """

    def __init__(self, grille, joueur_courant):
        """
        Initialise la position de la grille et le joueur actuel.
        
        Paramètres :
        - grille : Liste 2D représentant le plateau de jeu.
        - joueur_courant : Caractère représentant le joueur actuel.
        """
        self.grille = [ligne[:] for ligne in grille]
        self.joueur_courant = joueur_courant

    def est_terminale(self):
        """
        Détermine si l'état actuel du jeu est terminal (c'est-à-dire, si la partie est terminée).
        
        Retourne : Un booléen indiquant si la partie est terminée.
        """
        return self.verifier_gagnant() or all(case != ' ' for ligne in self.grille for case in ligne)

    def evaluer(self):
        """
        Évalue l'état du jeu du point de vue du joueur 'R'.
        
        Retourne : Un score entier indiquant la favorabilité de l'état pour 'R'.
        """
        # Score positif pour des positions favorables à 'R', négatif pour 'J'
        gagnant = self.verifier_gagnant()
        if gagnant == 'R':
            return 1000  # L'IA ('R') gagne
        elif gagnant == 'J':
            return -1000  # L'adversaire ('J') gagne
        elif self.est_terminale():
            return 0

        score = 0
        for ligne in range(len(self.grille)):
            for col in range(len(self.grille[0])):
                if self.grille[ligne][col] == 'R':
                    score += self.evaluer_position(ligne, col)
                elif self.grille[ligne][col] == 'J':
                    score -= self.evaluer_position(ligne, col)

        return score

    def evaluer_position(self, ligne, col):
        """
        Évalue la favorabilité d'une position spécifique sur le plateau.
        
        Paramètres :
        - ligne : Index de la ligne de la position.
        - col : Index de la colonne de la position.
        
        Retourne : Un score entier basé sur la proximité avec une condition de victoire.
        """
        score_proximite = 0
        score_vertical = compter_consecutifs_vertical(self.grille, 'R', ligne, col)
        score_horizontal = compter_consecutifs_horizontal(self.grille, 'R', ligne, col)
        score_diagonal_droite = compter_consecutifs_diagonal_droite(self.grille, 'R', ligne, col)
        score_diagonal_gauche = compter_consecutifs_diagonal_gauche(self.grille, 'R', ligne, col)
        
        # Prioriser les alignements plus longs
        score_proximite += max(score_diagonal_droite, score_diagonal_gauche, score_vertical, score_horizontal) ** 2
        return score_proximite

    def generer_coups(self):
        """
        Génère tous les coups possibles pour le joueur actuel.
        
        Retourne : Liste des indices de colonnes où le joueur peut placer son jeton.
        """
        return [col for col in range(len(self.grille[0])) if self.grille[0][col] == ' ']

    def jouer(self, coup):
        """
        Joue un coup et retourne l'état du jeu résultant.
        
        Paramètres :
        - coup : Index de la colonne où le jeton doit être placé.
        
        Retourne : Un nouvel objet Position représentant l'état après le coup.
        """
        nouvelle_grille = [ligne[:] for ligne in self.grille]
        ligne_insertion = trouver_ligne_vide(nouvelle_grille, coup)
        nouvelle_grille[ligne_insertion][coup] = self.joueur_courant
        return Position(nouvelle_grille, 'R' if self.joueur_courant == 'J' else 'J')

    def verifier_gagnant(self):
        """
        Vérifie s'il y a un gagnant dans l'état actuel du jeu.
        
        Retourne : Le caractère du joueur gagnant, ou None s'il n'y a pas de gagnant.
        """
        for ligne in range(len(self.grille)):
            for col in range(len(self.grille[0])):
                if self.grille[ligne][col] != ' ':
                    # Vérification horizontale
                    if col + 3 < len(self.grille[0]):
                        if (self.grille[ligne][col] == self.grille[ligne][col + 1] ==
                                self.grille[ligne][col + 2] == self.grille[ligne][col + 3]):
                            return self.grille[ligne][col]
                    # Vérification verticale
                    if ligne + 3 < len(self.grille):
                        if (self.grille[ligne][col] == self.grille[ligne + 1][col] ==
                                self.grille[ligne + 2][col] == self.grille[ligne + 3][col]):
                            return self.grille[ligne][col]
                    # Vérification diagonale /
                    if col + 3 < len(self.grille[0]) and ligne + 3 < len(self.grille):
                        if (self.grille[ligne][col] == self.grille[ligne + 1][col + 1] ==
                                self.grille[ligne + 2][col + 2] == self.grille[ligne + 3][col + 3]):
                            return self.grille[ligne][col]
                    # Vérification diagonale \
                    if col - 3 >= 0 and ligne + 3 < len(self.grille):
                        if (self.grille[ligne][col] == self.grille[ligne + 1][col - 1] ==
                                self.grille[ligne + 2][col - 2] == self.grille[ligne + 3][col - 3]):
                            return self.grille[ligne][col]
        return None

       


