# PCB-LAYOUT-2: wariant A do oceny

PROTOTYPE / PROVISIONAL — NOT FOR MANUFACTURING. Nie ma ścieżek, przelotek routingu ani pól miedzi.

## Układ funkcjonalny

- MAIN pionowo po lewej, obrót180°, oba USB-C ku górnej krawędzi, antena w dół. Referencyjny PCB28×57 i konserwatywna dodatkowa rezerwa anteny6,4mm; pełny zarezerwowany obrys XY(64,53)…(92,116.4). Moduł i jego obudowy USB mieszczą się referencyjnie w laminacie; nie wykorzystano niezatwierdzonego wystawania modułu.
- DAC u góry po prawej, obrót180° całego footprintu. Rzeczywisty rysunek jacka w źródłowym footprintcie wskazywał dół przy0°, mimo wartości symbolu JACK RIGHT. Po obrocie jack jest ku górnej krawędzi. Padów, symbolu ani wartości nie zmieniono. Nie przywrócono błędnego STEP. FB301/C301/C302/C303 są z prawej przy zasilaniu A6; AUDIO L/GND/R nad środkową strefą.
- BT po prawej, płasko, antena w górę, USB w dół. Wspólny punkt obu footprintów(126,124.05), oba0°; nigdy nie obracano rzędów niezależnie. Odstęp wewnętrznych listew22,86mm. J402.8=5V_SYS bez zmian. Obrys płytki(110.76,105)…(141.24,141.83); źródłowa rezerwa USB sięga148,18mm, wewnątrz PCB150mm.
- RTC w górnej części strefy środkowej: pin1(103.5,77.6), referencyjny obrys(96.8,75.98)…(110.2,89.38). Przesunięcie względem geometrycznego środka było potrzebne dla15mm odstępu od anteny BT. Pionowy goldpin męski1×5, pin4NC i bateria bez zmian.
- I2C/SPI/INPUT/AMP w jednym szeregu przy dolnej krawędzi; pin1 rozpoznawalny po kwadratowym padzie i nadruku1. ARK przy lewej, zabezpieczenia F101/Q101/D101 ułożone przy nim; AMS1117/C105 i AUX w dolnej lewej strefie. C101 przeniesiony do zasilania MAIN. Pozostałe części grupowane jako POWER, MAIN, AUDIO, BT, DISPLAY, INPUT/RTC. Przestrzeń wokół anten pozostaje pusta; nie wypełniano jej drobnicą dla samej estetyki.

Wszystkie77 części elektrycznych oraz4 otwory są na TOP;11 dawnych BOTTOM przeniesione. Nie ma żadnej drobnicy pod pełnymi obrysami MAIN/BT/DAC/RTC. Nie polegano na niepotwierdzonym8,5mm prześwicie, żeby coś schować. Gniazda modułów pozostają własnymi częściami montażu i są jedynymi elementami znajdującymi się pod odpowiadającymi im płytkami.

## Nadruk i zworki

Logo tekstowe VoxOne, VoxOne_M1, sekcje, +5V/GND, pin1, wybór3V3/5V i I2C PU ON/OFF. Wszystkie referencje zachowane; moduły/złącza mają pełne widoczne podpisy, natywne pola montażowe nadal na F.Fab. Ukryte przez płytki modułów opisy GPIO przeniesiono tylko graficznie na F.Fab, bez zmiany bibliotek/padów. Końcowy DRC nadruku0 ostrzeżeń.

JP501/JP502: 1–2=3V3, 2–3=5V. JP601: 1–2 S1,3–4 S2,5–6 KEY. JP602: 1–2 SDA,3–4 SCL; założona zworkaON, zdjętaOFF na M1. W aktualnym obrocie90° JP602 obie pary zakłada się pionowo w widoku2D. Nie zwierać rzędów1–3 ani2–4; mogłoby to połączyć SDA/SCL. Dokładne linie par są na F.Fab; SDA/SCL i ON/OFF na nadruku. Podciągania zewnętrznych modułów mogą pozostać aktywne po zdjęciu zworek; wszystkie do3,3V. I2C bez translatorów.

Nagłówki użytkowe: J5011=VCC,2=GND,3=SDA,4=SCL; J5021=VCC,2=GND,3=SCK,4=MOSI,5=CS,6=DC,7=RST,8=BL; J6011=S1,2=S2,3=KEY,4=GND; J6031=EN_OC,2=MUTE_OC,3=GND; J3011=L,2=GND,3=R. Pełne etykiety pinów są w schemacie i tym raporcie; nie wciskano długich nazw między padami.

## Pozycje wszystkich77 elementów

Współrzędne KiCad w mm, obrys(50,50)…(150,150); obrót wg native API.

| Ref | Wartość zachowana | X | Y | Obrót° | Strona |
|---|---|---|---|---|---|
| C101 | 470u 16V radial | 100.0 | 64.0 | 0.0 | TOP |
| C102 | 100n X7R 25V | 96.0 | 57.0 | 0.0 | TOP |
| C103 | 10u 16V radial | 95.0 | 137.0 | 0.0 | TOP |
| C104 | 100n X7R 25V | 66.099999 | 143.0 | 0.0 | TOP |
| C105 | 22u 16V solid tantalum | 86.0 | 134.0 | 0.0 | TOP |
| C106 | 100n X7R 25V | 79.5 | 134.0 | 90.0 | TOP |
| C201 | 100n X7R 25V | 61.0 | 56.0 | 90.0 | TOP |
| C202 | 10n X7R 25V | 96.0 | 53.0 | 0.0 | TOP |
| C203 | 100u 16V radial | 103.0 | 72.8 | 0.0 | TOP |
| C301 | 100n X7R 25V | 145.5 | 59.8 | 0.0 | TOP |
| C302 | 10n X7R 25V | 146.0 | 70.0 | 0.0 | TOP |
| C303 | 10u 16V radial THT | 146.0 | 65.0 | 0.0 | TOP |
| C401 | 100n X7R 25V | 145.8 | 136.0 | 0.0 | TOP |
| C402 | 10n X7R 25V | 146.5 | 139.0 | 0.0 | TOP |
| C403 | 100u 16V radial | 146.0 | 130.0 | 0.0 | TOP |
| C501 | 100n X7R 25V | 111.5 | 76.0 | 90.0 | TOP |
| C502 | 10n X7R 25V | 111.5 | 81.5 | 90.0 | TOP |
| C503 | 10u 16V radial THT | 63.0 | 137.0 | 0.0 | TOP |
| C504 | 100n X7R 25V | 95.0 | 78.0 | 90.0 | TOP |
| C505 | 10n X7R 25V | 95.0 | 83.5 | 90.0 | TOP |
| C506 | 10u 16V radial THT | 86.0 | 141.0 | 0.0 | TOP |
| C507 | 1u X7R 25V | 124.0 | 74.0 | 0.0 | TOP |
| C508 | 100n X7R 25V | 95.0 | 89.0 | 90.0 | TOP |
| C601 | 100n X7R 25V | 113.5 | 86.0 | 0.0 | TOP |
| C602 | 10n X7R 25V | 119.0 | 86.0 | 0.0 | TOP |
| C603 | 10u 16V radial | 116.0 | 80.0 | 0.0 | TOP |
| D101 | SMBJ5.0A TVS unidir. | 53.5 | 98.5 | 90.0 | TOP |
| D501 | 1N4148W | 94.0 | 132.0 | 0.0 | TOP |
| F101 | T3.15A / >=16V | 54.5 | 77.5 | 0.0 | TOP |
| FB301 | 600R@100MHz / >=0.5A | 146.0 | 74.0 | 0.0 | TOP |
| J101 | ARK 5V / GND | 57.0 | 90.7 | 90.0 | TOP |
| J301 | AUDIO OUT: 1=L 2=GND 3=R | 100.5 | 55.5 | 90.0 | TOP |
| J401 | BT LEFT INNER / USB DOWN | 126.0 | 124.05 | 0.0 | TOP |
| J402 | BT RIGHT INNER / USB DOWN | 126.0 | 124.05 | 0.0 | TOP |
| J501 | I2C: VCC GND SDA SCL | 61.0 | 147.8 | 90.0 | TOP |
| J502 | SPI: VCC GND SCK MOSI CS DC RST BL | 74.0 | 147.8 | 90.0 | TOP |
| J601 | INPUT: S1 S2 KEY GND | 98.0 | 147.8 | 90.0 | TOP |
| J603 | AMP: EN_OC MUTE_OC GND | 112.0 | 147.8 | 90.0 | TOP |
| JP501 | I2C VCC SELECT | 92.5 | 142.5 | 90.0 | TOP |
| JP502 | SPI VCC SELECT | 100.0 | 128.5 | 90.0 | TOP |
| JP601 | PULL-UP ENABLE 2x3 | 124.0 | 88.0 | 90.0 | TOP |
| JP602 | I2C PULL-UP / 2x2 / 2.54mm | 101.0 | 138.0 | 90.0 | TOP |
| Q101 | FDD6685 DPAK | 54.5 | 69.0 | 0.0 | TOP |
| Q401 | MMBT3904 / reset OC | 147.0 | 88.5 | 0.0 | TOP |
| Q503 | MMBT3904 BL drive | 102.0 | 142.5 | 90.0 | TOP |
| Q504 | AO3401A BL high-side | 94.5 | 94.0 | 90.0 | TOP |
| Q601 | MMBT3904 EN OC | 106.5 | 142.5 | 0.0 | TOP |
| Q602 | MMBT3904 MUTE OC | 81.5 | 140.0 | 0.0 | TOP |
| R101 | 300R 1% / 0.125W | 64.5 | 132.5 | 0.0 | TOP |
| R201 | 33R | 95.0 | 66.0 | 90.0 | TOP |
| R202 | 33R | 94.0 | 71.0 | 90.0 | TOP |
| R203 | 33R | 98.0 | 73.5 | 0.0 | TOP |
| R204 | 100R 1% | 95.0 | 61.0 | 90.0 | TOP |
| R205 | 10k | 62.15 | 66.0 | 90.0 | TOP |
| R301 | 10k | 125.0 | 77.0 | 0.0 | TOP |
| R401 | 6k8 1% | 140.0 | 87.5 | 90.0 | TOP |
| R402 | 100k | 143.0 | 87.5 | 90.0 | TOP |
| R503 | 100k | 129.5 | 80.5 | 90.0 | TOP |
| R504 | 100R | 123.0 | 81.5 | 0.0 | TOP |
| R505 | 10k | 119.0 | 75.5 | 0.0 | TOP |
| R506 | 10k 1% | 133.0 | 82.0 | 90.0 | TOP |
| R507 | 10k | 133.0 | 87.5 | 90.0 | TOP |
| R508 | 100k | 136.0 | 87.5 | 90.0 | TOP |
| R601 | 10k | 105.0 | 132.0 | 0.0 | TOP |
| R602 | 10k | 99.5 | 132.0 | 0.0 | TOP |
| R603 | 10k | 107.0 | 137.5 | 90.0 | TOP |
| R604 | 4k7 | 111.5 | 143.5 | 0.0 | TOP |
| R605 | 4k7 | 54.5 | 126.5 | 0.0 | TOP |
| R606 | 6k8 1% | 76.5 | 142.5 | 0.0 | TOP |
| R607 | 100k | 52.5 | 109.5 | 90.0 | TOP |
| R608 | 6k8 1% | 71.0 | 142.5 | 0.0 | TOP |
| R609 | 100k | 52.5 | 115.0 | 90.0 | TOP |
| U101 | AMS1117-3.3 (UMW) | 73.0 | 136.0 | 0.0 | TOP |
| U201 | ESP32-S3 DevKitC-1 N16R8 (*) | 92.0 | 110.0 | 180.0 | TOP |
| U301 | PCM5102A MODULE / JACK RIGHT | 124.5 | 64.0 | 180.0 | TOP |
| U501 | SN74LVC1G17DBV | 99.0 | 91.5 | 0.0 | TOP |
| U601 | DS3231 for Pi / 5 POS | 103.5 | 77.6 | 0.0 | TOP |

H901=(55,55), H902=(145,55), H903=(55,145), H904=(145,145); otworyNPTH Ø3,2. Dla łba/podkładki przyjęto rezerwęØ7mm. Nie utworzono wariantuB: wariantA spełnił twarde ograniczenia dla geometrii referencyjnej.
