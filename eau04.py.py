#Prochain nombre premier
#Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


import sys 

argument = sys.argv[1]
result = 0

def nombre_premier(n): 
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


try:
    argument = int(sys.argv[1])
    result = argument + 1
    while not nombre_premier(result):
        result += 1
    print(result)
except ValueError:
    print("Error")
