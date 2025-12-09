from Targy import Targy

class Karakter:

    def __init__ (self, nev, inventory, bortonbe):
        self.nev= str(nev)
        self.inventory= inventory
        self.bortonbe= bool(bortonbe)

    def megy(self):
        import terkep
        import jatek
        hova=input("Hova szeretnél menni?: ")
        if hova in jatek.szoba_lista:
            terkep.tartozkodasi_hely=hova
            if hova == "folyoso" and ("zseblampa" not in self.inventory):
                print("A folyosóra csak akkor mehetsz ha van zseblámpád!")
        else:
            print("Nincs ilyen helyiség")

    def felvesz(self):
        import jatek
        import terkep
        import targyak
        
        hely_index = jatek.szoba_lista.index(terkep.tartozkodasi_hely.lower())
        targy_neve = jatek.targy_lista[hely_index]
        
        if targy_neve == "nincsitem":
            print("Nincs itt semmi felvehető.")
            return

        if targy_neve == "kulcs":
            targy_obj = targyak.kulcs
        elif targy_neve == "level":
            targy_obj = targyak.level
        elif targy_neve == "sulthus":
            targy_obj = targyak.sulthus
        elif targy_neve == "falfirka":
            targy_obj = targyak.falfirka
        elif targy_neve == "zseblampa":
            targy_obj = targyak.zseblampa
        elif targy_neve == "csillamgyumi":
            targy_obj = targyak.csillamgyumi
        elif targy_neve == "info":
            targy_obj = targyak.info
        elif targy_neve == "kotel":
            targy_obj = targyak.kotel
        else:
            print("Hiba: A tárgy nem található.")
            return

        self.inventory.append(targy_obj)
        print(f"Felvetted: {targy_obj.nev}")
        jatek.targy_lista[hely_index] = "nincsitem"

    def hasznal(self):
        targy=input("Mit akarsz használni?: ")
        
        talalt_targy = None
        for item in self.inventory:
            if item.nev == targy:
                talalt_targy = item
                break
        
        if talalt_targy:
            talalt_targy.hasznal()
        else:
            print("Nincs ilyen tárgy az inventory-ban.")

    def olvas(self):
        targy=input("Mit akarsz olvasni?: ")
        
        talalt_targy = None
        for item in self.inventory:
            if item.nev == targy:
                talalt_targy = item
                break
        
        if talalt_targy:
            if talalt_targy.tipus == "olvashato":
                talalt_targy.felolvas()
            else:
                print("Ez a tárgy nem olvasható.")
        else:
            print("Nincs ilyen tárgy az inventory-ban.")

    def ad(self):
        import jatek
        targy=input("Mit akarsz odaadni?: ")
        
        talalt_targy = None
        talalt_index = -1
        for i, item in enumerate(self.inventory):
            if item.nev == targy:
                talalt_targy = item
                talalt_index = i
                break
        
        if not talalt_targy:
            print("Nincs ilyen tárgy az inventory-ban.")
            return
        
        if jatek.karakterek_szama > 1:
            kinek=input("Kinek akarod adni?: ")
            print(f"Odaadtad {targy}-t {kinek}-nek.")
            self.inventory.pop(talalt_index)
        else:
            print("Nincs másik karakter akinek odaadhatnád.")

    def valtas(self):
        import jatek
        if jatek.karakterek_szama > 1:
            if jatek.iranyitott_karakter == 1:
                jatek.iranyitott_karakter = 2
                print("Átváltottál a 2. karakterre.")
            else:
                jatek.iranyitott_karakter = 1
                print("Átváltottál az 1. karakterre.")
        else:
            print("Nincs másik karakter amire válthatnál.")