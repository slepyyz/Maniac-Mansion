from Targy import Targy
import jatek

class Karakter:

    def __init__ (self, nev, eletero, inventory, bortonbe):
        self.nev= str(nev)
        self.eletero= int(eletero)
        self.inventory= inventory
        self.bortonbe= bool(bortonbe)

    def megy():
        input("Hova szeretnél menni?: ")
        #lépés kód

    def felvesz(self):
        Targy.felvesz()

    def hasznal(self):
        targy=input("Mit akarsz használni?: ")
        hasznalt=self.inventory.index(targy)
        self.inventory[hasznalt].hasznal()

    def olvas(self):
        targy=input("Mit akarsz olvasni?: ")
        olvasott=self.inventory.index(targy)
        if self.inventory[olvasott].tipus== "olvashato":
            self.inventory[olvasott].felolvas()

    def ad(self):
        targy=input("Mit akarsz odaadni?: ")
        if jatek.karakterek_szama >1:
            kinek=input("Kinek akarod adni?: ")

    def valtas():
        if jatek.karakterek_szama >1:
            if jatek.iranyitott_karakter==1:
                jatek.iranyitott_karakter=2
            else:
                jatek.iranyitott_karakter=1