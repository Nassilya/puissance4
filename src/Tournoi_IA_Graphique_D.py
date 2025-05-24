import time
import matplotlib.pyplot as plt
from DecisionIA import jouer_coup_ia
from GestionPosition import trouver_ligne_vide
from Position import Position

# ----------- Paramètres du tournoi pour IA difficile -----------
comparaisons_ia = [
    ("difficile", "facile"),
    ("difficile", "moyen"),
    ("difficile", "difficile")
]
iterations = 50  # nombre de parties 

# ----------- Stockage des résultats -----------
statistiques = []
temps_execution = []

for ia1, ia2 in comparaisons_ia:
    victoires_ia1 = 0
    victoires_ia2 = 0
    temps_total = 0

    for _ in range(iterations):
        grille = [[' ' for _ in range(7)] for _ in range(6)]
        joueur = 'R'
        debut = time.time()

        while True:
            niveau = ia1 if joueur == 'R' else ia2
            colonne = jouer_coup_ia(grille, joueur, niveau)

            if colonne == -2:
                break  # match nul

            ligne = trouver_ligne_vide(grille, colonne)
            grille[ligne][colonne] = joueur
            position = Position(grille, 'J' if joueur == 'R' else 'R')

            if position.verifier_gagnant():
                if joueur == 'R':
                    victoires_ia1 += 1
                else:
                    victoires_ia2 += 1
                break

            joueur = 'J' if joueur == 'R' else 'R'

        temps_total += (time.time() - debut)

    # Résumé des résultats
    temps_moyen = temps_total / iterations
    nom_comparaison = f"{ia1.capitalize()} vs {ia2.capitalize()} ({temps_moyen:.2f}s)"
    temps_execution.append((nom_comparaison, temps_moyen))
    statistiques.append((
        f"{ia1.capitalize()} vs {ia2.capitalize()}",
        ia1.capitalize(), victoires_ia1,
        ia2.capitalize(), victoires_ia2
    ))

# ----------- Affichage des graphiques -----------

# --- 1. Graphique à barres (temps moyen)
noms = [res[0] for res in temps_execution]
valeurs = [res[1] for res in temps_execution]

plt.figure(figsize=(10, 4))
plt.barh(noms, valeurs, color='#F54238')  # rouge clair
plt.xlabel("Temps moyen par match (secondes)")
plt.title("Temps d'exécution moyen par confrontation IA (Difficile)")
plt.tight_layout()
plt.show()

# --- 2. Camemberts des victoires
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

for i, (titre, ia1, vic1, ia2, vic2) in enumerate(statistiques):
    axs[i].pie(
        [vic1, vic2],
        labels=[f"{ia1} ({vic1} victoires)", f"{ia2} ({vic2} victoires)"],
        colors=["#B22222", "#F54238"],  # rouge foncé et rouge clair
        autopct='%1.1f%%',
        startangle=90
    )
    axs[i].set_title(titre)

plt.tight_layout()
plt.show()