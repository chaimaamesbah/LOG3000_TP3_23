# Module templates

## Description

Ce répertoire contient les fichiers HTML utilisés par Flask pour afficher l'interface de la calculatrice.

## Fichiers

- **`index.html`** : définit l'interface utilisateur, notamment les boutons numériques, les opérateurs et la zone d'affichage. Il contient également les fonctions JavaScript qui permettent de saisir et d'effacer une expression.

## Dépendances et fonctionnement

La page est affichée par le serveur Flask défini dans `app.py`. Elle utilise la variable `result` transmise par le serveur pour afficher le résultat d'un calcul.

Les expressions sont envoyées au serveur à l'aide d'un formulaire HTTP POST. L'apparence de la page dépend du fichier `static/style.css`.