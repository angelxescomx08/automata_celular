from threading import Thread

class Hilo(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
        return 

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def reglas(r, n1, n2, n3):
    if n1 == n2 == n3 == 1:
        return r[0]
    if n1 == n2 == 1 and n3 == 0:
        return r[1]
    if n1 == 1 and n2 == 0 and n3 == 1:
        return r[2]
    if n1 == 1 and n2 == 0 and n3 == 0:
        return r[3]
    if n1 == 0 and n2 == 1 and n3 == 1:
        return r[4]
    if n1 == 0 and n2 == 1 and n3 == 0:
        return r[5]
    if n1 == 0 and n2 == 0 and n3 == 1:
        return r[6]
    if n1 == 0 and n2 == 0 and n3 == 0:
        return r[7]

def llenar_estado_inicial(inicial, inicio, fin, op):
    arr = []
    inc = 0
    if op == "+":
        for i in range(inicio, fin):
            arr.append(int(inicial[i]))
    else:
        for i in range(fin, inicio):
            arr.append(int(inicial[i]))
    return arr


def calcular_iteracion(r, i, m, inicio, fin, op):
    arr = []
    if op == "+":
        for j in range(inicio, fin):
            if j == 0:
                arr.append(reglas(r,m[i][len(m[i])-1], m[i][j], m[i][j+1]))
            elif j == len(m[i])-1:
                arr.append(reglas(r,m[i][j-1], m[i][j], m[i][0]))
            else:
                arr.append(reglas(r,m[i][j-1], m[i][j], m[i][j+1]))
    else:
        for j in range(fin, inicio):
            if j == 0:
                arr.append(reglas(r,m[i][len(m[i])-1], m[i][j], m[i][j+1]))
            elif j == len(m[i])-1:
                arr.append(reglas(r,m[i][j-1], m[i][j], m[i][0]))
            else:
                arr.append(reglas(r,m[i][j-1], m[i][j], m[i][j+1]))
    return arr


def crear_matriz_hilos(r, iteraciones, inicial):
    matriz = []
    fin = 0
    if len(inicial)%2 == 0:
        fin = (len(inicial)//2)-1
    else:
        fin = len(inicial)//2
    h1 = Hilo(target=llenar_estado_inicial, args=(inicial, 0,fin+1,"+"))
    h2 = Hilo(target=llenar_estado_inicial, args=(inicial, len(inicial),fin+1,"-"))
    h1.start()
    h2.start()
    arr1 = h1.join()
    arr2 = h2.join()
    matriz.append(arr1+arr2)

    for i in range(0,iteraciones):
        h1 = Hilo(target=calcular_iteracion, args=(r, i, matriz,0,fin+1,"+"))
        h2 = Hilo(target=calcular_iteracion, args=(r, i, matriz,len(inicial),fin+1,"-"))
        h1.start()
        h2.start()
        arr1 = h1.join()
        arr2 = h2.join()
        matriz.append(arr1+arr2)
    return matriz