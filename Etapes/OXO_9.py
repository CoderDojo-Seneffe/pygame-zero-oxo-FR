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
gagnant = ''

def draw():
    screen.clear()
    screen.draw.line((GAUCHE_GRILLE + TAILLE_CASE, HAUT_GRILLE), (GAUCHE_GRILLE + TAILLE_CASE, BAS_GRILLE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE + 2 * TAILLE_CASE, HAUT_GRILLE), (GAUCHE_GRILLE + 2 * TAILLE_CASE, BAS_GRILLE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE, HAUT_GRILLE + TAILLE_CASE), (DROITE_GRILLE, HAUT_GRILLE + TAILLE_CASE), (255, 255, 255))
    screen.draw.line((GAUCHE_GRILLE, HAUT_GRILLE + 2 * TAILLE_CASE), (DROITE_GRILLE, HAUT_GRILLE + 2 * TAILLE_CASE), (255, 255, 255))

    for i, ligne in enumerate(grille):
        for j, case in enumerate(ligne):
            screen.draw.textbox(case, Rect(GAUCHE_GRILLE + i * TAILLE_CASE, HAUT_GRILLE + j * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    if gagnant == '-':
        screen.draw.text('Eglalité!', (10, 30))
    elif gagnant != '':
        screen.draw.text(gagnant + ' a gagné!', (10, 30))

def on_mouse_down(pos):
    global joueur, gagnant

    if gagnant != '':
        return

    x = pos[0]
    y = pos[1]
    if x < GAUCHE_GRILLE or x >= DROITE_GRILLE:
        return
    if y < HAUT_GRILLE or y >= BAS_GRILLE:
        return

    if grille[(x - GAUCHE_GRILLE) // TAILLE_CASE][(y - HAUT_GRILLE) // TAILLE_CASE] != ' ':
        return
    grille[(x - GAUCHE_GRILLE) // TAILLE_CASE][(y - HAUT_GRILLE) // TAILLE_CASE] = joueur

    if gagne(joueur):
        gagnant = joueur
        return

    if len(cases_disponibles()) == 0:
        gagnant = '-'
        return

    if joueur == 'X':
        joueur = 'O'
    else:
        joueur = 'X'

def gagne(pion):
    if grille[0][0] == grille[0][1] == grille[0][2] == pion \
        or grille[1][0] == grille[1][1] == grille[1][2] == pion \
        or grille[2][0] == grille[2][1] == grille[2][2] == pion \
        or grille[0][0] == grille[1][0] == grille[2][0] == pion \
        or grille[0][1] == grille[1][1] == grille[2][1] == pion \
        or grille[0][2] == grille[1][2] == grille[2][2] == pion \
        or grille[0][0] == grille[1][1] == grille[2][2] == pion \
        or grille[0][2] == grille[1][1] == grille[2][0] == pion:
        return True
    return False

def cases_disponibles():
    cases = []
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                cases.append((i, j))
    return cases
