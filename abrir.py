#from abrir import iterar_archivo

def iterar_archivo(path):
    try:
        with open(path,"r") as archivo:
            for linea in archivo:
                print(linea, end ="")
    except FileNotFoundError:
        print("te has equivocado, prueba otra vez")
    except Exception as e:
        print("Error" + e)
        
iterar_archivo("domains.txt")