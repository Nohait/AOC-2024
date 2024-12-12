import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def mot_potentiel(mot, V0, taille_grille=1000, taille_texte=150):
    # Initialisation de la grille
    grille = np.zeros((taille_grille, taille_grille))
    masque = np.zeros((taille_grille, taille_grille), dtype=bool)

    # Création d'une image avec PIL pour dessiner le mot
    image = Image.new('L', (taille_grille, taille_grille), 0)  # Grille noire
    draw = ImageDraw.Draw(image)

    # Chargement d'une police par défaut
    try:
        font = ImageFont.truetype("arial.ttf", taille_texte)  # Police Arial
    except IOError:
        font = ImageFont.load_default()  # Police par défaut si Arial n'est pas trouvée

    # Calcul des dimensions du texte
    if hasattr(draw, "textbbox"):
        bbox = draw.textbbox((0, 0), mot, font=font)  # Compatible Pillow >= 8.0.0
        largeur_texte, hauteur_texte = bbox[2] - bbox[0], bbox[3] - bbox[1]
    else:
        largeur_texte, hauteur_texte = draw.textsize(mot, font=font)  # Pillow < 8.0.0

    # Position pour centrer le texte
    position = ((taille_grille - largeur_texte) // 2, (taille_grille - hauteur_texte) // 2)

    # Dessiner le mot sur l'image
    draw.text(position, mot, fill=255, font=font)

    # Convertir l'image en tableau numpy
    image_array = np.array(image)

    # Appliquer le potentiel V0 aux pixels correspondant au mot
    grille[image_array > 0] = V0
    masque[image_array > 0] = True

    return grille, masque

# Paramètres du problème
N = 1000  # Taille de la grille
V0 = 10   # Potentiel pour les lettres
mot = "   M P 2\n T O U S\n   D E S\nD I E U X"
mot2 = "M P I"
n_iter = 1000  # Nombre d'itérations

# Initialisation de la grille et des conditions aux limites
potentiels, masque = mot_potentiel(mot, V0, taille_grille=N, taille_texte=150)

# Copie initiale de la grille pour la relaxation
v = potentiels.copy()

# Relaxation itérative
for k in range(n_iter):
    if k % 100 == 0:
        print(f"Progression : {k / n_iter * 100:.2f}%")

    # Mise à jour des potentiels dans la grille
    v_new = v.copy()
    v_new[1:-1, 1:-1] = 0.25 * (v[2:, 1:-1] + v[:-2, 1:-1] + v[1:-1, 2:] + v[1:-1, :-2])

    # Réimposer les conditions aux limites
    v_new[masque] = potentiels[masque]

    # Mise à jour de la grille
    v = v_new

# Visualisation finale
x = np.linspace(0, N, N)
y = np.linspace(0, N, N)
X, Y = np.meshgrid(x, y)
plt.figure(figsize=(10, 10))
plt.contourf(X, Y, np.flipud(v), levels=100, cmap="hot")  # Inversion avec np.flipud
plt.colorbar(label="V")
plt.show()
