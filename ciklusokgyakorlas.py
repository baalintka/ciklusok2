import math
def feladat1():
    i:int=1
    a:int=int(input("adjon meg egy pozitív számot: "))
    while i<a:
        print(i,end=",")
        i+=1
    print(i)
def feladat2():
    osszeg:int =0
    i: int = 1
    a: int = int(input("adjon meg egy pozitív számot: "))
    osszeg+=a
    while i<a:
        if a % i==0:
            print(i,end=",")
            osszeg+=i
        i+=1
    print(i)
    print(f"Összeg:{osszeg}")

def feladat3():

    a: int = int(input("adjon meg egy pozitív számot: "))
    b: int = int(input("adjon meg egy masik pozitív számot: "))

    while a < b:
        if a % 2 == 0:
            print(a, end=",")

        a += 1
    print(a)
def feladat4():
    i:int=0
    a: int = 1
    b: int = 20
    while i<b:
        print(round(math.pow(a ,2)))
        a+=1
        i+=1
    print(round(math.pow(20 ,2)))

def feladat5():
    szoveg:str=input("irj be valami szöveget: ")
    i:int=0

    while i<len(szoveg):
        print(szoveg[i])
        i+=1
#6.	Írj programot, amely bekér egy szöveget és kiírja visszafelé (Indul a kutya és a tyúk aludni)!
def feladat6():

    szoveg: str = input("irj be valami szöveget: ")
    i: int = len(szoveg)-1
    while not i< 1:
        print(szoveg[i],end="")
        i-=1
    print(szoveg[i], end="")
def feladat7():
    M: int = int(input("adjon meg egy pozitív számot: "))
    N: int = int(input("adjon meg egy pozitív számot: "))