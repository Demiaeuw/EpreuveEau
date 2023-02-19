#Prochain nombre premier
#Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


import sys

def nombre_premier(n):      #test nombre premier
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

