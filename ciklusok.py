import math
def szamok(a:int,b:int):
    if a==b:
        print("A KÉT SZÁM EGYENLŐ")
        return
    if b>a:
        csere:float=a
        a=b
        b=csere
        i:int=math.ceil(a)
        while i<b:
            if(i==b-1):
                print(i)
            else:
                print(i,end=",")
            i+=1

