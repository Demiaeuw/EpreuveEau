#Par ordre Ascii
#Créez un programme qui trie les éléments donnés en argument par ordre ASCII.

import sys


if len(sys.argv) < 2:
    print("Error")
    sys.exit()


sorted_args = sorted(sys.argv[1:])


for arg in sorted_args:
    print(arg, end=" ")



"""
import sys

# Vérification du nombre d'arguments
if len(sys.argv) < 2:
    print("Error")
    sys.exit()

# Tri des arguments par ordre ASCII
for i in range(1, len(sys.argv)):
    min_idx = i
    for j in range(i+1, len(sys.argv)):
        if sys.argv[j] < sys.argv[min_idx]:
            min_idx = j
    if i != min_idx:
        sys.argv[i], sys.argv[min_idx] = sys.argv[min_idx], sys.argv[i]

# Affichage des arguments triés
for i in range(1, len(sys.argv)):
    print(sys.argv[i], end=" ")
"""
