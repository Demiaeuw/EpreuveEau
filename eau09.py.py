#Entre min et max
#Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.


import sys 

def nombre(a, b):
    for i in range(a, b):
        print(i + 1, end=" ")



try:
    if len(sys.argv) != 3:
        print("Entré 2 arguments")
    else:
        val1 = int(sys.argv[1])
        val2 = int(sys.argv[2])
        nombre(val1, val2)
except ValueError:
    print("Entré 2 chiffres entier")
