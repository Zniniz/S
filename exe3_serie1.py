'''
Ecrire(“veuillez saisir nombre d'heures travaillées »)
NbreHeureTra=lire(NbreHeureTra)
Ecrire(“veuillez saisir le taux horaire »)
TauxHoraire=lire(TauxHoraire)
SalaireBrut= NbreHeureTra* TauxHoraire
DeductionFed=0.15* SalaireBrut
DeductionProvi=0.2* SalaireBrut
AssuEmp=0.025* SalaireBrut
RegimeRente=0.02* SalaireBrut
Salairenet= SalaireBrut- DeductionFed- DeductionProvi- AssuEmp- RegimeRente

Ecrire(“Votre salaire net”, Salairenet)
Écrire(« Déduction fédérale », DeductionFed)
Écrire(« Déduction provinciale », DeductionProvi)
Écrire(« Déduction d'assurance emploi », AssuEmp)
Écrire(« Déduction de régime des rentes », RegimeRente)
'''
print("veuillez saisir nombre d'heures travaillées")
NbreHeureTra=float(input())
print("veuillez saisir le taux horaire ")
TauxHoraire=float(input())
SalaireBrut= NbreHeureTra* TauxHoraire
DeductionFed=0.15* SalaireBrut
DeductionProvi=0.2* SalaireBrut
AssuEmp=0.025* SalaireBrut
RegimeRente=0.02* SalaireBrut
Salairenet= SalaireBrut- DeductionFed- DeductionProvi- AssuEmp- RegimeRente

print("Votre salaire net", Salairenet)
print("Déduction fédérale", DeductionFed)
print("Déduction provinciale",DeductionProvi)
print("Déduction d'assurance emploi", AssuEmp)
print("Déduction de régime des rentes", RegimeRente)
