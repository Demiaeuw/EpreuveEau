#Chiffres only
#Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.


import sys

argument = sys.argv[1]

try:
    argument = int(sys.argv[1])
    if len(sys.argv) != 2:
        print("error")
    else:
        print("true")
except ValueError:
    print("error")