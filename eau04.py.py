#Prochain nombre premier
#Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.

#verif argument nombre premier
#créer une liste de nombre premier 
#arreté la liste a la demande
#afficher le suivant 

import sys

argument = sys.argv[1]


def nombre_premier(n):          #verif argument nombre premier
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def liste_premiers(n):          #créer une liste de nombre premier 
    primes = []
    for i in range(2, n):
        if nombre_premier(i):
            primes.append(i)
    return primes


try:
    argument = int(sys.argv[1])     #arreté la liste a la demande
    demand = argument + 1           #!!!!!!!!!! afficher le suivant !!!!!!!!!!!!
    result = liste_premiers(demand)
    if argument < 0:
        print("-1")
    else:
        print(result[-1])
except ValueError:
    print("Entré un entier")