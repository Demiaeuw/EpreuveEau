#Tri par sélection
#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.


#Vous utiliserez une fonction de cette forme (selon votre langage) :
#my_bubble_sort(array) {
	# votre algorithme
#	return (new_array)
#}
import sys 

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if all(is_int(arg) for arg in sys.argv[1:]):
    result = selection_sort([int(arg) for arg in sys.argv[1:]])
    print(' '.join(str(arg) for arg in result))
else:
    print("Error")