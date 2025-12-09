# 🏚️ MANIAC MANSION - KALANDOZÁS 🏚️

![Game Status](https://img.shields.io/badge/status-playable-green)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

## 📖 TÖRTÉNET

Egy sötét, viharos éjszakán Johnny felfedez egy titokzatos házat. A bejáratnál egy figyelmeztető tábla áll: **"MAGÁN TERÜLET! A belépő vállalja, hogy kísérletezzenek rajta..."**

A házban különös lények laknak - színes csápok, akik speciális tárgyakat kérnek cserébe az életedért. Egy ingerült házinéni is ott van, aki a levelét keresi. Vajon sikerül túlélned ezt a veszélyes kalandot? 🎭

## 🎮 JÁTÉKSZABÁLYOK

### 🎯 CÉL
- Felfedezni a titokzatos házat
- Túlélni a veszélyeket
- Kikerülni a börtönt
- Megoldani a rejtvényeket

### 🚶 MOZGÁS
- **Bejárat**: Itt kezded a játékot. Kulcs nélkül csak a postaládához mehetsz.
- **Postaláda**: Itt található a fontos levél a házinéninek.
- **Konyha**: A házinéni itt várja a levelét. **VIGYÁZAT!** Levél nélkül börtönbe kerülsz!
- **Lépcső**: Olvasható falfirka található itt (tipp a csápokhoz).
- **Dolgozószoba**: Itt találod a zseblámpát.
- **Nappali**: A csillogó gipszgyümölcs itt van.
- **Erkély**: Kötél található itt.
- **Labor**: **VESZÉLY!** Csápok laknak itt.
- **Folyosó**: Zseblampa nélkül gödörbe esel és börtönbe kerülsz!

### 🏠 TÁRGYAK ÉS HELYEIK

| 🏠 Helyiség | 📦 Tárgy | 🔧 Típus | ⚠️ Megjegyzés |
|-------------|----------|----------|---------------|
| Bejárat | 🔑 Kulcs | Kulcs | A házba való belépéshez szükséges |
| Postaláda | 💌 Levél | Olvasható | A házinéninek kell adni |
| Konyha | 🥩 Sült hús | Adható | A piros csápnak kell |
| Lépcső | 🖼️ Falfirka | Olvasható | Tipp a csápokhoz |
| Dolgozószoba | 🔦 Zseblampa | Használható | A folyosóhoz szükséges |
| Nappali | ✨ Csillamgyumi | Adható | A zöld csápnak kell |
| Erkély | 🪢 Kötél | Használható | Hasznos eszköz |
| Labor | 📜 Info | Olvasható | Fontos információ |

### 🐙 CSÁPOK A LABORBAN

#### 💚 ZÖLD CSÁP
- **Mit akar**: Csillogó dolgokat (csillamgyumi)
- **Hol szerezd be**: Nappali
- **Mit történik ha nincs nálad**: Börtönbe kerülsz!

#### ❤️ PIROS CSÁP
- **Mit akar**: Nyers dolgokat (sült hús)
- **Hol szerezd be**: Konyha
- **Mit történik ha nincs nálad**: Börtönbe kerülsz!

### ⚠️ VESZÉLYEK

1. **👵 Házinéni (Konyha)**
   - Ha nincs nálad a levél → Börtön
   - Ha odaadod a levelet → Szabad vagy

2. **🐙 Csápok (Labor)**
   - Véletlenszerűen zöld vagy piros csáp jelenik meg
   - Megfelelő tárgy nélkül → Börtön

3. **🕳️ Gödör (Folyosó)**
   - Zseblampa nélkül → Gödörbe esel → Börtön

4. **🔐 Zárva (Ház)**
   - Kulcs nélkül nem mehetsz be a házba

## 🎮 PARANCSOK

| Parancs | Leírás | Példa |
|---------|--------|-------|
| `megy` | Helyiségek között mozgás | `konyha`, `labor` |
| `felvesz` | Tárgy felvétele az adott helyiségben | - |
| `olvas` | Olvasható tárgyak megtekintése | `level`, `falfirka` |
| `ad` | Tárgy odaadása valakinek | `hazineni` a konyhában |
| `használ` | Tárgy használata | `zseblampa`, `kotel` |
| `váltás` | Karakterváltás (többjátékos módban) | - |
| `vege` | Kilépés a játékból | - |

## 🚀 FUTTATÁS

### Követelmények
- Python 3.x
- Minden fájl ugyanabban a mappában

### Indítás
```bash
python jatek.py
```

## 📁 FÁJLSTRUKTÚRA

```
Maniac-Mansion/
├── jatek.py          # Fő játékfájl
├── belepes.py        # Kezdőképernyő
├── terkep.py         # Térkép és helyiségek
├── Karakter.py       # Karakter osztály
├── karakterek.py     # Johnny karakter
├── Targy.py          # Tárgy osztály
├── targyak.py        # Összes tárgy
└── README.md         # Ez a fájl
```

## 🏆 JÁTÉK STRATÉGIA

### 🔥 RECOMMENDED WALKTHROUGH

1. **🏠 Bejárat**: Vedd fel a kulcsot
2. **📫 Postaláda**: Vedd fel a levelet
3. **🍳 Konyha**: Add oda a levelet a házinéninek, vedd fel a sült húst
4. **🪜 Lépcső**: Olvasd el a falfirkát (fontos tipp!)
5. **💼 Dolgozószoba**: Vedd fel a zseblámpát
6. **🛋️ Nappali**: Vedd fel a csillamgyumit
7. **🌅 Erkély**: Vedd fel a kötelet
8. **🔬 Labor**: Szembesülj a csápokkal (legyen nálad mindkét tárgy!)
9. **🌙 Folyosó**: Most már biztonságosan átmehetsz

### 💡 TIPPEK

- 📝 Mindig olvasd el a falfirkát a lépcsőn!
- 🎒 Győződj meg róla, hogy mindkét tárgy (sült hús ÉS csillamgyumi) nálad van a labor előtt
- 🔦 Soha ne menj a folyosóra zseblampa nélkül
- 💌 Első dolgod legyen a levél megszerzése és odaadása

## ⚠️ GAME OVER FELTÉTELEK

- 👵 Belépés a konyhába levél nélkül
- 🐙 Csápokkal való találkozás megfelelő tárgy nélkül  
- 🕳️ Folyosóra lépés zseblampa nélkül
- ⛓️ Ha minden játékos börtönbe kerül

## 🎭 EASTER EGGS

- 📜 A laborban található "info" tárgy különleges üzenetet tartalmaz
- 🎲 A csápok véletlenszerűen jelennek meg - minden egyes labor látogatás új kihívás!

## 👥 FEJLESZTŐK

Készítette: **Python Kaland Csapat** 🐍

---

### 🌟 Jó szórakozást a Maniac Mansion kalandhoz! 🌟

*"Emlékezz: A kulcs a túléléshez a felkészülés és a bátor szív!"* 💪