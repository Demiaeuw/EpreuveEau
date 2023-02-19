#Suite de Fibonacci
#Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.



#Definir la suite de Fibonacci
#l'intégré dans une liste
#gerer la demande d'argument en lien avec la liste

import sys 

argument = sys.argv[1]

def fibonacci(n):               #Definir la suite de Fibonacci
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence
    
def areInt(x):                    #Verif si c'est un int()
    if isinstance(x, int):
        return True
    else:
        return False


try:
    if areInt(argument):
        demand = int(sys.argv[1]) + 1      #Demande de l'argument Pour stop la suite
        result = fibonacci(demand)
        
        if int(sys.argv[1]) < 0:
            print("-1")
        else:
            print(result[-1])
    
    else:
        print("-1")

except ValueError:
    print("error")

