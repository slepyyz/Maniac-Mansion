from Karakter import Karakter
from Targy import Targy
import belepes
import karakterek
import terkep


karakterek_szama=1
iranyitott_karakter=1

szoba_lista=["bejarat","postalada","konyha","lepcso","dolgozo","nappali","labor","erkely","folyoso"]
targy_lista=["kulcs","level","sulthus","falfirka","zseblampa","csillamgyumi","info","kotel","nincsitem"]

belepes.invitacio()
terkep.osszes_hely(szoba_lista,targy_lista)

jatek=True

while jatek:
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