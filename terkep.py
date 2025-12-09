from Targy import Targy
from Karakter import Karakter

def osszes_hely(szoba_lista,targy_lista):
    i=0
    while i<len(szoba_lista):
        print(f"{szoba_lista[i]}",end=" ")
        print(f"{targy_lista[i]}\n")
        i+=1