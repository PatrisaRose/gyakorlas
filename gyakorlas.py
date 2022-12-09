import random

sorozat = [-3, 5, 11, -2, 4]

def separator(sep=" "):
    i = 0
    s = ""
    while i < len(sorozat):
        if i == (len(sorozat)-1):
            s += str(sorozat[i])
        elif i < (len(sorozat)):
            s += str(sorozat[i]) + f"{sep} "

        i += 1
    print(s)

def randomSzam():
    rand = int(random.random()*8)+5
    sorozat[0] += rand
    print(sorozat)

def szamBekeres():
    szam = int(input("Kérlek adj meg egy páratlan, hárommal osztható kétjegyű számot: "))
    while 10 > szam or szam >= 100 and szam % 3 != 0 :
        szam = int(input("Kérlek adj meg másik számot: "))

    sorozat[-1] = szam
    print(sorozat)

def elsoKetjegyu():
    i = 0
    while sorozat[i] < 10 or sorozat[i] > 100:
        i += 1

    print(f"A szám értéje: {sorozat[i]} és a szám pozíciója {i}")

def prim():
    i = 0

    primek = []
    while i < len(sorozat):
        if sorozat[i] < 0:

            i += 1
        else:
            prim = True
            c = 2
            while c < sorozat[i]:
                if sorozat[i] % c == 0:
                    prim = False
                c += 1
            if prim:
                primek.append(sorozat[i])
            i += 1

    print(primek)
