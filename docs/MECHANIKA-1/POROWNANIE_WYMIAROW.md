# Porównanie wymiarów — kandydaci, nie decyzja

Wszystkie warianty są poziomymi prostokątami.100×100 nie jest traktowane jako rozwiązanie tego etapu.

| Wariant mm | Układy3modułów/RF/kabli | Po M3 i RTC | Pełny montaż TOP | Status |
|---|---|---|---|---|
| 100×75 | 300 | 0 | nie wykonano pełnego PCB | BLOCKED |
| 100×80 | 1200 | 0 | nie wykonano pełnego PCB | BLOCKED |
| 100×85 | 2778 | 0 | nie wykonano pełnego PCB | BLOCKED |
| 100×90 | 6438 | 0 | nie wykonano pełnego PCB | BLOCKED |
| 100×95 | 12702 | 120 | 77/77 | PROVISIONAL FEASIBLE — XY; serwis BLOCKED |

Liczba wyników jest liczbą pozycji w jawnej siatce, nie metryką jakości ani prawdopodobieństwem wykonalności. Dla95 końcowy kandydat dopracowano w pozycjach ułamkowych osobno.

## Wymagana kontrola funkcji i dostępu

| Parametr | 100×75 | 100×80 | 100×85 | 100×90 | 100×95 |
|---|---|---|---|---|---|
| MAIN28×63.4 | sam mieści się | sam mieści się | sam mieści się | sam mieści się | mieści się;ant UP0.5 mm |
| DAC + jack | mieści się oddzielnie;diagnostyka DAC niżej | jw. | górna prawa,konflikt M3 | jw. | górna prawa,jackface0 mm |
| BT30.48×36.83 | mieści się oddzielnie;szukano obok DAC | jw. | pod DAC w przykładzie | jw. | prawa,ant UP,USBdown |
| RTC diagnostyczne minimum do modułu | 2.000 mm* | 2.000 mm* | 4.000 mm* | 4.000 mm* | 2.175 mm do C602,pełne77 |
| 4×M3/Ø7 | brak2 prawych w pokazanym układzie | brakprawego górnego | brakprawego górnego | brakprawego górnego | 4×M3;H901 y11.5 |
| RF innych części | sprawdzono dla makro,nie 77 | jw. | jw. | jw. | min15.000 mm;łby15.078 mm |
| USB MAIN | brakpełnejbramy;wtyk+6.9 mm poza FR4** | +1.9 mm** | wewnętrznykorytarz** | wewnętrznykorytarz** | 2×9×18 mm,Ø4,0.325 mm margines doobrysu |
| USB BT | korytarz makro,brakpełnego77 | jw. | jw. | jw. | housing+2.58 mm,wtykdo+20.58 mm |
| Jack | w prawo,0 mm przyjętegeometrycznie | jw. | jw. | jw. | w prawo,0 mm;wtyk18 mmpoza PCB |
| I2C/SPI/INPUT/AMP | nierozstrzygniętebez77 | jw. | jw. | jw. | I2C/SPI/INPUTdół,AMPprawydół;dostępP1 |
| Zworki | nierozstrzygnięte | jw. | jw. | jw. | JP50113.1/JP5029.9/JP60119.1/JP60221.7mm do złącza |
| Zgodnośćkompozycji | diagnostyka odwraca stosDAC/BT | jw. | DACnad BT,ale M3 blokuje | jw. | głównekierunkitak;proporcja100:95 bliższa kwadratu |
| Routing | brak dowodu;dużeryzyko | dużeryzyko | dużeryzyko | dużeryzyko | niezweryfikowany;RFrozdzielapasymożliwychtras |

* Odległość RTC w niepełnym diagnostycznym układzie czterech obrysów, z brakującym M3, NIE w zatwierdzonym PCB77 części. Minimum rzeczywiste dla wszystkich części tych wariantów jest nieustalone; nie przypisuje się mu fikcyjnej liczby.

** Przy antenie MAIN0.5 mm od góry USBfacey63.9. Wysokość75/80nie jest automatycznie niemożliwa: część wtyku może wyjść poza laminat. Brak pełnego dostępu/złączy nie został zastąpiony samym porównaniem wysokości.

Zachowanie bezpośredniego stosu z górnym prawym M3 i przyjętymi rezerwami daje7.5+31.9+15+36.83=**91.23 mm** do końca płytki BT. To dolne ograniczenie TEJ rodziny układu, nie wszystkich możliwych rozmieszczeń. Dla 75/80/85/90deficyt tego stosu wynosi16.23/11.23/6.23/1.23mm jeszcze przed dolnymi złączami.95 ma na nie3.77 mm; pokazany kandydat wykorzystuje ten pas. Nie twierdzę, że95 jest globalnym minimum.
