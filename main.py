import sys
from bmh import boyer_moore_horspool
from kmp import KMP
from tools import exec_search, ROUND_BY

'''
Uso:
python main.py <patrón> <ubicación del texto> <número de iteraciones>

Si no se entrega el número adecuado de parámetros, se asumirá una búsqueda
como la de los Experimentos 3 y 4 (Quijote, pero una sola vez). 

Se retornan los resultados para ambos algoritmos.
*Advertencia: ¡los loops son lentos, no usar números muy grandes!
'''

# Main checking
if len(sys.argv) != 4:
    pattern = "Don Quijote de la Mancha"
    filename = "textfiles/quijoteEsp.txt"
    repeat = 1
else:
    pattern = sys.argv[1]
    filename = sys.argv[2]
    repeat = int(sys.argv[3])

# Start experiment
print("El patrón escogido fue \'" + pattern + "\'.")
print("Se repetirá el experimento", repeat, "veces.")

kmp_prom = exec_search(filename, pattern, "KMP", KMP().search, repeat)
bmh_prom = exec_search(filename, pattern, "BMH", boyer_moore_horspool, repeat)

# Results
if kmp_prom > bmh_prom:
    best = "BMH"
else:
    best = "KMP"

print("-- Resultado --")
dif = abs(kmp_prom - bmh_prom)
print(best, "fue el algoritmo más rápido por una diferencia promedio de", round(dif, ROUND_BY), "segundos.")