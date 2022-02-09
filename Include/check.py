def check(A,a,M):
    counter=0
    i=0
    save_char = None
    vett_rapp=[]
    for x in A:
        for y in a:
            counter += x[M.index(y)]
            if x[M.index(y)]==1: save_char=y
        if counter==0 : vett_rapp.append(None)
        elif counter==1 : vett_rapp.append(save_char)
        elif counter>1 : vett_rapp.append('x')
        counter=0
    noneCheck=False
    res = []
    for val in vett_rapp:
        if val != None and val !='x':
            res.append(val)
        elif val==None:
            noneCheck=True
    vett_rapp=res
    vett_rapp = list(dict.fromkeys(vett_rapp)) #rimuove duplicati
    if len(a)==len(vett_rapp) and not noneCheck: return 'mhs'
    elif len(a)==len(vett_rapp) and noneCheck: return 'ok'
    else : return 'ko'



# A=[[1,1,1,0,0,0],
#     [0,1,1,1,0,1],
#     [0,1,1,0,0,0],
#     [1,0,1,0,0,1],
#     [1,1,1,1,0,0],
#     [0,1,1,1,0,1],
#     [0,0,1,1,0,0]]
# M=['a','b','c','d','e','f']
# a=['c']
# print(check(A,a,M))
