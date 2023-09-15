#Constante
sauParPaq = 12

nbrEtudiantInfo = int(input("Entrez le nombre d'etudiants: "))

nbrHotprev = int(input("Entrez le nombre de hot-dog prevu par etudiants: "))
#Calcul
nbSau = nbrEtudiantInfo * nbrHotprev
paquetDeSau = nbSau // sauParPaq
sauIndividu = nbSau % sauParPaq

print("Nombre de paquet de saucisse : {0}\n"
      "Nombre de saucisse individuel : {1}\n"
      .format(paquetDeSau,sauIndividu))