# Module static

## Description

Ce répertoire contient les ressources statiques utilisées pour définir l'apparence de la calculatrice.

## Fichiers

- **`style.css`** : définit les couleurs, les dimensions, la disposition des boutons et les effets visuels de l'interface.

## Dépendances et fonctionnement

Le fichier CSS est chargé par `templates/index.html` à l'aide de la fonction `url_for()` de Flask.

Il utilise les classes et identifiants définis dans le HTML, notamment `.calculator`, `.buttons`, `.btn`, `.operator` et `#display`. Toute modification de ces éléments dans le HTML peut donc nécessiter une adaptation du CSS.

Aucune bibliothèque CSS externe n'est nécessaire.