#Suite de Fibonacci
#Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.



#Definir la suite de Fibonacci
#l'intégré dans une liste
#gerer la demande d'argument en lien avec la liste

import sys 



def fibonacci(n):               #Definir la suite de Fibonacci
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        return fibonacci_sequence
    


try:
    argument = int(sys.argv[1])
    demand = argument + 1      #Demande de l'argument Pour stop la suite
    result = fibonacci(demand)
    
    if argument < 0:
        print("-1")
    else:
        print(result[-1])
    
   

except ValueError:
    print("-1")

