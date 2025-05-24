# 🔴🟡 Puissance 4 – Projet IA
Ce projet consiste en une implémentation complète du jeu **Puissance 4** avec une **Intelligence Artificielle** jouable à trois niveaux de difficulté. Il a été développé dans le cadre du projet d’Intelligence Artificielle en L3 Informatique à l’Université Paris Cité.

L’objectif est de simuler une IA capable de jouer intelligemment à Puissance 4, en intégrant les algorithmes classiques de recherche comme **Negamax**, l’élagage **alpha-bêta**, l’**optimisation avec table de transposition**, et la **priorisation des coups** selon la stratégie.

## Objectifs pédagogiques

- Implémenter un moteur d’IA avec différentes stratégies
- Maîtriser les algorithmes de recherche et d’évaluation dans les jeux
- Analyser les performances (temps et taux de victoire) selon les niveaux

## Fonctionnalités

- Interface console pour jouer contre l’IA
- Trois niveaux d’IA : Facile, Moyen et Difficile
- Optimisation avec table de transposition
- Analyse de performance par tournoi automatique
- Visualisation des résultats avec `matplotlib`

## Fonctionnalités de l’IA

| Niveau    | Profondeur | Randomisation | Optimisation                 |
|-----------|------------|---------------|-------------------------------|
| Facile    | 3          | Oui (8%)      | Table de transposition       |
| Moyen     | 5          | Non           | Alpha-Beta + Transposition   |
| Difficile | 8          | Non           | Priorité centrale + Table    |


## Architecture du projet

```
Puissance4_IA/
├── main.py                  # Lancement du jeu
├── Position.py              # Classe représentant l’état du jeu
├── Interface.py             # affiche dynamiquement l’état du plateau pour une meilleure lisibilité en console
├── ModesJeu.py              # Ce module gère les différents modes de confrontation disponibles
├── GestionPosition.py       # Fonctions utilitaires pour manipuler la grille
├── IA_Strategies.py         # Fonctions de Negamax et IA par niveau
├── DecisionIA.py            # Fonction de décision selon le niveau
├── Tournoi_IA_Graphique.py  # Simulation de tournois entre IA
├── README.md                # Documentation
```

## Instructions pour exécuter le programme

1. **Prérequis** : Python 3 doit être installé sur votre machine.

2. **Cloner ou copier le projet** dans un dossier local.

3. **Installer les dépendances** (notamment `matplotlib`) :

```bash
pip install matplotlib
```

4. **Lancer le jeu** depuis un terminal :

```bash
python src/main.py
```

---

## Analyse comparative des IA

Un script de tournoi (`Tournoi_IA_Graphique.py`) permet de comparer les IA par paires sur plusieurs parties et de générer :

- Un graphique à barres des temps moyens d’exécution
- Des diagrammes en camembert des victoires

## Auteurs

- Nassilya Belguedj
