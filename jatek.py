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
    if karakterek.johnny.bortonbe:
        print("\n" + "🚨"*20)
        print("⛓️  JOHNNY BÖRTÖNBEN VAN! ⛓️")
        print("🚨"*20)
        if karakterek_szama == 1:
            print("💀 VÉGE A JÁTÉKNAK! 💀")
            print("Próbáld újra!")
            jatek = False
            continue
        else:
            print("🔄 Váltás a másik karakterre...")
    
    if terkep.tartozkodasi_hely == "konyha" and not level_odaadva:
        level_megvan = False
        for item in karakterek.johnny.inventory:
            if item.nev == "level":
                level_megvan = True
        if not level_megvan:
            print("\n" + "👵"*15)
            print("👵 A konyhába lépve a házinéni rád kiált!")
            print("👵 'HOL A LEVELEM?!' - Börtönbe kerültél!")
            print("👵"*15)
            karakterek.johnny.bortonbe = True
            continue
    
    terkep.osszes_hely(szoba_lista,targy_lista)
    print("🎮 MIT TESZEL?")
    print("⭐ Parancsok: megy, felvesz, használ, olvas, ad, váltás, vege")
    lepes=input("🎯 Választásod: ")
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
        print("\n" + "🌟"*20)
        print("🎮 KÖSZÖNJÜK A JÁTÉKOT! 🎮")
        print("   Maniac Mansion kaland vége!")
        print("🌟"*20)
        jatek = False