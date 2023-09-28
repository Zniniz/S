nombre1 = int(input("Nombre 1: "))
nombre2 = int(input("Nombre 2: "))

somme = 0
if nombre1<=nombre2:
    for i in range(nombre1, nombre2+1):
        somme+=i
elif nombre2<=nombre1:
    for i in range(nombre2, nombre1+1):
        somme+=i

print("Somme: ", somme)