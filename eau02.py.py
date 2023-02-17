#Paramètres à l’envers
#Créez un programme qui affiche ses arguments reçus à l’envers.

import sys

arguments = sys.argv[1:]
liste = []


def inverse(a):
    return a[::-1]


for argument in arguments:
    liste.append(argument)


for element in inverse(liste):
    print(element)


