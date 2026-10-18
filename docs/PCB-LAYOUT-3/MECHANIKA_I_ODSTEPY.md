# Mechanika i odstępy — dane referencyjne

Wynik niezależnego pcbnew LoadBoard: brak kolizji referencyjnych pełnych obrysów modułów z innymi częściami, rezerwami M3 i korytarzami wtyków/kabli. KontrolaF.CrtYd z CLI jest osobna od kontroli całych modułów. Dla standardowych goldpinów przy kontroli fizycznej użyto obrysu2,54mm z fabrycznegoF.Fab, nie większego prostokąta courtyard. To rozróżnienie jest jawne w MECHANICAL_CHECK.json; żadnych bibliotek ani padów nie zmieniano.

| Obszar | Współrzędne / rezerwa |
|---|---|
| MAIN pełny | (66,5;50,5)…(94,5;113,9),w tym konserwatywne6,4mm anteny |
| MAIN antena | (71,5;50,5)…(89,5;56,9);0,5mm od góry |
| MAIN USB1 | wtyk(71,5;113,9)…(80,5;131,9);kabel(74;131,9)…(78;155) |
| MAIN USB2 | wtyk(84,5;113,9)…(93,5;131,9);kabel(87;131,9)…(91;155) |
| DAC | (131,55;59,05)…(148,45;90,95);jackface(150;64,45) |
| Jack wtyk | (150;59,95)…(168;68,95),wyjście18mm poza prawą krawędź |
| BT | (109,5;108,5)…(139,98;145,33);antena do114,85 |
| BT USB | referencyjna obudowa do151,68:1,68mm poza laminat;wtyk do163,33:13,33mm poza laminat |
| RTC | (97,8;78,5)…(111,2;91,9);minimum2,095mm od R205 |
| M3 | H901(53,5;61,5),H902(145;55),H903(55;145),H904(146,5;141,5);NPTH3,2mm,łbyØ7mm |

Wzór M3 nie jest już symetrycznym90×90: H901 odsunięto dla metalowego łba przy antenie, H904 dla dolnego AMP i odsprzęganiaBT. Są to obiekty mechaniczne, nie nowe części elektryczne. Nie założono istniejącej obudowy ani dopasowania rozstawu do niej; wymaga akceptacji użytkownika. Łby/podkładki większe niżØ7mm wymagają ponownego sprawdzenia.

Wszystkie inne komponenty/moduły mają minimum15,000mm od referencyjnych anten. Dla rzeczywistych okrągłych rezerw łbów Ø7mm najmniejsza odległość to H901–MAIN około15,078mm. To analiza2D XY, nie symulacjaRF. Dwie prawdziwe strefy zakazu miedzi w projekcji anten są na obu warstwach. Nie ma miedzi trasowania ani wypełnień w całym projekcie.

Wytyczne [Espressif ESP32-S3](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html#general-principles-of-pcb-layout-for-modules-positioning-a-module-on-a-base-board) preferują antenę poza płytą bazową i zalecają odstęp otoczenia15mm. MAIN jest blisko krawędzi, ale nadal nad FR4 M1. Nie wykonano wycięcia laminatu; nie uznaje się tego za pełną walidacjęRF. Dla [ESP32/BT](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/pcb-layout-design.html) również potrzebne są testy rzeczywistego modułu i obudowy. Przed routingiem trzeba osobno ustalić pełne bufory miedzi/masy wokół anten i własnych padów modułów, nie automatycznie wypełniać obszaru poza obecnym prostokątem.

Wtyki MAIN9×18mm, kabelØ4mm i wtykBT10×18mm są rezerwami projektowymi, nie pomiarami wybranego kabla. USB MAIN kończy się referencyjnie36,1mm od dolnej krawędzi; po18mm wtyku pozostaje18,1mm drogi kabla po laminacie. Nie jest to USB bezpośrednio na dolnej krawędzi. Wymagany rzeczywisty test wkładania obu wtyków, odgiętki i braku naprężeń. Nie oparto dostępu na niezweryfikowanym prowadzeniu kabla nad innymi częściami.

DolneINPUT ma0,400mm między nominalnym plastikowym obrysem złącza a pełnym obrysemBT, około0,390mm między końcem rezerwy wtykuUSB BT i obrysemINPUT. Courtyard standardowego złącza może wchodzić w konserwatywny rzut modułu, podczas gdy rzeczywisteF.Fab i pady są poza nim; nie traktuje się tego jako potwierdzenia tolerancji. Dostęp palcami przewidziano od zewnętrznej dolnej krawędzi. P1 wymaga pomiaru rzeczywistych wtyków i próby serwisowej.

Odsprzęganie i sterowanie nie są ukryte pod modułami. C301100n ma 3,918mm między padem zasilania1 iVIN A6. C30210n i C30310µF mają odpowiednio20,659mm i20,449mm odVIN, a JP601 od środkaJ601 około32mm; te kompromisy pozostają do świadomej oceny, nie deklaruje się idealnej bliskości. Wszystkie dokładne pozycje i najmniejsze odległości zapisano w JSON i ROZMIESZCZENIE.md.

Brak pełnych bryłBT/DAC/RTC/F101 i niepotwierdzone wysokości podstawek, baterii, wtyków oraz tolerancji uniemożliwiają pełną kontrolęZ. Courtyard i powyższe obrysy nie zastępują kontroliSTEP–STEP ani fizycznego montażu. Dokładne klony nadalPROVISIONAL.
