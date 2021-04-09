import sys
import time
from collections import defaultdict


def boyer_moore_horspool(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    skip = defaultdict(lambda: m)
    found_indexes = []

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            found_indexes.append(i + 1)

        k += skip[ord(text[k])]

    return found_indexes

# Main
texto = open('textfiles/worksEdgarAllanPoe.txt', encoding='utf-8')
pattern = sys.argv[1]
result = boyer_moore_horspool(pattern, texto.read())
tic = time.process_time()
print("Búsqueda en Texto - BMH")
print("Apariciones del patrón", "\'"+pattern+"\'", ":\t",len(result))
print("Tiempo de ejecución (segundos):\t\t", tic)
