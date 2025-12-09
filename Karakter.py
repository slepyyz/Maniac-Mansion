from Targy import Targy
import jatek

class Karakter:

    def __init__ (self, nev, eletero, inventory, bortonbe):
        self.nev= str(nev)
        self.eletero= int(eletero)
        self.inventory= Targy
        self.bortonbe= bool(bortonbe)

    def megy():
        input("Hova szeretnél menni?: ")
        #lépés kód

    def felvesz():
        Targy.felvesz

    def hasznal(inventory):
        targy=input("Mit akarsz használni?: ")
        hasznalt=inventory.index(targy)
        inventory[hasznalt].hasznal

    def olvas(inventory):
        targy=input("Mit akarsz olvasni?: ")
        olvasott=inventory.index(targy)
        if inventory[olvasott].tipus== "olvashato":
            inventory[olvasott].felolvas

    def ad(inventory):
        targy=input("Mit akarsz odaadni?: ")
        if jatek.karakterek_szama >1:
            kinek=input("Kinek akarod adni?: ")

    def valtas():
        if jatek.karakterek_szama >1:
            if jatek.iranyitott_karakter==1:
                jatek.iranyitott_karakter=2
            else:
                jatek.iranyitott_karakter=1