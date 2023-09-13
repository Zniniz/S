#Écrire(« Nombre d'étudiants inscrits ? »)
#NbreEtudIns=lire(NbreEtudIns)
#Écrire(« Nombre d'étudiants inscrits = », NbreEtudIns)
'''Écrire(« Nombre d'étudiants présents ? »)
NbreEtuPre=lire(NbreEtuPre)
Écrire(« Nombre d'étudiants présents = », NbreEtuPre)
PourcentagePre= NbreEtuPre*100/ NbreEtudIns
Écrire(« Pourcentage de présences = », PourcentagePre)
'''


print("Nombre d'étudiants présents ?")
NbreEtuPre=int(input())
print("Nombre d'étudiants présents =", NbreEtuPre)
print("Nombre d'étudiants inscrits ?")
NbreEtudIns=int(input())
print("Nombre d'étudiants inscrits =", NbreEtudIns)
PourcentagePre= NbreEtuPre*100/ NbreEtudIns
print("Pourcentage de présences =",PourcentagePre,"%")