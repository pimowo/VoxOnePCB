# Porównanie PCB-LAYOUT-2 / PCB-LAYOUT-3

Źródło layout2 sprawdzono bezpośrednio i przez raporty, nie opierano się wyłącznie na deklarowanych liczbach. Odległości dotyczą referencyjnej geometrii, nie pomiaru klonów. Układ odniesieniaEdge.Cuts50…150mm.

| Parametr | PCB-LAYOUT-2 | PCB-LAYOUT-3 |
|---|---|---|
| MAIN | 180°,USBUP,antennaDOWN | 0°,antennaUP,USBDOWN |
| Antena MAIN do górnej krawędzi | 60,0mm | 0,5mm |
| USB MAIN | Ku górze; płaszczyzna y53,3mm od krawędzi | Ku dołowi; płaszczyzna referencyjna y113,9,36,1mm od dolnej krawędzi;2wtyki9×18 i2kableØ4 |
| Jack DAC | UP,facey54,4mm od górnej krawędzi | RIGHT,facex150,0mm od prawej krawędzi |
| DAC | 31,9×16,9 poziomo,obrót180° | 16,9×31,9 pionowo,obrót90°; wszystkie15padów bez zmian |
| BT | Origin126;124,05; body110,76…141,24 / 105…141,83 | Origin124,74;127,55; body109,5…139,98 / 108,5…145,33;USBhousing do151,68 |
| RTC | Pin1(103,5;77,6),body96,8…110,2 / 75,98…89,38 | Pin1(104,5;80,12),body97,8…111,2 / 78,5…91,9 |
| Minimalny odstęp RTC | 0,405mm do C203;0,625mm do kolumny | 2,095mm do R205;2,475mm do C601;3,3mm do MAIN |
| I2C | Dolny rząd,J501(61;147,8) | J501(60,5;147,8),przed kanałem USB,JP501 w tym samym dolnym bloku |
| SPI | J502(74;147,8),nad nimMAIN antena | J502(94;147,8),po prawej od kanału drugiego USB;JP502 nad złączem |
| INPUT | J601(98;147,8),JP601(124;88) | J601(131,4;147),JP601(103,2;136,5):bliżej niż poprzednio,lecz nadal około32mm |
| AMP | J603(112;147,8) | J603(143;147),prawy koniec dolnego rzędu |
| JP602 | (101;138),90°,pary pionowe | (81,5;141,8),0°,pary poziome1–2SDA,3–4SCL |
| TOP/BOTTOM | 77/0 | 77/0 |
| ERC | 0errors/0warnings | 0errors/0warnings |
| DRC | 173niepołączenia,0pozostałych | 173niepołączenia,0pozostałych |
| Nadruk DRC | 0ostrzeżeń | 0ostrzeżeń;7ref wyłącznieF.Fab jawnie |
| Problemy montażowe | RTC<1mm,MAINodrzuconaorientacja,DACnieRIGHT | LepszeodstępyRTC;długiekorytarzeUSB,złączki0,4mm odBT,przesunięteM3,nieznaneZ i klony pozostająPROVISIONAL |

## Podobieństwo do wizualizacji referencyjnej

Spełnione: MAIN pionowo po lewej, antena ku zewnętrznej górze, USB w dół; POWER po lewej; DAC u góry po prawej, dostęp do jacka od zewnątrz; BT prawa i płasko; RTC między MAIN a BT/pod sekcją audio; dolna kolejność I2C,SPI,INPUT,AMP; zielona płytka, podpisane grupy i zworki. Poprawiono konkretnie odrzucone kierunki MAIN i jacka oraz odstępyRTC.

Nieodtworzone dosłownie: proporcje prostokątnej koncepcji, poziomy szeroki DAC, JST, dodatkowe etykiety/pinyARK i pełne bryły modeli. Logo jest w wolnej górnej części zamiast lewego narożnika zajętego przez RF. Duże wolne pola wynikają z RF i kabli, nie są metryką gorszego wykorzystania powierzchni. BlokRESET/BL jest w górnej strefie sterowania; JP601 nie stoi bezpośrednio obok J601. Nie deklaruje się pełnej zgodności wszystkich życzeń bliskości ani gotowości do produkcji; użytkownik ma ocenić tę kompozycję i wymienione kompromisy.
