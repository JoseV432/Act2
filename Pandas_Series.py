import numpy as np
import pandas as pd

SEPARADOR = ("*"*20) + "\n"

#Crear una serie con valores iniciales
notas pd.Series ([87, 100, 85, 60, 78])
print(type (notas)) 
print notas
print(SEPARADOR)



#Crear una serie de 6 elementos que tengan el mismo valor
iguales = pd.Series (100, range (6)) 
print(type (iguales))
print(iguales)
print(SEPARADOR)



#Estadísticas Descriptivas para una serie notas.c
print("notas :") notas.meal
print("{notas}") notas.mi
print(f"cantidad = {notas.count()}")
print("media= {notas.mean()}")
print(f"minimo = {notas.min()}")
print(f"máximo = {notas.max()}")
print(f"desviación standard = {notas.std()}")
print("Sumarización descriptiva: ")
print(notas.describe())
print(SEPARADOR)



#Serie con indices personalizados
print("Series con indices personalizados: ")
notas_asignadas = pd.Series([87, 100, 85, 60, 78], index-["Crescencio","Rutilio"])

print (SEPARADOR)
print(notas_asignadas)


#Acceso a elementos en una serie por valor de índice
print ({f"La calificación de Rutilio es (notas_asignadas_dict['Rutilio']}")
print ({f"La calificación de Rutilio es (notas_asignadas_dict.Rutilio}")