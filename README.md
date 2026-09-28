# Le format texte : libérez vos documents !

Site Quarto des ateliers d'écriture académique au format texte (BU de Pau, UPPA).

## Structure

- `index.qmd` : page d'accueil classique (présentation, infos pratiques, tableau des séances).
- `affiche.qmd` : l'affiche (à la place d'une page « À propos »), stylée par `print.css`. Sans menu ni liens vers le dépôt, pour rester une vraie affiche imprimable.
- `seances/` : une page par séance (squelettes à compléter).
- `club.qmd` : le club et les échanges de pratiques.
- `_quarto.yml` : configuration (menu en haut, barre latérale, liens vers le dépôt et la source).
- `_brand.yml` : charte de départ (couleurs et police de l'affiche), à affiner.
- `scripts/affiche-sans-bootstrap.py` : après le rendu, retire Bootstrap de la seule page affiche, pour que son apparence et son impression ne changent pas.

## Avant la première publication

Dans `_quarto.yml`, remplacer `TON-PSEUDO` par l'identifiant GitHub (trois occurrences : `site-url`, `repo-url`, lien de la barre de menu).

## Commandes

```bash
quarto preview            # aperçu local avec rechargement automatique
quarto render             # génère le site dans _site/
quarto publish gh-pages   # publie sur GitHub Pages
```

Le PDF de l'affiche s'obtient en ouvrant la page affiche dans le navigateur, puis Imprimer → Enregistrer en PDF (A4, marges « aucune », graphiques d'arrière-plan activés).
