while True:
    o = 82
    pm = 35
    so = 200
    no = 213
    co = 30
    r = 0
    print("1. Ozone(O3)")
    print("2. Particules fines(PM2,5)")
    print("3. Dioxyde de soufre (SO2)")
    print("4. Dioxyde d'azote (NO2)")
    print("5. Monoxyde de carbone (CO)")
    print("0. Exit")

    choix = int(input("Veuillez faire le choix de votre contaminant.\n"))

    if choix == 1:
        r = int(input("Veuillez inserer la concentrations du contaminant."))
        print("La concentration est: ", (r/o)*50," ppb\n")
    elif choix == 2:
        r = int(input("Veuillez inserer la concentrations du contaminant.\n"))
        print("La concentration est: ", (r/pm)*50," ug/m3\n")
    elif choix == 3:
        r = int(input("Veuillez inserer la concentrations du contaminant.\n"))
        print("La concentration est: ", (r / so) * 50, " ppb\n")
    elif choix == 4:
        r = int(input("Veuillez inserer la concentrations du contaminant.\n"))
        print("La concentration est: ", (r / no) * 50, " ppb\n")
    elif choix == 5:
        r = int(input("Veuillez inserer la concentrations du contaminant.\n"))
        print("La concentration est: ", (r / co) * 50, " ppm\n")
    elif choix == 0:
        break
    else:
        print("Le choix",choix,"est invalid, veuillez reessayer. \n")