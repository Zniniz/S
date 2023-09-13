'''
Ecrire(“Veuillez saisir le prix d’un litre d’essence »)
       PrixLitreEssence=lire(PrixLirteEssence)
       Ecrire(“Veuillez saisir la distance »)
       Distance=lire(Distance)
       Ecrire(“Veuillez saisir la consommation de votre véhicule »)
        ConsoomationVeh=lire(ConsoomationVeh)
       nbreLitreConsommé= Distance* ConsoomationVeh/100
       CoutVoyage= nbreLitreConsommé* PrixLitreEssence
Ecrire(“Le coût de votre voyage est », CoutVoyage)
'''
print("Veuillez saisir le prix d’un litre d’essence")
PrixLitreEssence=float(input())
print("Veuillez saisir la distance")
Distance=float(input())
print("Veuillez saisir la consommation de votre véhicule ")
ConsoomationVeh=float(input())
nbreLitreConsomme= Distance* ConsoomationVeh/100
CoutVoyage= nbreLitreConsomme* PrixLitreEssence
print("Le coût de votre voyage est ", CoutVoyage)
