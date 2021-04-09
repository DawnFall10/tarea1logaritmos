import sys
import time


class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P):
                ret.append(i - (j - 1))
                j = partial[j - 1]

        return ret

# Main
texto = open('textfiles/worksEdgarAllanPoe.txt', encoding='utf-8')
pattern = sys.argv[1]
result = KMP().search(texto.read(), pattern)
tic = time.process_time()
print("Búsqueda en Texto - KMP")
print("Apariciones del patrón", "\'"+pattern+"\'", ":\t",len(result))
print("Tiempo de ejecución (segundos):\t\t", tic)
