class Karakter:

    def __init__ (self, nev, eletero, inventory, bortonbe):
        self.nev= str(nev)
        self.eletero= int(eletero)
        self.inventory= inventory #targy osztály lista
        self.bortonbe= bool(bortonbe)