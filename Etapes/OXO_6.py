WIDTH = 650
HEIGHT = 650

TAILLE_CASE = 150
GAUCHE_GRILLE = 100
DROITE_GRILLE = GAUCHE_GRILLE + 3 * TAILLE_CASE
HAUT_GRILLE = 150
BAS_GRILLE = HAUT_GRILLE + 3 * TAILLE_CASE

grille = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]
joueur = 'X'

def draw():
    screen.clear()
    screen.draw.line((GAUCHE_GRILLE + TAILLE_CASE, HAUT_GRILLE), (GAUCHE_GRILLE + TAILLE_CASE, BAS_GRILLE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE + 2 * TAILLE_CASE, HAUT_GRILLE), (GAUCHE_GRILLE + 2 * TAILLE_CASE, BAS_GRILLE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE, HAUT_GRILLE + TAILLE_CASE), (DROITE_GRILLE, HAUT_GRILLE + TAILLE_CASE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE, HAUT_GRILLE + 2 * TAILLE_CASE), (DROITE_GRILLE, HAUT_GRILLE + 2 * TAILLE_CASE), (255, 255, 255))

    for i, ligne in enumerate(grille):
        for j, case in enumerate(ligne):
            screen.draw.textbox(case, Rect(GAUCHE_GRILLE + i * TAILLE_CASE, HAUT_GRILLE + j * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

def on_mouse_down(pos):
    global joueur

    x = pos[0]
    y = pos[1]
    if x < GAUCHE_GRILLE or x >= DROITE_GRILLE:
        return
    if y < HAUT_GRILLE or y >= BAS_GRILLE:
        return
    grille[(x - GAUCHE_GRILLE) // TAILLE_CASE][(y - HAUT_GRILLE) // TAILLE_CASE] = joueur

    if joueur == 'X':
        joueur = 'O'
    else:
        joueur = 'X'
