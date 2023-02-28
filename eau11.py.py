#Différence minimum absolue
#Créez un programme qui affiche la différence minimum absolue entre deux éléments d’un tableau constitué uniquement de nombres. Nombres négatifs acceptés.


import sys 

argument = sys.argv[1:]

if len(argument) < 2:
    print("Error")
    sys.exit()

nombre = []

for arg in argument:
    try:
        num = int(arg)
        nombre.append(num)
    except ValueError:
        print("Error")
        sys.exit(1)

difference = nombre[1] - nombre[0]
if difference < 0:
    difference = -difference
for i in range(len(nombre)):
    for j in range(i+1, len(nombre)):
        diff = nombre[j] - nombre[i]
        if diff < 0:
            diff = -diff
        if diff < difference:
            difference = diff


print(difference)