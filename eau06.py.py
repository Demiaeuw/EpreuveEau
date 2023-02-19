#Majuscule sur deux
#Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.

import sys

argument = sys.argv[1]










try:
    argument = str(sys.argv[1])
    if len(argument) != 2:
        print("error")
    else:
        print(result)
except ValueError:
    print("error")