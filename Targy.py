class Targy:

    def __init__ (self, nev, hol_hasznalhato, tipus, tartalom):
        self.nev= nev
        self.hasznalhato= str(hol_hasznalhato)
        self.tipus= tipus
        self.tartalom= str(tartalom)

    def felvesz(self):
        #felvesz kód
        print(f"Felvetted: {self.nev}")

    def hasznal(self):
        print(f"⚡ Használtad: {self.nev.upper()}")

    def felolvas(self):
        print(f"📖 {self.tartalom}")