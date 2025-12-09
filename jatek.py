import belepes
import karakterek
import terkep


karakterek_szama=1
iranyitott_karakter=1
level_odaadva=False

szoba_lista=["bejarat","postalada","konyha","lepcso","dolgozo","nappali","labor","erkely","folyoso"]
targy_lista=["kulcs","level","sulthus","falfirka","zseblampa","csillamgyumi","info","kotel","nincsitem"]

belepes.invitacio()

jatek=True

while jatek:
    # Ellenőrizzük, hogy a játékos börtönben van-e
    if karakterek.johnny.bortonbe:
        print("Johnny börtönben van!")
        if karakterek_szama == 1:
            print("Vége a játéknak!")
            jatek = False
            continue
        else:
            print("Váltás a másik karakterre...")
            # Itt lehetne karakterváltás logika
    
    # Ellenőrizzük a konyha logikát - házinéni (csak ha még nem adtuk oda a levelet)
    if terkep.tartozkodasi_hely == "konyha" and not level_odaadva:
        level_megvan = False
        for item in karakterek.johnny.inventory:
            if item.nev == "level":
                level_megvan = True
        if not level_megvan:
            print("A konyhába lépve a házinéni rád kiált!")
            print("'Hol a levelem?' - Börtönbe kerültél!")
            karakterek.johnny.bortonbe = True
            continue
    
    terkep.osszes_hely(szoba_lista,targy_lista)
    lepes=input("Mit teszel?: ")
    if lepes == "megy":
        karakterek.johnny.megy()
    elif lepes == "felvesz":
        karakterek.johnny.felvesz()
    elif lepes == "használ":
        karakterek.johnny.hasznal()
    elif lepes == "olvas":
        karakterek.johnny.olvas()
    elif lepes == "ad":
        karakterek.johnny.ad()
    elif lepes == "váltás":
        karakterek.johnny.valtas()
    elif lepes == "vege":
        jatek = False