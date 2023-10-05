t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']

for indice, nbrJour in enumerate(t1):
    t2.insert( 2*nbrJour+1 , nbrJour )

print(t2)