import sys
from bmh import boyer_moore_horspool
from kmp import KMP
from tools import exec_search

if len(sys.argv) != 4:
    pattern = "Quijote"
    filename = "textfiles/quijoteEsp.txt"
    repeat = 1
else:
    pattern = sys.argv[1]
    filename = sys.argv[2]
    repeat = int(sys.argv[3])

print("El patrón escogido fue \'" + pattern + "\'.")
print("Se repetirá el experimento", repeat, "veces.")

kmp_list = []
bmh_list = []

# KMP loop
for i in range(0,repeat):
    kmp_time = exec_search(filename, pattern, "KMP", KMP().search, i==repeat-1)
    kmp_list.append(kmp_time)
kmp_prom = sum(kmp_list)/len(kmp_list)
print("Tiempo de ejecución promedio (segundos):\t", kmp_prom)
print("Tiempo de ejecución total (segundos):\t\t", sum(kmp_list))

# BMH loop
for i in range(0,repeat):
    bmh_time = exec_search(filename, pattern, "BMH", boyer_moore_horspool, i==repeat-1)
    bmh_list.append(bmh_time)
bmh_prom = sum(bmh_list)/len(bmh_list)
print("Tiempo de ejecución promedio (segundos):\t", bmh_prom)
print("Tiempo de ejecución total (segundos):\t\t", sum(bmh_list))

# Results
if kmp_prom > bmh_prom:
    best = "BMH"
else:
    best = "KMP"

print("-- Resultado --")
dif = kmp_prom - bmh_prom
print(best, "fue el algoritmo más rápido por una diferencia promedio de", abs(dif), "segundos.")