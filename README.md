# Calculatrice Flask

Projet réalisé dans le cadre du cours LOG3000 à Polytechnique Montréal.

**Équipe 23**

## 1. Description du projet

Ce projet consiste à développer et à maintenir une calculatrice web à l'aide de Python et du framework Flask. L'application permet aux utilisateurs d'effectuer les quatre opérations mathématiques de base : l'addition, la soustraction, la multiplication et la division.

L'utilisateur saisit une expression à partir des boutons de l'interface. Lorsqu'il appuie sur le bouton « = », l'expression est envoyée au serveur Flask, qui vérifie sa validité, effectue le calcul et retourne le résultat à afficher.

La calculatrice est conçue pour traiter une seule opération entre deux nombres à la fois. Elle ne prend donc pas en charge les expressions plus complexes contenant plusieurs opérateurs, des parenthèses ou des nombres négatifs.

Notre objectif est de rendre cette application fiable, bien documentée et facile à maintenir. Pour y parvenir, nous avons amélioré la documentation du code, développé des tests automatisés et corrigé les bogues identifiés. Nous utilisons également GitHub pour organiser les modifications et faciliter la collaboration entre les membres de l'équipe.

### Structure du projet

Le projet est composé des fichiers et répertoires suivants :

- **`app.py`** : contient le serveur Flask, valide les expressions saisies et fait appel aux fonctions de calcul.
- **`operators.py`** : regroupe les fonctions responsables des quatre opérations mathématiques.
- **`templates/`** : contient le fichier HTML qui définit l'interface de la calculatrice et les interactions avec les boutons.
- **`static/`** : contient le fichier CSS qui gère l'apparence et la disposition des éléments de l'interface.
- **`tests/`** : regroupe les tests automatisés permettant de vérifier le fonctionnement de l'application.

## 2. Installation

### Prérequis

Avant d'installer l'application, il est nécessaire de disposer des outils suivants :

- **Python 3** : pour exécuter l'application.
- **pip** : pour installer les dépendances Python.
- **Git** : pour récupérer le code source depuis GitHub.

### Étapes d'installation

**1. Cloner le dépôt GitHub**

Ouvrir un terminal et exécuter la commande suivante pour récupérer le projet :

`git clone https://github.com/chaimaamesbah/LOG3000_TP3_23.git`

**2. Accéder au répertoire du projet**

Se déplacer dans le dossier téléchargé :

`cd LOG3000_TP3_23`

**3. Créer et activer un environnement virtuel (recommandé)**

L'utilisation d'un environnement virtuel permet d'isoler les dépendances du projet.

Sur macOS ou Linux :

`python3 -m venv .venv`

`source .venv/bin/activate`

Sur Windows :

`py -m venv .venv`

`.venv\Scripts\activate`

**4. Installer les dépendances**

L'application utilise Flask pour gérer le serveur web. Installer cette bibliothèque avec la commande suivante :

`python -m pip install flask`

Sur macOS ou Linux, si `python` n'est pas reconnu, utiliser `python3` à la place.

## 3. Utilisation

### Démarrer l'application

Une fois l'installation terminée, se placer à la racine du projet et lancer le serveur Flask avec la commande :

`python app.py`

Sur macOS ou Linux, la commande `python3 app.py` peut également être utilisée.

Par défaut, l'application est accessible à l'adresse suivante :

http://127.0.0.1:5000

Ouvrir cette adresse dans un navigateur pour accéder à la calculatrice.

### Effectuer un calcul

L'interface permet de saisir et d'exécuter une opération à l'aide des boutons disponibles.

1. Sélectionner les boutons numériques pour saisir le premier nombre.
2. Choisir l'opération souhaitée parmi `+`, `-`, `*` et `/`.
3. Saisir le deuxième nombre.
4. Appuyer sur le bouton **=** pour effectuer le calcul et afficher le résultat.

Par exemple, pour effectuer l'addition `8+2`, il suffit de sélectionner successivement les boutons `8`, `+`, `2` et `=`. Le résultat attendu est `10`.

Le bouton **C** permet d'effacer l'affichage et de commencer un nouveau calcul. Si une expression est invalide, comme `8+` ou `8+2+3`, un message d'erreur s'affiche à la place du résultat.

Pour arrêter le serveur, utiliser la combinaison `Ctrl+C` dans le terminal.

## 4. Tests

Des tests automatisés ont été développés avec **pytest** afin de vérifier le fonctionnement de la calculatrice et d'identifier les bogues présents dans le code.

Ces tests couvrent notamment les quatre opérations mathématiques, la validation des expressions ainsi que les cas particuliers, comme la division par zéro.

Les fichiers de test sont regroupés dans le répertoire `tests/`, qui contient également une documentation expliquant leur rôle.

### Exécuter les tests

**1. Installer pytest :**

`python -m pip install pytest`

**2. Se placer à la racine du projet et lancer les tests :**

`python -m pytest`

Les tests ont d'abord été exécutés sur le code initial afin de repérer les problèmes. Après chaque correction, ils ont été relancés pour vérifier que le bogue était résolu. Une exécution complète des tests a été également réalisée après la fusion des modifications.

## 5. Flux de contribution

Pour assurer une bonne collaboration et conserver un historique clair des modifications, notre équipe utilise les Issues, les branches Git et les Pull Requests. Les modifications sont réalisées sur des branches distinctes plutôt que directement sur la branche principale `main`.

### 5.1. Création des Issues

Lorsqu'un bogue est découvert, une Issue GitHub est créée pour documenter le problème. Elle comprend une description du bogue, les étapes permettant de le reproduire, le résultat attendu et le résultat obtenu. Chaque issue est ensuite assignée à un membre de l'équipe.

### 5.2. Création des branches

Une branche distincte est créée pour chaque issue. Les branches de correction `fix/` ont été créées à partir de `test/operations-et-interface`, qui contenait déjà les tests. Les branches sont nommées selon le type de modification, par exemple `fix/nom-du-bogue` pour une correction ou `docs/documentation` pour une amélioration de la documentation.

### 5.3. Modifications et tests

Le membre responsable effectue les changements nécessaires sur sa branche et exécute les tests concernés. Les modifications sont ensuite enregistrées avec des messages de commit clairs qui décrivent les corrections apportées.

### 5.4. Pull Requests et fusion

Une fois les modifications terminées, une Pull Request est ouverte vers `main` en faisant référence à l’issue correspondante. Avant la fusion, on relance le test lié à l’issue pour vérifier que la correction fonctionne.

Après la fusion, l'ensemble des tests est exécuté à nouveau afin de confirmer le bon fonctionnement de l'application et de s'assurer qu'aucune régression n'a été introduite.
