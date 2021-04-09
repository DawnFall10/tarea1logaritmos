import time

def exec_search (filename, pattern, funcname, func, printBool):
    try:
        # Validate arguments:
        if filename[-4:] != ".txt":
            raise FileNotFoundError("Error: el archivo debe ser formato .txt")
        elif pattern == "":
            raise SyntaxError("Error: el patrón ingresado debe contener al menos un caracter")

        # Open file and execute function
        text = open(filename, encoding='utf-8')
        tic1 = time.process_time()
        result = func(text.read(), pattern)
        tic2 = time.process_time()
        text.close()

        delta = tic2 - tic1
        if printBool:
            print("--", funcname, "--")
            print("Apariciones del patrón:\t\t\t\t", len(result))
        return delta

    except:
        print(">:c")
        raise

