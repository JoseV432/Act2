import numpy as np 
SEPARADOR = ("*" * 20) + "/n"

#mayore a 3
arreglo_uni = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arreglo_uni)
print(SEPARADOR)

menores_a_5 = arreglo_uni[arreglo_uni < 5]
print(menores_a_5)
print(SEPARADOR)

mayoress_a_5 = arreglo_uni[arreglo_uni > 5]
print(mayoress_a_5)
pass