#Majuscule sur deux
#Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.
import sys 

argument = sys.argv[1]

def alterne_maj_min(chaine):
    result = ""
    majuscule = chaine[0].isupper()
    for i, c in enumerate(chaine):
        if c.isdigit():
            print("Error")
            return ""
        else:
            if i == 0:
                result += c.upper()
                majuscule = not majuscule
            elif c.isalpha():
                if majuscule:
                    result += c.upper()
                else:
                    result += c.lower()
                majuscule = not majuscule
            else:
                result += c
    return result

print(alterne_maj_min(argument))
