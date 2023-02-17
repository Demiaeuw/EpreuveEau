#Combinaisons de 3 chiffres
#Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.




for i in range(10):
    for j in range(10):
        for k in range(10):
            if i != j and i != k and j != k:
                nombre = str(i) + str(j) + str(k)
                print(nombre)
print()
