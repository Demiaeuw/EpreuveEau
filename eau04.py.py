#Prochain nombre premier
#Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.

#recup argument
#definir le chiffre premier en dessous
#prendre ce chiffre premier comme ref
#affiché le suivant


"""
import sys

argument = int(sys.argv[1])


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


"""


#index

"""

index = len(liste_premiers(argument))       #index
emplacement = index + 1

try:
    argument = int(sys.argv[1])

"""

