# Moduły i RF — PROVISIONAL

Współrzędne niżej są lokalne względem lewego górnego naroża FR4(0,0),Yw dół; natywne KiCad ma dodane(50,50)mm.

| Obszar | Obrys lokalny mm | Uwaga |
|---|---|---|
| MAIN | [16.5, 0.5, 44.5, 63.9] | pełna referencja, nie pomiar klona |
| DAC | [81.5, 7.5, 100.0, 39.4] | pełna referencja, nie pomiar klona |
| BT | [59.5, 54.4, 89.98, 91.22999999999999] | pełna referencja, nie pomiar klona |
| RTC | [47, 25, 60.4, 38.4] | pełna referencja, nie pomiar klona |

MAIN28×63.4 obejmuje konserwatywne6.4 mm anteny ponad obrysem bibliotecznym28×57. Antena MAIN(21.5,0.5)…(39.5,6.9),BT(59.5,54.4)…(89.98,60.75). Dwie rzeczywiste ruleareasF.Cu/B.Cu pod antenami przeniesiono z modułami; zakaz ścieżek/przelotek/padów/wypełnień w rzucie. Osobno inne części trzymano15 mm od anten. Moduł będący właścicielem własnej anteny jest z tego testu wyłączony; nie wyłączono jego konfliktów z cudzą anteną.

15 mm pochodzi z zachowanego kryterium poprzedniej rewizji. To analiza XY, nie symulacja RF. Anteny nadal nad FR4 — nie zaprojektowano wycięć. Pusta duża strefa między RTC a BT jest w dużej mierze buforem RF, nie miejscem na dowolną drobnicę. Nie zmniejszano tej rezerwy dla atrakcyjniejszych proporcji.

## Rozbieżność DAC

Wstępny dokument podawał około17.45×31.9 mm. Faktyczny rysunek źródłowego footprintu po obrocie ma krawędzie w X−8.5 i czoło jacka X+10 względem origin: konserwatywna suma **18.5×31.9 mm**, nie17.45 mm. Zastosowano większą sumę, również dlaRF/M3. Jack nie jest powodem do przerysowywania padów ani do zmniejszenia obrysu. Pełny prostokąt jest konserwatywną otoczką również pustych naroży przy wystającym jacku; nie modelem3D.

Oba wewnętrzne rzędy BT pozostają wspólnego położenia i0°;U2010°,U30190°. Zachowano79 pinów modułów, wszystkie UUID, funkcje, lokalne geometrie i sieci. Tabela znajduje się w DETAIL_METRICS.json. Rozstawy MAIN25.40,BT22.86,raster2.54 pozostają biblioteczne do pomiaru realnych płytek.

Model MAIN jest lokalny, nie do złączaono go doGitHub. Brak pełnych bryłBT/DAC/RTC/F101; obecne rzeczywiste podstawki są widoczne. STEP DAC pozostał odłączony. Wysokość podstawek8.5 mm i C101 model H16vsdocelowe H12.5 pozostają niepotwierdzone/niezgodne jak wcześniej.
