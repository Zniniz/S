fin = False
valeurSaisie = 0
moyenne = 0

while not fin:
    entier = int(input("Entrez un entier positif: "))
    if entier ==0:
        if valeurSaisie == 0:
            print("PAS DE NOMBRE")
        else:
            moyenne = moyenne/valeurSaisie
            print("Moyenne :", moyenne)
            fin = True
    elif entier<0:
        print("ERREUR")
    elif entier > 0:
        valeurSaisie+=1
        moyenne+=entier