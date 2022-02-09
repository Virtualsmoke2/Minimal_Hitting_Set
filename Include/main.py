from check import check
import numpy
import numpy as np
from sys import getsizeof


def mainFun(M, A, file):
    totMhs = 0
    maxQueue = 0
    # Initializing a queue
    queue = []  # queue.append to add, queue.pop to remove

    for x in M:
        queue.append([x])
    a = []
    ad = []

    for x in M:
        if np.sum(A, 0)[M.index(x)] == len(A):
            writefile(x, file,'')
            totMhs += 1

    while len(queue):
        print("Dimensione coda : " +
              str(getsizeof(queue) / 1000000) + "MB | " +
              str(len(queue)) + " candidati | " +
              str(totMhs) + " MHS trovati")
        if getsizeof(queue) / 1000000 > maxQueue: maxQueue = getsizeof(queue) / 1000000
        a = []
        ad = []
        a.append(queue.pop(0))
        a = [item for sublist in a for item in sublist]
        temp = a[-1]
        for x in range(M.index(temp) + 1, len(M)):
            ad = a.copy()
            e = M[x]
            ad.append(e)
            result = check(A, ad, M)
            if result == 'ok' and e != M[-1]:
                queue.append(list(ad))
            elif result == 'mhs':
                writefile(ad, file)
                totMhs += 1


    writefile("Max queue size : " + str(maxQueue) + "MB", "Complessita_" + file, '')
    writefile("MHS trovati : " + str(totMhs), "Complessita_" + file, '')
    writefile("M : " + str(len(M)), "Complessita_" + file, '')
    writefile("N : " + str(len(A)), "Complessita_" + file, '')


def writefile(str, file='default', space=' '):
    f = open(file, "a")
    str = space.join(str)
    f.write(str)
    f.write("\n")
    f.close()


def getQueue():
    return queue
