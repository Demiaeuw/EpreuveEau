#Suite de Fibonacci
#Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.



#Definir la suite de Fibonacci
#l'intégré dans une liste
#gerer la demande d'argument en lien avec la liste



result = 0
listeFibonacci = []

def Fibonacci():
    if result == 0:
        result += result
    else:
        result = result + result 
    print(result)

