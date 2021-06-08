from automata import reglas


def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


def cargar_archivo(ruta):
    archivo = open(ruta, 'r')
    arr = []
    iteraciones = int(archivo.readline())
    regla = archivo.readline()
    if regla[0] == "b":
        for i in range(1, len(regla)-1):
            arr.append(int(regla[i]))
    else:
        binario = binarizar(int(regla))
        for i in range(0, len(binario)):
            arr.append(int(binario[i]))
        if len(arr)<8:
            num = 8 - len(arr)
            for i in range(num):
                arr.insert(0,0)
    inicial = archivo.readline()
    archivo.close()
    return iteraciones, arr, inicial

def guardar_archivo(archivo, iteraciones, r, inicial):
    archivo.write(str(iteraciones)+"\n")
    reglas = "b"
    for i in r:
        reglas += str(i)
    archivo.write(reglas+"\n")
    archivo.write(inicial)
    archivo.close()