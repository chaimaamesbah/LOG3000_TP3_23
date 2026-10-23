# Module tests

## Description

Ce dossier contient les tests automatisés de la calculatrice. Ils permettent de vérifier les opérations mathématiques, le traitement des expressions et le fonctionnement de l'interface Flask.

## Fichiers

- **`test_operators.py`** : vérifie les quatre opérations mathématiques ainsi que le comportement de la division par zéro.
- **`test_app.py`** : teste la validation des expressions, les requêtes HTTP et l'affichage des boutons de la calculatrice.

## Dépendances

Les tests utilisent **pytest** et nécessitent **Flask** pour vérifier le fonctionnement de l'application web.

Ils dépendent également des fichiers `app.py`, `operators.py` et `templates/index.html`.

## Exécution des tests

Depuis la racine du projet, installer les dépendances :

```bash
python3 -m pip install flask pytest
```

Pour exécuter tous les tests :

```bash
python3 -m pytest -v
```

Pour exécuter uniquement les tests des opérations mathématiques :

```bash
python3 -m pytest tests/test_operators.py -v
```

Pour exécuter uniquement les tests de l'application :

```bash
python3 -m pytest tests/test_app.py -v
```

## Suivi des bogues

Lorsqu'un test échoue, le problème est documenté dans une Issue GitHub avec les étapes de reproduction et les résultats attendus et obtenus.

Chaque bogue est ensuite corrigé sur une branche distincte. Les tests sont relancés après les corrections pour vérifier leur fonctionnement.