from random import randint
print("Molimo Vas unesite sedam  brojeva od 1 do 39, jedan po jedan.")
def f1():
    global LotoBrojevi
    Loto1= randint(1,39)
    LotoBrojevi = [Loto1]
    Loto2= randint(1,39)
    if Loto2 in LotoBrojevi:
        while Loto2 in LotoBrojevi:
            Loto2 = randint(1,39)
    LotoBrojevi.append(Loto2)
    Loto3= randint(1,39)
    if Loto3 in LotoBrojevi:
        while Loto3 in LotoBrojevi:
            Loto3 = randint(1,39)
    LotoBrojevi.append(Loto3)
    Loto4= randint(1,39)
    if Loto4 in LotoBrojevi:
        while Loto4 in LotoBrojevi:
            Loto4 = randint(1,39)
    LotoBrojevi.append(Loto4)
    Loto5= randint(1,39)
    if Loto5 in LotoBrojevi:
        while Loto5 in LotoBrojevi:
            Loto5 = randint(1,39)
    LotoBrojevi.append(Loto5)
    Loto6= randint(1,39)
    if Loto6 in LotoBrojevi:
        while Loto6 in LotoBrojevi:
            Loto6 = randint(1,39)
    LotoBrojevi.append(Loto6)
    Loto7= randint(1,39)
    if Loto7 in LotoBrojevi:
        while Loto7 in LotoBrojevi:
            Loto7 = randint(1,39)
    LotoBrojevi.append(Loto7)
MojiBrojevi=[]
y = 7
while y != 0:
    MojiBrojevi.append(int(input()))
    y -= 1
print("Vasi brojevi su : ",MojiBrojevi)
print("Molimo Vas sacekajte.")
print( )
def f2():
    global BrojSedmica
    BrojSedmica=0
    global BrojSestica
    BrojSestica = 0
    global BrojPetica
    BrojPetica = 0
    global BrojCetvorki
    BrojCetvorki = 0
    global BrojTrojki
    BrojTrojki = 0
    global BrojDvojki
    BrojDvojki = 0
    global BrojJedinica
    BrojJedinica = 0
    x=1000000
    while x!=0:
        m=0
        f1()
        if MojiBrojevi[0] in LotoBrojevi:
            m+=1
        if MojiBrojevi[1] in LotoBrojevi:
            m+=1
        if MojiBrojevi[2] in LotoBrojevi:
            m+=1
        if MojiBrojevi[3] in LotoBrojevi:
            m+=1
        if MojiBrojevi[4] in LotoBrojevi:
            m+=1
        if MojiBrojevi[5] in LotoBrojevi:
            m+=1
        if MojiBrojevi[6] in LotoBrojevi:
            m+=1
        if m==1:
            BrojJedinica+=1
        if m==2:
            BrojDvojki+=1
        if m==3:
            BrojTrojki+=1
        if m==4:
            BrojCetvorki+=1
        if m==5:
            BrojPetica+=1
        if m==6:
            BrojSestica+=1
        if m==7:
            print( )
            print("Cestitamo, osvojili ste sedmicu nakon pokusaja broj ", 1000000 - x)
            print( )
            BrojSedmica += 1
        x-=1
f2()
print("Broj sedmica koje ste osvojili u milion pokusaja je  ", BrojSedmica)
print("Broj sestica koje ste osvojili u milion pokusaja je ",BrojSestica)
print("Broj petica koje ste osvojili u milion pokusaja je",BrojPetica)
print("Broj cetvorki koje ste osvojili u milion pokusaja je",BrojCetvorki)
print("Broj trojki koje ste osvojili u milion pokusaja je",BrojTrojki)
print("Broj dvojki koje ste osvojili u milion pokusaja je",BrojDvojki)
print("Broj jedinica koje ste osvojili u milion pokusaja je",BrojJedinica)
print( )
print("Sansa da osvojite sedmicu je ", BrojSedmica/10000, "%")
print("Sansa da osvojite sesticu je ", BrojSestica/10000, "%")
print("Sansa da osvojite peticu je ", BrojPetica/10000, "%")
print("Sansa da osvojite cetvorku je ", BrojCetvorki/10000, "%")
print("Sansa da osvojite trojku je ", BrojTrojki/10000, "%")
print("Sansa da osvojite dvojku je ", BrojDvojki/10000, "%")
print("Sansa da osvojite jedinicu je ", BrojJedinica/10000, "%")


