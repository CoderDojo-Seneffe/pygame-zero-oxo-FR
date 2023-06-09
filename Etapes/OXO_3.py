WIDTH = 650
HEIGHT = 650

TAILLE_CASE = 150
GAUCHE_GRILLE = 100
DROITE_GRILLE = GAUCHE_GRILLE + 3 * TAILLE_CASE
HAUT_GRILLE = 150
BAS_GRILLE = HAUT_GRILLE + 3 * TAILLE_CASE

def draw():
    screen.clear()
    screen.draw.line((GAUCHE_GRILLE + TAILLE_CASE, HAUT_GRILLE), (GAUCHE_GRILLE + TAILLE_CASE, BAS_GRILLE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE + 2 * TAILLE_CASE, HAUT_GRILLE), (GAUCHE_GRILLE + 2 * TAILLE_CASE, BAS_GRILLE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE, HAUT_GRILLE + TAILLE_CASE), (DROITE_GRILLE, HAUT_GRILLE + TAILLE_CASE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE, HAUT_GRILLE + 2 * TAILLE_CASE), (DROITE_GRILLE, HAUT_GRILLE + 2 * TAILLE_CASE), (255, 255, 255))

    screen.draw.textbox("X", Rect(GAUCHE_GRILLE, HAUT_GRILLE, TAILLE_CASE, TAILLE_CASE))
    screen.draw.textbox("O", Rect(GAUCHE_GRILLE + TAILLE_CASE, HAUT_GRILLE + TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))