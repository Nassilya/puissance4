import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Interface import afficher_grille
from ModesJeu import jouer_joueur_contre_joueur, jouer_joueur_contre_ia, jouer_ia_contre_ia, statistiques_ia_contre_ia
from DecisionIA import demander_difficulte

# ------------------------------------------------------------
# Fonction principale
# ------------------------------------------------------------
def lancer_puissance_4():
    """
    Fonction principale pour jouer à Puissance 4.
    """
    jeu_en_cours = True
    lignes = 6
    colonnes = 7
    joueur = 'R'

    print("Bienvenue dans le jeu Puissance 4 ! ")

    while jeu_en_cours:
        try:
            while True:
                try:
                    mode = int(input(
                        "\n Choisissez un mode de jeu :\n"
                        "1. Joueur vs Joueur\n"
                        "2. Joueur vs IA\n"
                        "3. IA vs IA\n"
                        "4. Statistiques IA vs IA\n"
                        "5. Quitter\n"
                        "Votre choix : "
                    ))
                    break
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

            # Initialiser une nouvelle grille
            grille = [[' ' for _ in range(colonnes)] for _ in range(lignes)]

            if mode == 1:
                afficher_grille(grille)
                jouer_joueur_contre_joueur(grille, joueur, colonnes)

            elif mode == 2:
                afficher_grille(grille)
                difficulte = demander_difficulte("Choisissez la difficulté de l'IA (facile, moyen, difficile) : ")
                jouer_joueur_contre_ia(grille, joueur, difficulte, colonnes)

            elif mode == 3:
                difficulte_r = demander_difficulte("Difficulté pour l’IA du joueur Rouge : ")
                difficulte_j = demander_difficulte("Difficulté pour l’IA du joueur Jaune : ")
                jouer_ia_contre_ia(grille, joueur, difficulte_r, difficulte_j, colonnes)

            elif mode == 4:
                difficulte1 = demander_difficulte("⚙️ Difficulté pour le premier IA : ")
                difficulte2 = demander_difficulte("⚙️ Difficulté pour le second IA : ")

                while True:
                    try:
                        iterations = int(input(" Nombre d’itérations à effectuer : "))
                        break
                    except ValueError:
                        print(" Veuillez entrer un nombre entier.")

                statistiques_ia_contre_ia(difficulte1, difficulte2, iterations)

            elif mode == 5:
                print("Merci d’avoir joué à Puissance 4. À bientôt !")
                jeu_en_cours = False

            else:
                print(" Choix de mode invalide.")

        except Exception as e:
            print(f" Une erreur inattendue est survenue : {e}")

# Point d'entrée du programme
if __name__ == "__main__":
    lancer_puissance_4()
