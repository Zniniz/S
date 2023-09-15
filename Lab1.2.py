AUGMENTATION = 0.03

ancienSalaire = float(input("Entrez l'ancien salaire annuel ($): "))

newSalaireAnn = ancienSalaire + (ancienSalaire * AUGMENTATION)

newSalaireMens = round(newSalaireAnn / 12 , 2)

montantRetro = round((ancienSalaire / 12) * 9 * AUGMENTATION , 2)

print("Le nouveau salaire : {0} $\n"
      "Nouveau salaire mensuelle : {1} $\n"
      "Montant retro : {2} $"
      .format(newSalaireAnn, newSalaireMens, montantRetro))