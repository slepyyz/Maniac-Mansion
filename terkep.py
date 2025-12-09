from Targy import Targy
from Karakter import Karakter
import karakterek

tartozkodasi_hely="Bejárat"

def osszes_hely(szoba_lista,targy_lista):
    print(f"Most itt vagy: {tartozkodasi_hely}")
    i=0
    while i<len(szoba_lista):
        print(f"{szoba_lista[i]}",end=" ")
        print(f"{targy_lista[i]}\n")
        i+=1