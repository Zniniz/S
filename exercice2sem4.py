a1= "Francais:quatorze:14"
a2="Russe:TCHETJRE:4"
a3="Grec:DUO:2"
a4="Francais:Mille:1000"
a5="Sanskrit:navati:90"
a6="Francais:Deux cent seize mille:216000"
listeVar=[a1,a2,a3,a4,a5,a6]

listVar2=[]

for var in listeVar:
    listVar2.append(
        var.split(':')
    )

nouvEntree = True
while nouvEntree:
    chiffre =str(input("Donne moi le chiffre: "))
    langue=str(input("Entre une langue: "))

    for liste in listVar2:
        if liste[2]==chiffre:
            if liste[0]==langue:
                print(liste[1])


    nouvEntree=str(input("Recommencer? (o/n): "))=="o"

    