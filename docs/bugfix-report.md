# Rapport de correction de bogues

Ce rapport documente la correction des sept bogues signalés dans les issues GitHub #1 à #7
du dépôt `chaimaamesbah/LOG3000_TP3_23`. Chaque correctif a été développé sur une branche
dédiée créée à partir de la base commune `test/operations-et-interface` (commit `d90e63b`),
qui est la seule branche contenant à la fois le code, la documentation et les tests
(`tests/test_operator.py`, `tests/test_app.py`) nécessaires pour reproduire et valider chaque
bogue.

## Méthodologie

Pour chaque issue :
1. Création de la branche depuis `origin/test/operations-et-interface`.
2. Reproduction du bogue à l'aide du test pytest associé (échec confirmé).
3. Application du correctif minimal et ciblé à l'issue.
4. Relance du test concerné : succès confirmé.
5. Commit explicite contenant uniquement ce correctif.
6. Push de la branche vers GitHub (`git push -u origin <branche>`).

## Tableau récapitulatif

| Issue | Branche | Bogue corrigé | Fichier(s) modifié(s) | Test exécuté | Résultat réel | Commit |
|---|---|---|---|---|---|---|
| #1 | `fix/issue-1-soustraction` | `subtract(a, b)` retournait `b - a` au lieu de `a - b` (résultat inversé, ex. `subtract(10, 3)` → `-7`) | `operators.py` | `tests/test_operator.py::test_subtraction` | PASSED (échouait avant : `assert -7 == 7`) | `62be1a9` |
| #2 | `fix/issue-2-multiplication` | `multiply(a, b)` effectuait `a ** b` (exponentiation) au lieu de `a * b`, ex. `multiply(3, 4)` → `81` | `operators.py` | `tests/test_operator.py::test_multiplication` | PASSED (échouait avant : `assert 81 == 12`) | `b98a024` |
| #3 | `fix/issue-3-division` | `divide(a, b)` utilisait la division entière `a // b` au lieu de `a / b`, ex. `divide(7, 2)` → `3` | `operators.py` | `tests/test_operator.py::test_division` | PASSED (échouait avant : `assert 3 == 3.5`) | `da86241` |
| #4 | `fix/issue-4-bouton-2` | Le bouton du chiffre 2 affichait le texte `02` au lieu de `2` | `templates/index.html` | `tests/test_app.py::test_button_label[2]` | PASSED (texte attendu `2` absent avant correction) | `f214337` |
| #5 | `fix/issue-5-bouton-8` | Le bouton du chiffre 8 affichait le texte `88` au lieu de `8` | `templates/index.html` | `tests/test_app.py::test_button_label[8]` | PASSED (texte attendu `8` absent avant correction) | `d52de4b` |
| #6 | `fix/issue-6-bouton-multiplication` | Le bouton de multiplication n'affichait aucun symbole | `templates/index.html` | `tests/test_app.py::test_button_label[*]` | PASSED (symbole `*` absent avant correction) | `c6a8105` |
| #7 | `fix/issue-7-bouton-division` | Le bouton de division n'affichait aucun symbole | `templates/index.html` | `tests/test_app.py::test_button_label[/]` | PASSED (symbole `/` absent avant correction) | `5b20881` |

## Détails par issue

### Issue #1 — Correction du calcul de soustraction
- **Cause** : dans `operators.py`, la fonction `subtract(a, b)` retournait `b - a`, inversant
  l'ordre des opérandes et donc le signe du résultat.
- **Correctif** : remplacement par `return a - b`.
- **Validation** : `python3 -m pytest tests/test_operator.py::test_subtraction -v` → 1 passed.
- **Commit** : `62be1a9` — *fix(operators): corrige l'inversion des opérandes dans subtract (#1)*

### Issue #2 — Correction du calcul de multiplication
- **Cause** : la fonction `multiply(a, b)` utilisait l'opérateur `**` (exponentiation) au lieu
  de `*` (multiplication).
- **Correctif** : remplacement par `return a * b`.
- **Validation** : `python3 -m pytest tests/test_operator.py::test_multiplication -v` → 1 passed.
- **Commit** : `b98a024` — *fix(operators): corrige multiply qui effectuait une exponentiation (#2)*

### Issue #3 — Correction du calcul de division
- **Cause** : la fonction `divide(a, b)` utilisait l'opérateur `//` (division entière), ce qui
  supprimait la partie décimale du résultat.
- **Correctif** : remplacement par `return a / b`.
- **Validation** : `python3 -m pytest tests/test_operator.py::test_division -v` → 1 passed.
- **Commit** : `da86241` — *fix(operators): corrige divide qui utilisait la division entière (#3)*

### Issue #4 — Correction de l'affichage du bouton 2
- **Cause** : dans `templates/index.html`, le texte affiché du bouton du chiffre 2 était `02`
  au lieu de `2`.
- **Correctif** : correction du texte du bouton en `2`.
- **Validation** : `python3 -m pytest tests/test_app.py -k "test_button_label and 2" -v` → test
  `test_button_label[2]` passed.
- **Commit** : `f214337` — *fix(ui): corrige l'affichage du bouton 2 qui montrait 02 (#4)*

### Issue #5 — Correction de l'affichage du bouton 8
- **Cause** : dans `templates/index.html`, le texte affiché du bouton du chiffre 8 était `88`
  au lieu de `8`.
- **Correctif** : correction du texte du bouton en `8`.
- **Validation** : `python3 -m pytest tests/test_app.py -k "test_button_label and 8" -v` → test
  `test_button_label[8]` passed.
- **Commit** : `d52de4b` — *fix(ui): corrige l'affichage du bouton 8 qui montrait 88 (#5)*

### Issue #6 — Correction de l'affichage du bouton de multiplication
- **Cause** : le bouton de multiplication dans `templates/index.html` n'avait aucun texte,
  rendant son rôle impossible à identifier visuellement.
- **Correctif** : ajout du symbole `*` comme texte du bouton.
- **Validation** : `python3 -m pytest "tests/test_app.py::test_button_label[*]" -v` → 1 passed.
- **Commit** : `c6a8105` — *fix(ui): ajoute le symbole manquant sur le bouton de multiplication (#6)*

### Issue #7 — Correction de l'affichage du bouton de division
- **Cause** : le bouton de division dans `templates/index.html` n'avait aucun texte, rendant
  son rôle impossible à identifier visuellement.
- **Correctif** : ajout du symbole `/` comme texte du bouton.
- **Validation** : `python3 -m pytest "tests/test_app.py::test_button_label[/]" -v` → 1 passed.
- **Commit** : `5b20881` — *fix(ui): ajoute le symbole manquant sur le bouton de division (#7)*

## Vérification d'indépendance des branches

Chaque branche part de la même base commune (`origin/test/operations-et-interface`,
commit `d90e63b`) et ne contient qu'un seul commit en avance sur cette base, modifiant
uniquement le fichier concerné par son issue :

| Branche | Commits en avance sur la base | Fichier(s) modifié(s) |
|---|---|---|
| `fix/issue-1-soustraction` | 1 | `operators.py` |
| `fix/issue-2-multiplication` | 1 | `operators.py` |
| `fix/issue-3-division` | 1 | `operators.py` |
| `fix/issue-4-bouton-2` | 1 | `templates/index.html` |
| `fix/issue-5-bouton-8` | 1 | `templates/index.html` |
| `fix/issue-6-bouton-multiplication` | 1 | `templates/index.html` |
| `fix/issue-7-bouton-division` | 1 | `templates/index.html` |

Aucune branche ne contient le correctif d'une autre issue. Aucune Pull Request n'a été créée,
aucune branche n'a été fusionnée et aucune issue n'a été fermée dans le cadre de ce travail.
