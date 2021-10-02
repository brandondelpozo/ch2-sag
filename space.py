"""
Part 1
una función que devuelve un arreglo de enteros con los pares a la izquierda 
y los impares a la derecha. El input es un arreglo de enteros.

Pseudocode
array given
set function get the array given in its parameter
extract odd numbers and asigne them to an array
extract even numbers and asign them to an array
unify both array with even on the left and odd on the right
return array unified

arrayNums = [1,2,3,4,35,12,52,128,256,512]
"""

def sortArrayEvenLeftAndOddRight(arrayNums):
    arrayLeft = []
    arrayRigh = []
    for i in arrayNums:
        if i % 2 == 0:
            arrayLeft.append(i)
        else:
            arrayRigh.append(i) # O(n^2)
    return arrayLeft + arrayRigh

print(sortArrayEvenLeftAndOddRight([1,2,3,4,35,12,52,128,256,512]))