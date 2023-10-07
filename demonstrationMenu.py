print("1. figure de 2D")
print("2. figure de 3D")
print("3.sortir")
choix=int(input("tapez 1 pour les figures de 2D, 2 pour les figures de 3D ou tapez 3 pour sortir du programme"))
if(choix==1):
    print("1. Cercle")
    print("2. Rectangle")
    print("3. sortir")
    choix2d=int(input("tapez 1 pour un cercle, 2 pour un rectangle ou tapez 3 pour sortir du programme"))
    if(choix2d==1):
        print("1. surface du cercle")
        print("2. périmètre du cercle")
        print("3. sortir ")
        choixparam=int(input("tapez 1 pour calculer la surface, 2 pour calculer le périmètre ou tapez 3 pour sortir du programme"))
        if(choixparam==1 or choixparam==2):
            rayon=float(input("veuillez saisir le rayon"))
            if(choixparam==1):
                surface=3.14*rayon**2
                print("la surface de cercle dont le rayon égal à", rayon ," est ",surface)
            elif(choixparam==2):
                perimetre = 3.14 * rayon * 2
                print("le périmètre du cercle dont le rayon égalà", rayon, " est ", perimetre)
            elif(choixparam==3):
                exit()
    elif (choix2d == 2):
               print("1. surface d'un rectangle")
               print("2. périmètre d'un rectangle")
               print("3. sortir ")
               choixparamrectangle=int(input("taper 1 pour la surface d'un rectangle ou 2 pour le perimetre d'un rectangle ou tapez 3 pour sorir"))
               if(choixparamrectangle==1 or choixparamrectangle==2):
                   largeur=float(input("largeur"))
                   longueur=float(input("longueur"))
                   if(choixparamrectangle==1):
                       surfacerect=largeur*longueur
                       print("la surfcae de ce rectangle égale ",surfacerect)
                   elif(choixparamrectangle==2):
                       perimetre=2*(largeur+longueur)
                       print("le périmètre de ce rectangle égale ", perimetre)

                   elif (choixparamrectangle == 3):
                       exit()




