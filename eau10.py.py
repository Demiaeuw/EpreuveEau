#Index wanted
#Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est cornstitué de tous les aguments sauf le dernier.
#L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.*


import sys

argument_test = sys.argv[-1]
argument = sys.argv[1:-1]


try:
    print(argument.index(argument_test))
    sys.exit()
except ValueError:
    print("-1")
    sys.exit()