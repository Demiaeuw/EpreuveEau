#Majuscule
#Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules. 
#Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.

import sys

argument = sys.argv[1]

def maj(chain):
    result = ""

    for c in (chain):
        if c.isdigit():
            print("Error")
            return ""
        else:
            if " " and "\t" and "\n":
                result += c.upper()
            else:
                result = c


print(maj(argument))
        