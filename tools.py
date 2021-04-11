import time
ROUND_BY = 6

def exec_search (filename, pattern, funcname, func, repeat):
    try:
        # Validate arguments:
        if filename[-4:] != ".txt":
            raise FileNotFoundError("Error: el archivo debe ser formato .txt")
        elif pattern == "":
            raise SyntaxError("Error: el patrón ingresado debe contener al menos un caracter")

        # Open file and execute function:
        text = open(filename, encoding='utf-8')
        alg_list = []
        for i in range(0,repeat):
            text.seek(0)
            tic1 = time.process_time()
            result = func(text.read(), pattern)
            tic2 = time.process_time()
            alg_time = tic2 - tic1
            alg_list.append(alg_time)
        text.close()

        # Printing data:
        alg_prom = round(sum(alg_list)/len(alg_list), ROUND_BY)
        total_time = round(sum(alg_list), ROUND_BY)
        print("--", funcname, "--")
        print("Apariciones del patrón:\t\t\t\t", len(result))
        print("Tiempo de ejecución promedio (segundos):\t", alg_prom)
        print("Tiempo de ejecución total (segundos):\t\t", total_time)
        return alg_prom

    except:
        print(">:c")
        raise

