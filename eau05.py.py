#String dans string
#Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.

import sys

val1 = sys.argv[1]
val2 = sys.argv[2]
argumentstest = sys.argv[1:]

try:
    val1 = str(sys.argv[1])
    val2 = str(sys.argv[2])
    if len(argumentstest) != 2:
        print("entrer 2 arguments")
    elif val2 in val1 or val1 in val2:
        print("true")
    else:
        print("false")


except ValueError:
    print("Error")