# Définir la taille du tableaux
TAILLE = 1000

# Instructions
instructions = [
    ("on", 887, 9, 959, 629),
    ("on", 454, 398, 844, 448),
    ("off", 539, 243, 559, 965),
    ("off", 370, 819, 676, 868),
    ("off", 145, 40, 370, 997),
    ("off", 301, 3, 808, 453),
    ("on", 351, 678, 951, 908),
    ("toggle", 720, 196, 897, 994),
    ("toggle", 831, 394, 904, 860),
]

# Creation de la grille (booléen)
grille = []
for i in range(TAILLE):
    ligne = [False] * TAILLE
    grille.append(ligne)

# Exécution
for turn, x1, y1, x2, y2 in instructions:
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):

            if turn == "on":
                grille[x][y] = True
            elif turn == "off":
                grille[x][y] = False
            elif turn == "toggle":
                grille[x][y] = not grille[x][y]

# Lumiere allumées TOTAL
lumiere_allumee = 0

for x in range(TAILLE):
    for y in range(TAILLE):
        if grille[x][y] == True:
            lumiere_allumee = lumiere_allumee + 1
        
print("Lumiere allumées :", lumiere_allumee)
