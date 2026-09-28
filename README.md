# Le format texte : libérez vos documents !

Site Quarto des ateliers d'écriture académique au format texte (BU de Pau, UPPA).

- `index.qmd` : l'affiche (page d'accueil), stylée par `print.css`. Les dates du calendrier renvoient vers les séances.
- `seances/` : une page par séance (squelettes à compléter).
- `club.qmd` : présentation du club et des échanges de pratiques.
- `_quarto.yml` : configuration du site. `_brand.yml` : charte de départ (couleurs et police de l'affiche), à affiner.
- `scripts/affiche-sans-bootstrap.py` : retire Bootstrap de la seule page d'accueil après le rendu, pour que l'affiche garde exactement son apparence et son impression.

## Commandes

```bash
quarto preview   # aperçu local avec rechargement automatique
quarto render    # génère le site dans _site/
```

Pour obtenir le PDF de l'affiche : ouvrir `_site/index.html` (ou l'aperçu) dans le navigateur, puis Imprimer → Enregistrer en PDF (A4, marges « aucune », graphiques d'arrière-plan activés).
