import time
import sys
from Position import Position
from GestionPosition import est_match_nul as tie, trouver_ligne_vide
from DecisionIA import jouer_coup_ia
from Interface import afficher_grille

# ---------------------------------------------
# Mode Joueur contre Joueur
# ---------------------------------------------

def jouer_joueur_contre_joueur(grille, joueur, colonnes):
    while True:
        afficher_grille(grille)  # Affiche la grille à chaque tour

        choix = input(f"Joueur {joueur}, choisissez une colonne (0-{colonnes - 1}) : ")

        try:
            col = int(choix)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            continue

        if 0 <= col < colonnes and grille[0][col] == ' ':
            ligne = trouver_ligne_vide(grille, col)
            grille[ligne][col] = joueur

            position = Position(grille, 'R' if joueur == 'J' else 'J')
            if position.verifier_gagnant():
                afficher_grille(grille)
                print(f"Le joueur {joueur} a gagné !")
                break

            if tie(grille):  # test de match nul après le coup
                afficher_grille(grille)
                print("La partie est un match nul.")
                break

            joueur = 'J' if joueur == 'R' else 'R'
        else:
            print("Choix invalide. Veuillez choisir une colonne valide.")

# ---------------------------------------------
# Mode Joueur contre IA
# ---------------------------------------------

def jouer_joueur_contre_ia(grille, joueur, difficulte, colonnes):
    while True:
        afficher_grille(grille)

        if joueur == 'R':
            choix = input(f"Joueur {joueur}, choisissez une colonne (0-{colonnes - 1}) : ")

            try:
                col = int(choix)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
                continue

            if 0 <= col < colonnes and grille[0][col] == ' ':
                ligne = trouver_ligne_vide(grille, col)
                grille[ligne][col] = joueur

                position = Position(grille, 'J')
                if position.verifier_gagnant():
                    afficher_grille(grille)
                    print(f"Le joueur {joueur} a gagné !")
                    break

                if tie(grille):
                    afficher_grille(grille)
                    print("La partie est un match nul.")
                    break

                joueur = 'J'
            else:
                print("Choix invalide.")
        else:
            col = jouer_coup_ia(grille, joueur, difficulte)
            print(f"L'IA a choisi la colonne {col}")

            if col == -2:
                afficher_grille(grille)
                print("La partie est un match nul.")
                break

            if 0 <= col < colonnes and grille[0][col] == ' ':
                ligne = trouver_ligne_vide(grille, col)
                grille[ligne][col] = joueur

                position = Position(grille, 'R')
                if position.verifier_gagnant():
                    afficher_grille(grille)
                    print(f"L'IA ({joueur}) a gagné !")
                    break

                if tie(grille):
                    afficher_grille(grille)
                    print("La partie est un match nul.")
                    break

                joueur = 'R'
            else:
                print("L'IA a choisi une colonne invalide.")

                
# ---------------------------------------------
# Mode IA contre IA
# ---------------------------------------------

def jouer_ia_contre_ia(grille, joueur, difficulte_r, difficulte_j, colonnes):
    while True:
        col = jouer_coup_ia(grille, joueur, difficulte_r if joueur == 'R' else difficulte_j)
        print(f"L'IA {joueur} a choisi la colonne {col}")

        if col == -2:
            print("La partie est un match nul.")
            break

        if 0 <= col < colonnes and grille[0][col] == ' ':
            ligne = trouver_ligne_vide(grille, col)
            grille[ligne][col] = joueur
            afficher_grille(grille)

            position = Position(grille, 'J' if joueur == 'R' else 'R')
            if position.verifier_gagnant():
                print(f"Victoire de l'IA {joueur} !")
                break

            joueur = 'J' if joueur == 'R' else 'R'
        else:
            print("Colonne invalide choisie par l'IA.")

# ---------------------------------------------
# Statistiques IA vs IA
# ---------------------------------------------

def statistiques_ia_contre_ia(difficulte1, difficulte2, iterations):
    victoires1 = 0
    victoires2 = 0
    debut = time.time()

    for i in range(iterations):
        ratio = (i + 1) / iterations
        bar = int(ratio * 20)
        sys.stdout.write(f"\rChargement : [{'█' * bar}{'░' * (20 - bar)}] {int(ratio * 100)}%")
        sys.stdout.flush()

        grille = [[' ' for _ in range(7)] for _ in range(6)]
        joueur = 'R'

        while True:
            col = jouer_coup_ia(grille, joueur, difficulte1 if joueur == 'R' else difficulte2)

            if col == -2:
                break

            ligne = trouver_ligne_vide(grille, col)
            grille[ligne][col] = joueur

            position = Position(grille, 'J' if joueur == 'R' else 'R')
            if position.verifier_gagnant():
                if joueur == 'R':
                    victoires1 += 1
                else:
                    victoires2 += 1
                break

            joueur = 'J' if joueur == 'R' else 'R'

    print()
    fin = time.time()
    temps_total = fin - debut
    moyenne = temps_total / iterations
    ratio1 = victoires1 / iterations
    ratio2 = victoires2 / iterations

    print(f"Victoires IA 1 ({difficulte1}) : {victoires1}")
    print(f"Victoires IA 2 ({difficulte2}) : {victoires2}")
    print(f"Ratio IA 1 : {ratio1:.2f}")
    print(f"Ratio IA 2 : {ratio2:.2f}")
    print(f"Temps total : {temps_total:.2f}s")
    print(f"Temps moyen par partie : {moyenne:.2f}s")
