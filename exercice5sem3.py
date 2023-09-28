petite = 0

for i in range(10):
    entier = int(input("Entrez un entier: "))
    if i == 0:
        petite = entier
    elif entier < petite:
        petite = entier
print("Plus petite valeur est: ", petite)