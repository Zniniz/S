print("Calcul du cout d'un voyage")
#Entrez les donnees
prixessence = float(input("Entrez un prix ($/L): "))

distance = float(input("Entez la distance du voyage [Km]: "))

consommation = float(input("Entrez la consaommation de votre vehicule [L/100Km]: "))
#Calcul
coutVoyage = round(prixessence * distance * (consommation/100), 2)
#Affichage
print("Cout: {0} $".format(coutVoyage))