while True:
    vend = 10/100
    rep = 20/100
    prod = 5
    manu = 100
    r = 0
    print("1. Département de commerce. (C)")
    print("2. Département de production.(P)")
    print("3. Sortir du programme.(E)")

    choix = str(input("Veuillez faire le choix de votre département.\n"))

    if choix == "C":
        print("1. Représentants")
        print("2. Vendeurs")
        print("3. Sortir du programme.(E)")
        choix2 = str(input("Veuillez faire le choix de votre employé.\n"))
        if choix2 == "R":
            r = int(input("Veuillez inserer le chiffre d'affaire realiser mensuellement."))
            print("Le salaire est: ", (r*rep)+1400,"$\n")
        if choix2 == "V":
            r = int(input("Veuillez inserer le chiffre d'affaire realise mensuellement."))
            print("Le salaire est: ", (r*vend)+1000,"$\n")
        elif choix == "E" or choix2 == "E":
            exit()

    elif choix == "P":
        print("1. Producteurs")
        print("2. Affectes a la manutention")
        print("3. Sortir du programme.(E)")
        choix2 = str(input("Veuillez faire le choix de votre employé.\n"))
        if choix2 == "P":
            r = int(input("Veuillez inserer le nombre d'unites produits mensuellement."))
            print("Le salaire est: ", (r * prod), "$\n")
        if choix2 == "M":
            r = int(input("Veuillez inserer le nombre d'heure de travail mensuel."))
            print("Le salaire est: ", (r * manu), "$\n")
        elif choix == "E" or choix2 == "E":
            exit()

    elif choix == "E":
        exit()
    else:
        print("Le choix",choix,"est invalid, veuillez reessayer. \n")
