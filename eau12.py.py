#Tri à bulle
#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.


#Vous utiliserez une fonction de cette forme (selon votre langage) :
#my_bubble_sort(array) {
	# votre algorithme
#	return (new_array)
#}


import sys

def my_bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if all(is_int(arg) for arg in sys.argv[1:]):
    result = my_bubble_sort([int(arg) for arg in sys.argv[1:]])
    print(' '.join(str(arg) for arg in result))
else:
    print("Error")

