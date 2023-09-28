from random import *

partieGagnee = False
scoreJoueur1 = 0
scoreJoueur2 = 0

while not partieGagnee:
    joueur1 = randint(1,6)
    joueur2 = randint(1,6)
    print("Joueur 1: ",joueur1,", Joueur 2:",joueur2)
    if joueur1 > joueur2:
        scoreJoueur1+=1
        if scoreJoueur1 == 10:
            partieGagnee=True
            gagnant = "Joueur 1"

    elif joueur2 > joueur1:
        scoreJoueur2+=1
        if scoreJoueur2 == 10:
            partieGagnee=True
            gagnant = "Joueur 2"

print("Le gagnant est: ", gagnant)