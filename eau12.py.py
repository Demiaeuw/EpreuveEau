#Tri à bulle
#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.


#Vous utiliserez une fonction de cette forme (selon votre langage) :
#my_bubble_sort(array) {
	# votre algorithme
#	return (new_array)
#}


import sys
"""
def my_bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

result = my_bubble_sort(sys.argv[1:])

try:
    result = int(result)
    print(result, end="")
except ValueError:
    print("Error")
    
"""
argument = sys.argv[1:]
argument.sort()
print(argument, end="")