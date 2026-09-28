"""Après le rendu du site, retire les feuilles de style Bootstrap de la page affiche.

Quarto ajoute Bootstrap à toutes les pages d'un site (nécessaire à la navigation
des séances). La page affiche avec sa propre feuille (print.css) :
on lui enlève Bootstrap pour que son rendu et son impression restent
identiques à ceux de l'affiche autonome.
"""
import re
from pathlib import Path

page = Path("_site/affiche.html")
html = page.read_text(encoding="utf-8")
html = re.sub(r'<link[^>]*site_libs/bootstrap/[^>]*>\s*', '', html)
page.write_text(html, encoding="utf-8")
print("affiche.html : feuilles Bootstrap retirées")
