#Combinaisons de 2 nombres
#Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


for i in range(100):
    for k in range(100):
        if i != k:
            chaineFormatI = "{:02d}".format(i)
            chaineFormatK = "{:02d}".format(k)
            nombre = str(chaineFormatK) + " " + str(chaineFormatI)
            print(nombre)
print()


