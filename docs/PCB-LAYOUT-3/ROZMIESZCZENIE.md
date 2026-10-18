# Rozmieszczenie PCB-LAYOUT-3

PROTOTYPE / PROVISIONAL — NOT FOR MANUFACTURING. Nowa kompozycja na źródłach layout2; nie tylko kosmetyka. Nominalny obrys(50,50)…(150,150)mm,100×100mm,2Cu.

## Przebieg i iteracje

A: pełna analiza referencji, historii, źródeł i baseline, checkpoint. B: nowe pozycje MAIN/DAC/BT/RTC, RF i osobne korytarze dwóch USB MAIN, USB BT i jacka. C: dolny rząd I2C/SPI/INPUT/AMP, selektory VCC, JP602 i JP601. D: przełożenie wszystkich grup drobnicy; ochrona wejścia wzdłuż lewej krawędzi, AUX poniżej, R201–204 przy lewej listwie MAIN, reset/BL w górnej strefie sterowania, własne grupy DAC/RTC/BT. E: niezależne kontrole pełnych obrysów, usunięcie wykrytych kolizji, eksporty i faktyczny DRC. Pierwsza kontrola wykryła zbyt mały odstęp C301 od krawędzi i C402 od M3; skorygowano pozycje, nie reguły. Przywrócono też pełny oryginalny nadruk złącza J603 i przesunięto całe złącze, aby nie pozostawić niezgodności z biblioteką. Iteracja2 i finalne raporty zachowane osobno.

## Grupy

- MAIN0°: antena w górę przy krawędzi, obaUSB w dół. R201/202/20333Ω są w grupie przy źródłowych GPIO, zamiast daleko po stronie odbiornika. U201 i jego44pady obrócono jako całość; bez lustra.
- POWER: J101 po lewej, F101 powyżej wejścia, Q101 poniżej, D101/C101 obok 5V_SYS, U101 i jego kondensatory niżej. To celowo pionowy, wąski blok, nie rozmieszczenie pod MAIN. ARK pozostaje 2-pin, śruby dostępne z góry, przewód od lewej.
- DAC90°: źródłowe A1–A6 i B1–B9 wraz z rzeczywistą geometrią obrócone razem. Jack w prawo, facex150, AUDIO J301 obok. C301 przy narożu VIN; C302/C303/FB301 po lewej stronie modułu, jawny kompromis długości do oceny przed routingiem.
- BT: oba wewnętrzne gniazda w tym samym punkcie i przy0°, antenaUP, USBDOWN. Kondensatory przy końcu VCC prawego gniazda. ResetBT w osobnej górnej grupie sterującej poza RF.
- RTC: osobny pełny obrys13,4×13,4 i własne C601–603 po prawej, minimum2,095mm do innych części. Bez drobnicy pod modułem.
- DISPLAY: selektory i kondensatory przy dolnych złączach; sprzętowy RESET/BL w oddzielnej górnej grupie sterowania. I2C bez translatorów, zewnętrzny wyświetlacz nie może podciągać do5V.
- INPUT/AMP: JP601/R601–603 w dolnej strefie środkowej; sterowanie AMP w dostępnych pasach serwisowych. Q601 bliżej AMP, Q602 pomiędzy korytarzami USB. JP601 jest około32mm od J601 — opisany kompromis do decyzji, nie twierdzenie o idealnej bliskości.

Wszystkie77 części TOP; cztery otwory również jako footprintyTOP. Brak elementów pod pełnymi obrysami modułów; własne podstawki stanowią część montażu. Nie wykorzystano niepotwierdzonego prześwitu8,5mm, żeby ukryć drobnicę. Nie rozpoczęto routingu.

## Zworki i nadruki

JP501/JP502:1–2=3V3,2–3=5V; środkowyVCC. JP601:1–2S1,3–4S2,5–6KEY. JP602:1–2SDA,3–4SCL, zworki poziomo na aktualnym widokuTOP; nie łączyć1–3/2–4. Prawidłowe pary są narysowane na F.Fab, a SDA/SCL i krótkie wskaźniki odpowiadają wierszom na F.SilkS. ON=shunt,OFF=open; zewnętrzne pull-up mogą nadal działać. Wszystkie podciągania całej magistrali do zgodnych3,3V.

Nadruk ma min0,8mm zgodnie z niezmienioną konfiguracją; finalny DRC0 ostrzeżeń nadruku. Wszystkie wartości i natywne reference fields zachowane. Referencje D101,R101,C105,U101,C401,C402,R602 pozostają na F.Fab z powodu braku czytelnego miejsca na TOP bez nakładania na części. Nie usunięto pól ani nie wyłączono kontroli; ich pozycje/oznaczenia są dostępne w KiCad i tabeli montażowej poniżej. Brak ich napisu naF.SilkS jest ograniczeniem tej propozycji, nie ukrytą zmianą elektryczną.

## Pełna tabela77 elementów

Współrzędne globalneKiCad w mm; kąt wg natywnego API; wartości zachowane.

| Ref | Wartość | X | Y | Kąt° | Strona |
|---|---|---|---|---|---|
| C101 | 470u 16V radial | 53.6 | 120.8 | 0.0 | TOP |
| C102 | 100n X7R 25V | 61.5 | 103.8 | 90.0 | TOP |
| C103 | 10u 16V radial | 61.5 | 139.0 | 0.0 | TOP |
| C104 | 100n X7R 25V | 54.0 | 127.6 | 0.0 | TOP |
| C105 | 22u 16V solid tantalum | 62.1 | 131.0 | 90.0 | TOP |
| C106 | 100n X7R 25V | 61.7 | 144.5 | 0.0 | TOP |
| C201 | 100n X7R 25V | 64.5 | 115.5 | 90.0 | TOP |
| C202 | 10n X7R 25V | 68.7 | 117.3 | 90.0 | TOP |
| C203 | 100u 16V radial | 60.8 | 110.0 | 0.0 | TOP |
| C301 | 100n X7R 25V | 147.4 | 93.2 | 0.0 | TOP |
| C302 | 10n X7R 25V | 128.5 | 82.0 | 0.0 | TOP |
| C303 | 10u 16V radial THT | 126.0 | 87.3 | 0.0 | TOP |
| C401 | 100n X7R 25V | 141.4 | 136.7 | 90.0 | TOP |
| C402 | 10n X7R 25V | 145.5 | 136.7 | 0.0 | TOP |
| C403 | 100u 16V radial | 146.0 | 132.3 | 0.0 | TOP |
| C501 | 100n X7R 25V | 68.7 | 123.5 | 90.0 | TOP |
| C502 | 10n X7R 25V | 69.8 | 138.5 | 0.0 | TOP |
| C503 | 10u 16V radial THT | 68.2 | 142.9 | 0.0 | TOP |
| C504 | 100n X7R 25V | 94.9 | 126.0 | 90.0 | TOP |
| C505 | 10n X7R 25V | 102.0 | 131.0 | 0.0 | TOP |
| C506 | 10u 16V radial THT | 95.6 | 131.9 | 0.0 | TOP |
| C507 | 1u X7R 25V | 111.0 | 56.0 | 90.0 | TOP |
| C508 | 100n X7R 25V | 106.0 | 60.0 | 90.0 | TOP |
| C601 | 100n X7R 25V | 116.0 | 89.5 | 0.0 | TOP |
| C602 | 10n X7R 25V | 122.0 | 92.0 | 0.0 | TOP |
| C603 | 10u 16V radial | 116.0 | 83.3 | 0.0 | TOP |
| D101 | SMBJ5.0A TVS unidir. | 64.9 | 122.0 | 90.0 | TOP |
| D501 | 1N4148W | 100.6 | 74.5 | 0.0 | TOP |
| F101 | T3.15A / >=16V | 52.5 | 83.0 | 0.0 | TOP |
| FB301 | 600R@100MHz / >=0.5A | 124.0 | 79.0 | 0.0 | TOP |
| J101 | ARK 5V / GND | 56.0 | 98.0 | 90.0 | TOP |
| J301 | AUDIO OUT: 1=L 2=GND 3=R | 125.5 | 65.0 | 0.0 | TOP |
| J401 | BT LEFT INNER / USB DOWN | 124.74 | 127.55 | 0.0 | TOP |
| J402 | BT RIGHT INNER / USB DOWN | 124.74 | 127.55 | 0.0 | TOP |
| J501 | I2C: VCC GND SDA SCL | 60.5 | 147.8 | 90.0 | TOP |
| J502 | SPI: VCC GND SCK MOSI CS DC RST BL | 94.0 | 147.8 | 90.0 | TOP |
| J601 | INPUT: S1 S2 KEY GND | 131.4 | 147.0 | 90.0 | TOP |
| J603 | AMP: EN_OC MUTE_OC GND | 143.0 | 147.0 | 90.0 | TOP |
| JP501 | I2C VCC SELECT | 68.8 | 130.0 | 0.0 | TOP |
| JP502 | SPI VCC SELECT | 94.0 | 137.0 | 0.0 | TOP |
| JP601 | PULL-UP ENABLE 2x3 | 103.2 | 136.5 | 0.0 | TOP |
| JP602 | I2C PULL-UP / 2x2 / 2.54mm | 81.5 | 141.8 | 0.0 | TOP |
| Q101 | FDD6685 DPAK | 52.3 | 113.0 | 0.0 | TOP |
| Q401 | MMBT3904 / reset OC | 116.0 | 64.0 | 0.0 | TOP |
| Q503 | MMBT3904 BL drive | 116.0 | 71.0 | 0.0 | TOP |
| Q504 | AO3401A BL high-side | 121.3 | 71.0 | 0.0 | TOP |
| Q601 | MMBT3904 EN OC | 142.0 | 132.0 | 90.0 | TOP |
| Q602 | MMBT3904 MUTE OC | 82.6 | 136.1 | 90.0 | TOP |
| R101 | 300R 1% / 0.125W | 56.8 | 130.25 | 0.0 | TOP |
| R201 | 33R | 62.0 | 73.0 | 90.0 | TOP |
| R202 | 33R | 62.0 | 78.0 | 90.0 | TOP |
| R203 | 33R | 62.0 | 83.0 | 90.0 | TOP |
| R204 | 100R 1% | 63.0 | 88.0 | 90.0 | TOP |
| R205 | 10k | 97.0 | 96.3 | 90.0 | TOP |
| R301 | 10k | 128.8 | 75.5 | 90.0 | TOP |
| R401 | 6k8 1% | 111.0 | 61.0 | 90.0 | TOP |
| R402 | 100k | 111.0 | 66.0 | 90.0 | TOP |
| R503 | 100k | 101.5 | 70.0 | 90.0 | TOP |
| R504 | 100R | 96.5 | 74.0 | 90.0 | TOP |
| R505 | 10k | 105.5 | 71.5 | 0.0 | TOP |
| R506 | 10k 1% | 111.0 | 71.5 | 90.0 | TOP |
| R507 | 10k | 116.0 | 76.0 | 0.0 | TOP |
| R508 | 100k | 121.5 | 76.0 | 0.0 | TOP |
| R601 | 10k | 98.5 | 136.2 | 0.0 | TOP |
| R602 | 10k | 98.5 | 140.1 | 0.0 | TOP |
| R603 | 10k | 98.5 | 144.0 | 0.0 | TOP |
| R604 | 4k7 | 82.0 | 126.5 | 90.0 | TOP |
| R605 | 4k7 | 82.0 | 131.5 | 90.0 | TOP |
| R606 | 6k8 1% | 82.0 | 116.5 | 90.0 | TOP |
| R607 | 100k | 82.0 | 121.5 | 90.0 | TOP |
| R608 | 6k8 1% | 82.0 | 147.8 | 0.0 | TOP |
| R609 | 100k | 79.35 | 135.9 | 90.0 | TOP |
| U101 | AMS1117-3.3 (UMW) | 54.8 | 135.5 | 0.0 | TOP |
| U201 | ESP32-S3 DevKitC-1 N16R8 (*) | 66.5 | 56.9 | 0.0 | TOP |
| U301 | PCM5102A MODULE / JACK RIGHT | 140.0 | 75.0 | 90.0 | TOP |
| U501 | SN74LVC1G17DBV | 106.0 | 65.0 | 0.0 | TOP |
| U601 | DS3231 for Pi / 5 POS | 104.5 | 80.12 | 0.0 | TOP |
