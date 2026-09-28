"""Après le rendu du site, retire les feuilles de style Bootstrap de la page d'accueil.

Quarto ajoute Bootstrap à toutes les pages d'un site (nécessaire à la navigation
des séances). L'accueil est une affiche avec sa propre feuille (print.css) :
on lui enlève Bootstrap pour que son rendu et son impression restent
identiques à ceux de l'affiche autonome.
"""
import re
from pathlib import Path

page = Path("_site/index.html")
html = page.read_text(encoding="utf-8")
html = re.sub(r'<link[^>]*site_libs/bootstrap/[^>]*>\s*', '', html)
page.write_text(html, encoding="utf-8")
print("index.html : feuilles Bootstrap retirées")
