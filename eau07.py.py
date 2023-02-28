#Majuscule
#Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules. 
#Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.

import sys

argument = sys.argv[1]

def capitalize_words(argument):
    words = argument.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

try:
    argument = str(sys.argv[1])
    if len(sys.argv) != 2:
        print("error")
        sys.exit()
    else:
        print(capitalize_words(argument))
except ValueError:
    print("Error")
    sys.exit()