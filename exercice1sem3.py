trouver = False
nombreMystere = 48
nbEssai = 0

while (not trouver) and (nbEssai<=10):
    print("Devine un nombre")
    essai=int(input("Je pense c`est: "))
    if essai == nombreMystere:
        trouver=True
        print("WON")

    elif essai < nombreMystere:
        print("Trop petit")
        nbEssai+=1
    elif essai > nombreMystere:
        print("Trop Gros")
        nbEssai+=1

    if nbEssai == 10:
        print("PERDU")