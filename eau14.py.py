#Par ordre Ascii
#Créez un programme qui trie les éléments donnés en argument par ordre ASCII.

import sys


if len(sys.argv) < 2:
    print("Error")
    sys.exit()


sorted_args = sorted(sys.argv[1:])


for arg in sorted_args:
    print(arg, end=" ")




