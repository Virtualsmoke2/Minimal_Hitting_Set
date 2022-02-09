import os
import time

from main import mainFun,writefile
from preprocessing import togli_righe,togli_colonne,controlloCorrettezzaBenchmark

def fillM(str,M):
    pos=0
    fineCorsa=len(str)
    while True:
        i = str.find('(',pos)
        f = str.find(')',pos)
        if i==-1 : break
        M.append(str[i+1:f])
        pos=f+1
    return M


# basepath = 'benchmarks1/'
# for entry in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath, entry)):
#         print(entry)
#         with open(os.path.join(basepath, entry)) as f:
#             contents = f.readlines()
#             fillM(contents[4])
#             for c in range(5,len(contents)):
#                 A.append([int(x) for x in contents[c].split(' ')[:-1]])
#         #mainFun(M, A)
#         print(A)
#         print(M)

# 1084.452647447586  benchmarks1/c432.020.matrix


def Mbase():
    benchmarks=["c432.020.matrix"]
    for bench in benchmarks:
        directory="benchmarks1/"
        file=bench
        open('workingFile', 'w').close()
        f = open("workingFile", "a")
        f.write(file)
        f.close()
        M = []
        A = []
        with open(directory+file) as f:
            contents = f.readlines()
            M = fillM(contents[4],M)
            for c in range(5,len(contents)):
                A.append([int(x) for x in contents[c].split(' ')[:-1]])

        M = controlloCorrettezzaBenchmark(A,M)

        # t0=time.time()
        # mainFun(M, A,file)
        # t0 = time.time()-t0

        t1=time.time()
        A = togli_righe(A)
        M,A = togli_colonne(M,A)
        mainFun(M, A,file+"OPTIMIZED")
        t1=time.time()-t1

        # writefile("Senza preprocessing ci ha messo : "+str(t0)+"s","Complessita_"+file,'')
        writefile("Con preprocessing ci ha messo : "+str(t1)+"s","Complessita_"+file+"OPTIMIZED",'')
        # writefile("Con il preprocessing l'algoritmo e' piu veloce di : " + str(t0-t1) + "s", "Complessita_" + file + "OPTIMIZED", '')

