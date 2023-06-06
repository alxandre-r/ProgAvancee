import random
import sys
import time

def initListePersonnes(n,nf) :
    l=[]
    L = 200
    C = 300
    if nf!="" :
        f = open(nf,"r")
        buffer=f.readline()
        buffer=f.readline()
        L = int(buffer)
        buffer=f.readline()
        buffer=f.readline()
        C = int(buffer)
        buffer=f.readline()
        buffer=f.readline()
        n = int(buffer)
    for i in range(0,n) :
        if nf == "" :
            p = random.randint(50,120)
            v = random.randint(1,5)
        else :
            buffer=f.readline()
            p = int(buffer)
            buffer=f.readline
            v = int(buffer)
        l.append((p,v))
    return (l,L,C)

def simulePassage(l,L,C) :
    t=0
    surLePont=[]
    poidsSurLePont=0
    while l != [] :
        # on peut s'engager
        if poidsSurLePont + l[0][0] <= C :
            #calcul de l'heure de sortie :
            # c'est t + L/l[0][1], sauf s'il y a un bouchon devant
            # dans ce cas c'est la même heure que celui devant
            sortiePrevue = t + float(L)/float(l[0][1])
            if surLePont == [] :
                poidsSurLePont = l[0][0]
                surLePont.append((l[0][0],l[0][1],sortiePrevue))
            else :
                sortiePrec = surLePont[-1][2]
                if sortiePrec > sortiePrevue :
                    sortiePrevue = sortiePrec
                    poidsSurLePont = poidsSurLePont + l[0][0]
                surLePont.append((l[0][0],l[0][1],sortiePrevue))
            l = l[1:]

        else : # il faut attendre
            # on fait sortir une personne et on met à jour le temps de départ possible
            if poidsSurLePont - surLePont[0][0] + l[0][0] < C : # ça suffit à permettre une entrée
                # l'heure de départ seracelle de la sortie
                t = surLePont[0][2]
            # on vide le pont
            poidsSurLePont = poidsSurLePont - surLePont[0][0]
            surLePont = surLePont[1:]
    return surLePont[-1][2]

argc=len(sys.argv)
random.seed()
if argc==3:
    if sys.argv[1] == "-f" : (lcb,L,C) = initListePersonnes(0,sys.argv[2])
    elif sys.argv[1] == "-n" : (lcb,L,C) = initListePersonnes(int(sys.argv[2]),"")
    else:
        print("usage : python3 les_kibitzs_v3.py [-f nomFichier | -n nombre de personnes]")
        sys.exit[1]
else:
    print("usage : python3 les_kibitzs_v3.py [-f nomfichier | -n nombre de personnes]")
    sys.exit(1)

print("###",L,C,lcb)

tmp=lcb[:]
temps = simulePassage(lcb,L,C)
print("### Brut, temps total : ",temps)

lcb = tmp[:]
lcb.sort(key = lambda x : x[1], reverse=False)
temps = simulePassage(lcb,L,C)
print("### Vitesse, temps total : ",temps)

lcb = tmp[:]
lcb.sort(key = lambda x : x[1], reverse=True)
temps = simulePassage(lcb,L,C)
print("### Vitesse décroissante, temps total : ",temps)

lcb = tmp[:]
lcb.sort(reverse=False)
temps = simulePassage(lcb,L,C)
print("### Poids, temps total : ",temps)

lcb = tmp[:]
lcb.sort(reverse=True)
temps = simulePassage(lcb,L,C)
print("### Poids décroissant, temps total",temps)

def genPermut(n,prof) :
    if prof == 1 :
        res = []
        for i in range(0,n) :
            res.append([i])
    else :
        tmp = genPermut(n,prof-1)
        res = []
        for i in range(0,n) :
            for permut in tmp :
                if not (i in permut) :
                    res.append([i]+permut)
    return res

N=len(lcb)
if N <= 10 :
    st = time.time()
    durationMin=temps
    lcb3 = []
    num=0
    arrangements = genPermut(N,N)

    for arrangement in arrangements :
        lcb=[]
        for i in range(0,N) :
            lcb.append(tmp[arrangement[i]])
        lcb2 = lcb[:]
        duration = simulePassage(lcb2,L,C)
        if duration <= durationMin :
            durationMin = duration