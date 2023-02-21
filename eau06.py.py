#Majuscule sur deux
#Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.

import sys

argument = sys.argv[1]
argumentstest = sys.argv[1:] 

result = argument.upper()







try:
    argument = str(sys.argv[1])
    if len(argumentstest) != 1:
        print("trop d'argument")
    else:
        print(argument.upper())
except ValueError:
    print("error")