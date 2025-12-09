from Targy import Targy
from Karakter import Karakter
import karakterek

tartozkodasi_hely="bejarat"

def osszes_hely(szoba_lista,targy_lista):
    print("\n" + "─"*50)
    print(f"📍 HELYZETED: {tartozkodasi_hely.upper()}")
    print("─"*50)
    print("🗺️  ELÉRHETŐ HELYEK ÉS TÁRGYAK:")
    print("─"*50)
    i=0
    while i<len(szoba_lista):
        if targy_lista[i] == "nincsitem":
            targy_ikon = "❌"
            targy_nev = "nincs tárgy"
        else:
            targy_ikon = "📦"
            targy_nev = targy_lista[i]
        print(f"🏠 {szoba_lista[i].ljust(12)} {targy_ikon} {targy_nev}")
        i+=1
    print("─"*50)
    print()