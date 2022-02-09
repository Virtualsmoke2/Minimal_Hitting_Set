import numpy
import numpy as np

def togli_righe(A):
    daEliminare = []
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if controlloRighe(A[i],A[j]):
                daEliminare.append(i)
            elif controlloRighe(A[j],A[i]):
                daEliminare.append(j)
    daEliminare = list(dict.fromkeys(daEliminare))
    A = np.delete(A, daEliminare, 0)
    return A


def controlloRighe(i,j):
    for x in range(0,len(i)):
        if j[x]==1 and i[x]==0:
            return False
    return True

def togli_colonne(M,A):
    a = np.sum(A,0)
    Mnew=[]
    daEliminare=[]
    i=0
    for v in a:
        if v!=0 : Mnew.append(M[i])
        else : daEliminare.append(i)
        i=i+1

    A = np.delete(A, daEliminare, 1)
    return Mnew,A

def controlloCorrettezzaBenchmark(A,M):
    if (len(A[0])!=len(M)):
        M.append('patch')
    return M
