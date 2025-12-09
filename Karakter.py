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
        
        # Ellenőrizzük, hogy létezik-e a helyiség
        if hova not in jatek.szoba_lista:
            print("Nincs ilyen helyiség")
            return
        
        # Bejárat ellenőrzés - csak kulccsal lehet bemenni (kivéve postaláda)
        if terkep.tartozkodasi_hely == "bejarat" and hova != "bejarat" and hova != "postalada":
            kulcs_megvan = False
            for item in self.inventory:
                if item.nev == "kulcs":
                    kulcs_megvan = True
            if not kulcs_megvan:
                print("A bejáratból csak a postaládához mehetsz kulcs nélkül!")
                return
        
        # Folyosó ellenőrzés - csak zseblámpával lehet bemenni
        if hova == "folyoso":
            zseblampa_megvan = False
            for item in self.inventory:
                if item.nev == "zseblampa":
                    zseblampa_megvan = True
            if not zseblampa_megvan:
                print("A folyosóra csak akkor mehetsz ha van zseblámpád!")
                print("Gödörbe estél és börtönbe kerültél!")
                self.bortonbe = True
                return
        
        # Labor ellenőrzés - csápok
        if hova == "labor":
            import random
            csap_tipus = random.choice(["zold", "piros"])
            print(f"Találkoztál a {csap_tipus} csáppal!")
            
            if csap_tipus == "zold":
                # Zöld csáp - csillamgyumi kell
                csillamgyumi_megvan = False
                for item in self.inventory:
                    if item.nev == "csillamgyumi":
                        csillamgyumi_megvan = True
                if not csillamgyumi_megvan:
                    print("A zöld csáp csillogó dolgot akar! Börtönbe kerültél!")
                    self.bortonbe = True
                    return
                else:
                    print("Odaadtad a csillamgyumit a zöld csápnak.")
                    # Eltávolítjuk a csillamgyumit
                    for i, item in enumerate(self.inventory):
                        if item.nev == "csillamgyumi":
                            self.inventory.pop(i)
                            return
            else:
                # Piros csáp - sulthus kell
                sulthus_megvan = False
                for item in self.inventory:
                    if item.nev == "sulthus":
                        sulthus_megvan = True
                if not sulthus_megvan:
                    print("A piros csáp nyers dolgot akar! Börtönbe kerültél!")
                    self.bortonbe = True
                    return
                else:
                    print("Odaadtad a sülthúst a piros csápnak.")
                    # Eltávolítjuk a sülthúst
                    for i, item in enumerate(self.inventory):
                        if item.nev == "sulthus":
                            self.inventory.pop(i)
                            return
        
        # Ha minden rendben, akkor léphetünk
        terkep.tartozkodasi_hely = hova
        print(f"Elmentél ide: {hova}")

    def felvesz(self):
        import jatek
        import terkep
        import targyak
        
        hely_index = jatek.szoba_lista.index(terkep.tartozkodasi_hely)
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
        
        if talalt_targy:
            if talalt_targy.tipus == "olvashato":
                talalt_targy.felolvas()
            else:
                print("Ez a tárgy nem olvasható.")
        else:
            print("Nincs ilyen tárgy az inventory-ban.")

    def ad(self):
        import jatek
        import terkep
        targy=input("Mit akarsz odaadni?: ")
        
        talalt_targy = None
        talalt_index = -1
        for i, item in enumerate(self.inventory):
            if item.nev == targy:
                talalt_targy = item
                talalt_index = i
        
        if not talalt_targy:
            print("Nincs ilyen tárgy az inventory-ban.")
            return
        
        # Konyha - házinéni logika
        if terkep.tartozkodasi_hely == "konyha":
            kinek=input("Kinek akarod adni?: ")
            if kinek == "hazineni":
                if targy == "level":
                    print("Odaadtad a levelet a házinéninek.")
                    self.inventory.pop(talalt_index)
                    # Beállítjuk, hogy odaadtuk a levelet
                    import jatek
                    jatek.level_odaadva = True
                    return
                else:
                    print("A házinéni csak a levelet fogadja el!")
                    return
            else:
                print("Itt csak a házinéni van.")
                return
        
        # Több karakteres játék esetén
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